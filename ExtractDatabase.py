

databaseSumber = "db_supermarket"
databaseDimensional = "db_dimensional"

qtruncate_all_dimen = "SELECT CONCAT('TRUNCATE TABLE ', TABLE_NAME) FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'db_dimensional' "

qtruncate_all_config = "select concat('TRUNCATE TABLE ',TABLE_NAME) FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'db_config_data_w' "


#
class MyEtl():


    #======================== LIST EXTRACT TRANSFORM DATA ==============    ==========#
    qBarang = "SELECT id_barang,tb_kategori_barang.nama_kat_brg,nama_barang " \
              "FROM tb_barang INNER JOIN tb_kategori_barang ON tb_barang.id_kat_brg = tb_kategori_barang.id_kat_brg"

    qCustomer = "SELECT id_member, nama_member, no_telp FROM tb_member"

    qPegawai = "SELECT `tb_pegawai`.`id_pegawai`, `tb_pegawai`.`nama_pegawai`, `tb_role`.`nama_role` FROM `tb_pegawai`" \
               "INNER JOIN `tb_role` ON `tb_role`.`id_role` = `tb_pegawai`.`id_role`"

    qCabang = 'SELECT tb_cabang.`id_cabang`, tb_cabang.`nama_cabang`, CONCAT(tb_cabang.`alamat`,", ",tb_kabupaten.`nama_kabupaten`,", ",tb_provinsi.`nama_provinsi`) AS alamat ' \
              'FROM tb_cabang ' \
              'INNER JOIN tb_kabupaten USING (id_kabupaten) ' \
              'INNER JOIN tb_provinsi USING  (id_provinsi)'

    qTransaksi = 'SELECT tb_detail_transaksi.`id_transaksi`, tb_transaksi.`id_member`,id_detail_trans, id_barang, harga_satuan AS harga_barang, jmlh_barang,'\
                'tb_transaksi.`id_cabang`,tb_pegawai.`id_pegawai`, tb_transaksi.`tgl_transaksi` '\
                'FROM tb_detail_transaksi '\
                'INNER JOIN tb_transaksi USING (id_transaksi)'\
                'INNER JOIN tb_pegawai USING (id_pegawai)'

    qDimensiTransBulan ='SELECT  id_barang,MONTH(tgl_transaksi) AS bulan,YEAR(tgl_transaksi) AS tahun,id_cabang,'\
                'SUM(jmlh_brg) AS total_terbeli, SUM(jmlh_brg*harga_barang) AS total_pendapatan '\
                'FROM tb_dimensi_transaksi GROUP BY id_barang,id_cabang,bulan'

    qDimensiTransTahun ='SELECT  id_barang,YEAR(tgl_transaksi) AS tahun,id_cabang,'\
                        'SUM(jmlh_brg) AS total_terbeli, SUM(jmlh_brg*harga_barang) AS total_pendapatan '\
                        'FROM tb_dimensi_transaksi GROUP BY id_barang,id_cabang,tahun'

    qDimensiTransCustomerBulan = 'SELECT id_user,id_barang, MONTH(tgl_transaksi) AS bulan, YEAR(tgl_transaksi),id_cabang,'\
                                'SUM(jmlh_brg*harga_barang) AS total_belanja,jmlh_brg FROM tb_dimensi_transaksi '\
                                'GROUP BY id_barang,id_cabang,bulan'

    qDimensiTransPegawai = 'SELECT id_pegawai,SUM(jmlh_brg*harga_barang)AS total_transaksi,MONTH(tgl_transaksi)AS bulan,YEAR(tgl_transaksi)tahun,'\
                            'id_cabang,COUNT(id_transaksi)AS banyak_transaksi FROM tb_dimensi_transaksi '\
                            'GROUP BY id_pegawai,bulan'

    qDimensiTransTahunPerCabang ='SELECT id_cabang,YEAR(tgl_transaksi) AS tahun, '\
                                'SUM(jmlh_brg*harga_barang) AS total_belanja FROM tb_dimensi_transaksi '\
                                'GROUP BY id_cabang,tahun'
    #==================================================================================================================================#

    qInsertBarang = "INSERT INTO tb_dimensi_barang(id_barang,kategori_barang,nama_barang) VALUES('%i','%s','%s');"

    qInsertCustomer = "INSERT INTO tb_dimensi_customer(id_customer,nama_customer,no_telp) VALUES('%i','%s','%s');"

    qInsertPegawai = "INSERT INTO tb_dimensi_pegawai(id_pegawai,nama_pegawai, role) VALUES('%i','%s','%s');"

    qInsertCabang = "INSERT INTO tb_dimensi_cabang(id_cabang,nama_cabang, alamat_kab_prov) VALUES('%i','%s','%s');"

    qInsertBulan = "INSERT INTO tb_dimensi_bulan VALUES(Null,   '%s');"

    qInsertTransaksi = "INSERT INTO tb_dimensi_transaksi(id_transaksi,id_user,id_detail_transaksi,id_barang,harga_barang,jmlh_brg,id_cabang,id_pegawai,tgl_transaksi) " \
                       "VALUES('%i','%i','%i','%i','%2.f','%i','%i','%i','%s');"

    qInsertFaktaTransaksiBulan = "INSERT INTO tb_fakta_trans_barang(id_barang,id_bulan,tahun,id_cabang,total_brg_terjual,total_pendapatan)"\
                            "values('%i','%i','%i','%i','%2.f','%2.f')"

    qInsertFaktaTransaksiTahun = "INSERT INTO tb_fakta_tahun(id_barang,tahun,id_cabang,total_brg_terjual,total_pendapatan)"\
                            "values('%i','%i','%i','%2.f','%2.f')"

    qInsertFaktaCustomer = "INSERT INTO tb_fakta_customer(id_customer,id_barang,id_bulan,tahun,id_cabang,total_belanja,banyak_brg)"\
                            "VALUES('%i','%i','%i','%i','%i','%2.f','%i')"

    qInsertFaktaPegawai = "INSERT INTO tb_fakta_pegawai(id_pegawai,total_transaksi,id_bulan,tahun,id_cabang,banyak_transaksi)"\
                        "VALUES('%i','%2.f','%i','%i','%i','%i')"

    qInsertFaktaTransaksiTahunPerCabang = "INSERT INTO tb_fkt_thn_gran_tinggi(id_cabang,tahun,total_trans) VALUES('%i','%i','%f')"
    #==================================================================================================================================#

    qTruncateData = "SELECT CONCAT('TRUNCATE TABLE ', TABLE_NAME) FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'db_dimensional' "\
                    "AND TABLE_NAME NOT IN (SELECT 'tb_dimensi_barang' UNION SELECT 'tb_dimensi_cabang' UNION SELECT 'tb_dimensi_bulan' "\
                    "UNION SELECT 'tb_dimensi_customer' UNION SELECT 'tb_dimensi_pegawai' UNION SELECT 'tb_dimensi_transaksi');"

    qSelectBulan = "SELECT 'januari' AS bulan UNION SELECT 'februari' UNION SELECT 'maret' UNION SELECT 'april' "\
                    "UNION SELECT 'mei' UNION SELECT 'juni' UNION SELECT 'juli' UNION SELECT 'agustus' "\
                    "UNION SELECT 'september' UNION SELECT 'oktober' "\
                    "UNION SELECT 'november' "\
                    "UNION SELECT 'desember' "


    #======================#
    qExportPenjualanTahun = "SELECT tb_dimensi_barang.`nama_barang`,tahun, tb_dimensi_cabang.`nama_cabang`,total_brg_terjual,total_pendapatan " \
        "FROM tb_fakta_tahun " \
        "INNER JOIN tb_dimensi_barang USING (id_barang) " \
        "INNER JOIN tb_dimensi_cabang USING (id_cabang)"

    ExportPenjualanBulan = "SELECT tb_dimensi_barang.`nama_barang`,tb_dimensi_bulan.`nama_bulan`,tahun,tb_dimensi_cabang.`nama_cabang`, "\
            "total_brg_terjual,total_pendapatan "\
            "FROM tb_fakta_trans_barang "\
            "INNER JOIN tb_dimensi_barang USING (id_barang) "\
            "INNER JOIN tb_dimensi_cabang USING (id_cabang) "\
            "INNER JOIN tb_dimensi_bulan USING (id_bulan)"

    ExportCustomer = "SELECT tb_dimensi_customer.`nama_customer`, tb_dimensi_barang.`nama_barang`,tb_dimensi_bulan.`nama_bulan`," \
        "tahun,banyak_brg,total_belanja,tb_dimensi_cabang.`nama_cabang` " \
        "FROM tb_fakta_customer " \
        "INNER JOIN tb_dimensi_customer USING (id_customer) " \
        "INNER JOIN tb_dimensi_barang USING (id_barang) " \
        "INNER JOIN tb_dimensi_bulan USING (id_bulan) " \
        "INNER JOIN tb_dimensi_cabang USING (id_cabang) " \
        "ORDER BY tahun,id_bulan"
    # def generate_tb_bulan(self,dm, dbdimen, query):
    #
    #     with open('bulan.txt', 'r') as f:
    #         val = f.read().splitlines()
    #         for item in val:
    #             x = (tuple([int(i) if i.isdigit() else i for i in item.split(",")]))
    #             dm.execute(query % x)
    #             dbdimen.commit()


    def get_table_value(self,cursor_args, query_args):
        cursor_args.execute(query_args)
        data = cursor_args
        return data


    def tableSourceToDestination(self,cursorArgs, cursorDm, dbConnection, queryArgs, queryInsert):
        cursorArgs.execute(queryArgs)
        datas = cursorArgs

        for data in datas.fetchall():
            print(queryInsert%data)
            cursorDm.execute(queryInsert%data)
            dbConnection.commit()


    def truncateDatabase(self,dm,qtruncate):
        print("masuk")
        truncate = self.get_table_value(dm,qtruncate)
        #print(truncate)
        #dm.execute("SET FOREIGN_KEY_CHECKS=0;")
        print("masuk ke truncate")
        for a in truncate.fetchall():
            dm.execute(a[0])
            print(a[0])


        print("end")


    def truncateallDatabase(self,dm,dconf,connect_dm,connect_config):

        dconf.execute("SET FOREIGN_KEY_CHECKS=0;")
        connect_config.commit()
        truncateconfig = self.get_table_value(dconf,qtruncate_all_config)
        #print(truncateconfig.fetchall())
        for a in truncateconfig.fetchall():
            print(a[0])
            dconf.execute(a[0])
            connect_config.commit()


        dm.execute("SET FOREIGN_KEY_CHECKS=0;")
        connect_dm.commit()
        connect_config.rollback()
        truncatedimen = self.get_table_value(dm, qtruncate_all_dimen)
        for b in truncatedimen.fetchall():
            print(b[0])
            dm.execute(b[0])
            connect_dm.commit()

        dm.execute("SET FOREIGN_KEY_CHECKS=1;")
        connect_dm.commit()
        dconf.execute("SET FOREIGN_KEY_CHECKS=1;")
        connect_config.commit()

        pass



    # def export_penjualan_tahunan(self,dm):
    #
    #
    #
    #     export_tahunan = self.get_table_value(dm,q)
    #
    #     return export_tahunan






    # def main(self,ds,dm,dbDimen):
    #
    #     dm.execute("SET FOREIGN_KEY_CHECKS=0;")
    #     dbDimen.commit()
    #     self.truncateDatabase(dm,self.qTruncateData)
    #     dbDimen.commit()
    #     dm.execute("SET FOREIGN_KEY_CHECKS=1;")
    #     self.tableSourceToDestination(ds, dm, dbDimen, self.qBarang, self.qInsertBarang)
    #     self.tableSourceToDestination(ds, dm, dbDimen, self.qCustomer, self.qInsertCustomer)
    #     self.tableSourceToDestination(ds, dm, dbDimen, self.qPegawai, self.qInsertPegawai)
    #     self.tableSourceToDestination(ds, dm, dbDimen, self.qCabang, self.qInsertCabang)
    #
    #     self.tableSourceToDestination(ds, dm, dbDimen, self.qTransaksi, self.qInsertTransaksi)
    #     self.tableSourceToDestination(dm, dm, dbDimen, self.qDimensiTransBulan, self.qInsertFaktaTransaksiBulan)
    #     self.tableSourceToDestination(dm, dm, dbDimen, self.qDimensiTransTahun, self.qInsertFaktaTransaksiTahun)
    #     self.tableSourceToDestination(dm, dm ,dbDimen, self.qDimensiTransCustomerBulan,self.qInsertFaktaCustomer)
    #     self.tableSourceToDestination(dm, dm, dbDimen, self.qDimensiTransPegawai, self.qInsertFaktaPegawai)
    #     self.tableSourceToDestination(dm, dm, dbDimen, self.qDimensiTransTahunPerCabang,self.qInsertFaktaTransaksiTahunPerCabang)

