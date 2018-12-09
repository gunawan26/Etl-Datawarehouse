import datetime
from ExtractDatabase import MyEtl


qCountTableDimensional = "SELECT count(*) from information_schema.TABLES where TABLE_SCHEMA = 'db_dimensional'"
qCountTableConfig = "SELECT COUNT(*) FROM tb_info_table"
qGetTableDimensional = "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'db_dimensional' "
qInsertTableConfig = "INSERT INTO tb_info_table(nama_table) VALUES('%s')"
qInsertUpdateLog = "INSERT INTO update_log(update_date,batch) VALUES('{0}',{1})"
qInsertdetailConfig = "INSERT INTO tb_detail_update VALUES(NULL,{0},'{1}',{2},{3},{4})"
#==============BATCH INFO UPDATE TABLE===============#
qGetBatchInfo = "SELECT MAX(batch) FROM update_log"

#================== Analyze Table====================#



class UpdateConfig:

    def __init__(self,connection_to_config,config,connection_to_dimen,dimen,connection_to_source,source):
        self.connection_to_config = connection_to_config
        self.config = config
        self.connection_to_dimen = connection_to_dimen
        self.dimen = dimen
        self.connection_to_source = connection_to_source
        self.source = source

        #self.on_update(source,dimen,connection_to_dimen,config)
        pass

    def get_max(self,db_source_args,table_name_args,id_name_args):
        qMax = "SELECT MAX({0}) AS max_id FROM {1}".format(id_name_args,table_name_args)
        db_source_args.execute(qMax)
        val = db_source_args.fetchone()
        new_val = val[0]
        if new_val is None:
            new_val = 0

        return new_val


    def get_min(self,db_source_args,table_name_args,id_name_args):
        qMin = "SELECT MIN({0}) AS min_id FROM {1}".format(id_name_args,table_name_args)
        db_source_args.execute(qMin)
        val = db_source_args.fetchone()
        new_val = val[0]
        if new_val is None:
            new_val = 0

        return new_val


    def where_q(self,args_id_field,args_id):
        q = " WHERE {0} > {1}".format(args_id_field,int(args_id))
        return q


    def on_update(self,ds,dm,dbdimen,dconfig):
        global  uptodate_info
        global counter_update
        global qGEtTimeNow
        global last_id_config

        last_id_config = 0

        qGEtTimeNow = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

        counter_update = 0
        uptodate_info = True
        etl = MyEtl()
        dconfig.execute("SELECT MAX(batch) FROM update_log")
        val = dconfig.fetchone()

        dm.execute("SELECT COUNT(*) FROM tb_dimensi_bulan")
        count_bulan_val = dm.fetchone()
        count_bulan = count_bulan_val[0]
        my_val = val[0]

        if my_val is None:
            my_val = 1
        else:
            my_val+=1



        get_max_tb_brg = self.get_max(ds,"tb_barang","id_barang")
        get_max_det_trans = self.get_max(ds,"tb_detail_transaksi","id_detail_trans")
        get_max_customer = self.get_max(ds,"tb_member","id_member")
        get_max_pegawai = self.get_max(ds,"tb_pegawai","id_pegawai")
        get_max_cabang = self.get_max(ds,"tb_cabang","id_cabang")


        get_max_dimensi_brg = self.get_max(dm,"tb_dimensi_barang","id_barang")
        get_max_dimensi_transaksi = self.get_max(dm,"tb_dimensi_transaksi","id_detail_transaksi")
        get_max_dimensi_customer = self.get_max(dm,"tb_dimensi_customer","id_customer")
        get_max_dimensi_pegawai = self.get_max(dm,"tb_dimensi_pegawai","id_pegawai")
        get_max_dimensi_cabang = self.get_max(dm,"tb_dimensi_cabang","id_cabang")


        getmin_dimensi_barang    = self.get_min(dm,"tb_dimensi_barang","id_barang")
        getmin_dimensi_cabang    = self.get_min(dm,"tb_dimensi_cabang","id_cabang")
        getmin_dimensi_customer  = self.get_min(dm,"tb_dimensi_customer","id_customer")
        getmin_dimensi_transaksi = self.get_min(dm,"tb_dimensi_transaksi","id_dimensi_trans")
        getmin_dimensi_pegawai = self.get_min(dm,"tb_dimensi_pegawai","id_pegawai")


        if count_bulan == 0:
            etl.tableSourceToDestination(dm, dm ,dbdimen, etl.qSelectBulan,etl.qInsertBulan)
            print("successful insert table dimensi bulan")

        self.is_update(get_max_customer,get_max_dimensi_customer, getmin_dimensi_customer,ds,dm,dbdimen,etl.qCustomer,etl.qInsertCustomer,"id_customer","tb_dimensi_customer")
        self.is_update(get_max_tb_brg,get_max_dimensi_brg, getmin_dimensi_barang,ds,dm,dbdimen,etl.qBarang,etl.qInsertBarang,"id_barang","tb_dimensi_barang")
        self.is_update(get_max_pegawai,get_max_dimensi_pegawai, getmin_dimensi_pegawai,ds,dm,dbdimen,etl.qPegawai,etl.qInsertPegawai,"id_pegawai","tb_dimensi_pegawai")
        self.is_update(get_max_cabang,get_max_dimensi_cabang, getmin_dimensi_cabang,ds,dm,dbdimen,etl.qCabang,etl.qInsertCabang,"id_cabang","tb_dimensi_cabang")
        self.is_update(get_max_det_trans,get_max_dimensi_transaksi, getmin_dimensi_transaksi,ds,dm,dbdimen,etl.qTransaksi,etl.qInsertTransaksi,"id_detail_trans","tb_dimensi_transaksi")


        print(uptodate_info)
        if uptodate_info == False:
            dm.execute("SET FOREIGN_KEY_CHECKS=0;")
            etl.truncateDatabase(dm,etl.qTruncateData)
            etl.tableSourceToDestination(dm,dm,dbdimen,etl.qDimensiTransBulan,etl.qInsertFaktaTransaksiBulan)
            etl.tableSourceToDestination(dm, dm, dbdimen, etl.qDimensiTransTahun, etl.qInsertFaktaTransaksiTahun)
            etl.tableSourceToDestination(dm, dm, dbdimen, etl.qDimensiTransCustomerBulan, etl.qInsertFaktaCustomer)
            etl.tableSourceToDestination(dm, dm, dbdimen, etl.qDimensiTransPegawai, etl.qInsertFaktaPegawai)
            etl.tableSourceToDestination(dm, dm, dbdimen, etl.qDimensiTransTahunPerCabang,etl.qInsertFaktaTransaksiTahunPerCabang)
            dbdimen.commit()

        return uptodate_info


    def is_update(self,max_source,max_dimens,min_dimens,ds_args,dm_args,db_dimen_args,etl_source_args,etl_insert_args,val_id_q,table_name):
        global uptodate_info
        global counter_update
        global qGEtTimeNow
        global last_id_config
        global config
        config = self.config
        global connection_to_config
        connection_to_config = self.connection_to_config
        etl_new = MyEtl()
        if max_source > max_dimens:
            counter_update +=1
            if min_dimens == 0:
                etl_new.tableSourceToDestination(ds_args,dm_args,db_dimen_args,etl_source_args,etl_insert_args)
            else:
                new_q = self.where_q(val_id_q,max_dimens)
                etl_new.tableSourceToDestination(ds_args, dm_args, db_dimen_args,etl_source_args+new_q,etl_insert_args)

            uptodate_info = False
            print(counter_update)
            if counter_update == 1:
                config.execute(qGetBatchInfo)
                batch_val = config.fetchone()
                if batch_val[0] is None:
                    new_batch = 1

                else:
                    new_batch = batch_val[0]+1


                print("INSERT INTO update_log(update_date,batch) VALUES('{0}',{1})".format(qGEtTimeNow,new_batch))
                config.execute("INSERT INTO update_log(update_date,batch) VALUES('{0}',{1})".format(qGEtTimeNow,new_batch))
                connection_to_config.commit()

                config.execute("SELECT MAX(log_id) FROM update_log")
                val = config.fetchone()
                last_id_config = val[0]
                print(last_id_config)


            row_inserted = max_source - max_dimens
            print(qInsertdetailConfig.format(last_id_config,table_name,min_dimens,max_dimens,row_inserted))
            config.execute(qInsertdetailConfig.format(last_id_config,table_name,min_dimens,max_dimens,row_inserted))
            connection_to_config.commit()



    def update_val(self,dm,ds):
        update_result = {}
        get_max_tb_brg = self.get_max(ds,"tb_barang","id_barang")
        get_max_det_trans = self.get_max(ds,"tb_detail_transaksi","id_detail_trans")
        get_max_customer = self.get_max(ds,"tb_member","id_member")
        get_max_cabang = self.get_max(ds,"tb_cabang","id_cabang")

        get_max_dimensi_brg = self.get_max(dm,"tb_dimensi_barang","id_barang")
        get_max_dimensi_transaksi = self.get_max(dm,"tb_dimensi_transaksi","id_detail_transaksi")
        get_max_dimensi_pegawai = self.get_max(dm,"tb_dimensi_pegawai","id_pegawai")
        get_max_dimensi_cabang = self.get_max(dm,"tb_dimensi_cabang","id_cabang")
        get_max_dimensi_customer = self.get_max(dm, "tb_dimensi_customer", "id_customer")

        if get_max_tb_brg > get_max_dimensi_brg:
            new_q =  "SELECT COUNT(*) FROM tb_barang WHERE id_barang > {0}".format(get_max_dimensi_brg)
            update_result["tb_barang"] = self.ret_update_return_result(ds,new_q)

        if get_max_det_trans > get_max_dimensi_transaksi:
            new_q2 = "SELECT COUNT(*) FROM tb_detail_transaksi WHERE id_detail_trans > {0}".format(get_max_dimensi_transaksi)
            update_result["tb_detail_transaksi"] = self.ret_update_return_result(ds,new_q2)


        if get_max_customer > get_max_dimensi_customer:
            new_q3 = "SELECT COUNT(*) FROM  tb_member WHERE id_member > {0}".format(get_max_dimensi_customer)
            update_result["tb_customer"] = self.ret_update_return_result(ds,new_q3)

        if get_max_cabang >get_max_dimensi_cabang:
            new_q4 = "SELECT COUNT(*) FROM tb_cabang WHERE id_cabang > {0}".format(get_max_dimensi_cabang)
            update_result["tb_cabang"] = self.ret_update_return_result(ds,new_q4)

        return update_result


    def ret_update_return_result(self,ds,q):
        ds.execute(q)
        n_val = ds.fetchone()
        f_val = n_val[0]
        return f_val


    def get_last_update(self,config):
        config.execute("SELECT MAX(update_date),MAX(batch) FROM update_log")
        val = config.fetchone()
        value_tgl = str(val[0])
        value_batch = val[1]

        return value_tgl,value_batch


def main():
    UpdateConfig()


if __name__ == "__main__":
    main()