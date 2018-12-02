from Connector import sql_connect
import datetime
from ExtractDatabase import MyEtl

connection_to_config = sql_connect('db_config_data_w')
config = connection_to_config.cursor()
connection_to_dimen = sql_connect('db_dimensional')
dimen = connection_to_dimen.cursor()
connection_to_source = sql_connect('db_supermarket')
source = connection_to_source.cursor()


qCountTableDimensional = "SELECT count(*) from information_schema.TABLES where TABLE_SCHEMA = 'db_dimensional'"
qCountTableConfig = "SELECT COUNT(*) FROM tb_info_table"

qGetTableDimensional = "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'db_dimensional' "

qInsertTableConfig = "INSERT INTO tb_info_table(nama_table) VALUES('%s')"

qInsertUpdateLog = "INSERT INTO update_log(update_date,batch) VALUES('{0}',{1})"

#==============BATCH INFO UPDATE TABLE===============#
qGetBatchInfo = "SELECT COUNT(*) FROM update_log"
qGEtTimeNow = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')


#================== Analyze Table====================#



class UpdateConfig:

    def __init__(self):
        self.get_table_from_dimen()
        self.on_update(source,dimen,connection_to_dimen,config)
        pass



    def get_table_from_dimen(self):

        dimen.execute(qCountTableDimensional)
        config.execute(qCountTableConfig)
        count_table_dimen = dimen.fetchone()
        count_table_config = config.fetchone()
        count_table_dimen = int(count_table_dimen[0])
        count_table_config = int(count_table_config[0 ])


        if count_table_dimen > count_table_config:
            dimen.execute(qGetTableDimensional)

            val = dimen

            for x in val.fetchall():
                val_table = "".join(x)
                print(val_table)
                config.execute(qInsertTableConfig%val_table)
                connection_to_config.commit()
        else:
            print("banyak tabel  sudah up todated")



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
        uptodate_info = True
        etl = MyEtl()
        dconfig.execute("SELECT MAX(batch) FROM update_log")
        val = dconfig.fetchone()

        dm.execute("SELECT COUNT(*) FROM tb_dimensi_bulan")
        count_bulan = dm.fetchone()

        my_val = val[0]

        if my_val is None:
            my_val = 1
        else:
            my_val+=1

        dconfig.execute(qInsertUpdateLog.format(qGEtTimeNow,my_val))
        print(qInsertUpdateLog.format(qGEtTimeNow,my_val))

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
            etl.tableSourceToDestination(dm, dm ,dbdimen, etl.qSelectBulan,etl.qSelectBulan)
            print("successful insert table dimensi bulan")

        if get_max_customer > get_max_dimensi_customer:
            if getmin_dimensi_customer == 0:
                etl.tableSourceToDestination(ds, dm, dbdimen, etl.qCustomer, etl.qInsertCustomer)

            else:
                new_q_customer = self.where_q("id_customer",get_max_dimensi_customer)
                etl.tableSourceToDestination(ds,dm,dbdimen,etl.qCustomer+new_q_customer,etl.qInsertCustomer)
            uptodate_info = False


        if get_max_tb_brg > get_max_dimensi_brg:
            if getmin_dimensi_barang == 0:
                etl.tableSourceToDestination(ds, dm, dbdimen, etl.qBarang, etl.qInsertBarang)

            else:
                new_q_brg = self.where_q("id_barang",int(get_max_dimensi_brg))
                etl.tableSourceToDestination(ds,dm,dbdimen,etl.qBarang+new_q_brg,etl.qInsertBarang)
                print("test")
            uptodate_info = False


        if get_max_pegawai > get_max_dimensi_pegawai:
            if getmin_dimensi_cabang == 0:
                etl.tableSourceToDestination(ds, dm, dbdimen, etl.qPegawai, etl.qInsertPegawai)
            else:
                new_q_pegawai = self.where_q("id_pegawai",get_max_dimensi_pegawai)
                etl.tableSourceToDestination(ds,dm,dbdimen,etl.qPegawai+new_q_pegawai,etl.qInsertPegawai)
            uptodate_info = False


        if get_max_cabang > get_max_dimensi_cabang:
            if getmin_dimensi_cabang == 0:
                etl.tableSourceToDestination(ds, dm, dbdimen, etl.qCabang, etl.qInsertCabang)
            else:
                new_q_cabang = self.where_q("id_cabang",get_max_dimensi_cabang)
                etl.tableSourceToDestination(ds,dm,dbdimen,etl.qCabang+new_q_cabang,etl.qInsertCabang)

            uptodate_info = False


        if get_max_det_trans > get_max_dimensi_transaksi:
            if getmin_dimensi_transaksi == 0:

                etl.tableSourceToDestination(ds, dm, dbdimen, etl.qTransaksi, etl.qInsertTransaksi)

            else:
                new_q_trans = self.where_q("id_det_transaksi",get_max_dimensi_transaksi)
                etl.tableSourceToDestination(ds, dm, dbdimen, etl.qTransaksi+new_q_trans,etl.qInsertTransaksi)

            uptodate_info = False


        if uptodate_info == False:
            dm.execute("SET FOREIGN_KEY_CHECKS=0;")
            print("masuk pak eko")
            etl.tableSourceToDestination(dm,dm,dbdimen,etl.qDimensiTransBulan,etl.qInsertFaktaTransaksiBulan)
            etl.tableSourceToDestination(dm, dm, dbdimen, etl.qDimensiTransTahun, etl.qInsertFaktaTransaksiTahun)
            etl.tableSourceToDestination(dm, dm, dbdimen, etl.qDimensiTransCustomerBulan, etl.qInsertFaktaCustomer)
            etl.tableSourceToDestination(dm, dm, dbdimen, etl.qDimensiTransPegawai, etl.qInsertFaktaPegawai)
            etl.tableSourceToDestination(dm, dm, dbdimen, etl.qDimensiTransTahunPerCabang,etl.qInsertFaktaTransaksiTahunPerCabang)
            dbdimen.commit()




def main():
    UpdateConfig()


if __name__ == "__main__":
    main()