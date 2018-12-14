import pandas as pd
import xlsxwriter
import Connector
import ExtractDatabase
import datetime


# databaseDimensional = "db_dimensional"
# databaseSumber = "db_supermarket"
#
#
# dbSource = Connector.sql_connect(databaseSumber)  # melakukan koneksi ke database source
# ds = dbSource.cursor()  # membuat kursor untuk melakukan eksekusi
# dbDimen = Connector.sql_connect(databaseDimensional)
# dm = dbDimen.cursor()
# connection_to_config = Connector.sql_connect('db_config_data_w')
# config = connection_to_config.cursor()

date_now = str(datetime.datetime.now().strftime('%Y-%m-%d-%M-%S'))
print(date_now)

class writeExcel:


    def save_file(self,dbDimen):

        my = ExtractDatabase.MyEtl()

        df_pen_thn = pd.read_sql(my.qExportPenjualanTahun,dbDimen)
        df_pen_bulan = pd.read_sql(my.ExportPenjualanBulan,dbDimen)
        df_pen_cust = pd.read_sql(my.ExportCustomer,dbDimen)

        name = "dwh_{0}.xlsx".format(date_now)
        print(name)
        writer = pd.ExcelWriter("dwh_{0}.xlsx".format(date_now), engine='xlsxwriter')

        df_pen_thn.to_excel(writer, sheet_name='Penjualan Tahunan',startrow=1)
        df_pen_bulan.to_excel(writer,sheet_name='Penjualan Bulanan',startrow=1)
        df_pen_cust.to_excel(writer,sheet_name='Transaksi Customer',startrow=1)

        writer.save()

        pass

