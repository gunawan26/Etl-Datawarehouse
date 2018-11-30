import wx
import DatawarehouseGui
import Connector
from ExtractDatabase import MyEtl
import wx.dataview
databaseDimensional = "db_dimensional"
databaseSumber = "db_supermarket"
dbSource = Connector.sql_connect(databaseSumber)  # melakukan koneksi ke database source
ds = dbSource.cursor()  # membuat kursor untuk melakukan eksekusi
dbDimen = Connector.sql_connect(databaseDimensional)
dm = dbDimen.cursor()



#=================================================================================================#
#=========================================query list==============================================#

qSearchdataFakta = 'SELECT tb_dimensi_barang.`nama_barang`,tb_dimensi_bulan.`nama_bulan`,tahun,tb_dimensi_cabang.`nama_cabang`,total_brg_terjual,total_pendapatan ' \
                   'FROM tb_fakta_trans_barang ' \
                   'INNER JOIN tb_dimensi_barang USING(id_barang) ' \
                   'INNER JOIN tb_dimensi_bulan USING (id_bulan) ' \
                   'INNER JOIN tb_dimensi_cabang USING (id_cabang) '

qListBulan = 'SELECT nama_bulan FROM tb_dimensi_bulan'

qListTahun = 'SELECT tahun,tb_dimensi_cabang.`nama_cabang`, total_trans FROM tb_fakta_trans_tahun INNER JOIN tb_dimensi_cabang USING (id_cabang)'

qListCabang = 'SELECT tb_dimensi_cabang.nama_cabang FROM tb_dimensi_cabang'

qCariCabang = "SELECT id_cabang FROM tb_dimensi_cabang WHERE nama_cabang = '%s'"

qResultCabangById = "SELECT tahun,tb_dimensi_barang.`nama_barang`, tb_dimensi_cabang.`nama_cabang`, total_brg_terjual, total_pendapatan FROM tb_fakta_tahun "\
                    "INNER JOIN tb_dimensi_barang USING (id_barang) "\
                    "INNER JOIN tb_dimensi_cabang USING (id_cabang) "\
                    "WHERE id_cabang = %d "


class EventErrorDialog(DatawarehouseGui.error_Dialog_1):

    def __init__(self,parent):
        DatawarehouseGui.error_Dialog_1.__init__(self,parent)
        self.Show()


class DetailTransTahun(DatawarehouseGui.MyFrame4):

    def __init__(self,parent,result_final):
        DatawarehouseGui.MyFrame4.__init__(self,parent)

        for x,item in enumerate(result_final,start=1):
            new_val = list(item)
            new_val.insert(0,x)

            self.m_dataViewList_penjualan_tahunan.AppendItem(new_val)
            self.Exit_det.Bind(wx.EVT_BUTTON,self.exit_page)
            print(str(new_val))


        self.Show()

    def exit_page(self,event):
        print("close the panel")
        self.Close(force=False)


class eventHandler(DatawarehouseGui.MyFrame1):

    def __init__(self,parent):
        MyEtl(ds,dm,dbDimen)
        list_bulan = []
        list_cabang = []

        DatawarehouseGui.MyFrame1.__init__(self,parent)
        self.tampil_tb_fakta_penjualan(dm,qSearchdataFakta)
        bulan = self.list_bulan(dm,qListBulan)
        list_cabang = (self.return_list(dm,qListCabang))
        list_cabang.insert(0,"-")
        self.m_choice2.Set(list_cabang)

        #self.search_tb_fakta_penjualan(dm,"oreo","oktober","cabang 1",qListTahun)
        self.daftar_trans_tahun(dm,qListTahun)
        #self.m_comboBox3 = PromptingComboBox(self,"default value",dummy,style=wx.CB_SORT)
        #self.bSizer51.Add( self.m_comboBox31, 0, wx.ALL, 5 )

        self.Bind(wx.EVT_BUTTON, lambda event: self.onclick_cari_laporan_tahunan(event, dm, qListTahun),
                  self.cari_penjualan_tahun)

        self.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, lambda event:self.onClickrow_trans_tahun(event,dm,qCariCabang))

        self.cari_button.Bind(wx.EVT_BUTTON, lambda event:self.search_tb_fakta_penjualan(event,dm,qSearchdataFakta))

        pass


    def onclick_cari_laporan_tahunan(self,event,cur,query_args):
        query = []
        tahun_start_param = self.m_text_thn_start.GetValue()
        tahun_end_param = self.m_text_thn_end.GetValue()

        cabang_param = self.m_choice2.GetString(self.m_choice2.GetCurrentSelection())
        print("masuk")
        if tahun_start_param == "" or tahun_end_param == " ":
            EventErrorDialog(None)
        else:
            query.append("tahun BETWEEN {0} AND {1} ".format(int(tahun_start_param),int(tahun_end_param)))


        if cabang_param == "" or cabang_param == " ":
            EventErrorDialog(None)

        else:
            if(cabang_param != '-'):
                query.append(" tb_dimensi_cabang.`nama_cabang` = '{0}'".format(cabang_param))

        if(len(query)>0):

            query.insert(0,"where ")
            q_final = self.merge_query(query_args, query)
            print(q_final)
            cur.execute(q_final)
            self.m_dataViewList_penjualan_tahunan.DeleteAllItems()
            final_val = cur

            for x, item in enumerate(final_val.fetchall(), start=1):
                list_item = list(item)
                list_item.insert(0, x)
                print(list_item)
                self.m_dataViewList_penjualan_tahunan.AppendItem(list_item)



    def tampil_tb_fakta_penjualan(self,cur, query_args):
        cur.execute(query_args)
        val = cur
        for i,item in enumerate(val.fetchall(),start=1):
           # btn = wx.Button(self.m_dataViewList_penjualan_tahunan)
            x = list(item)
            x.insert(0,i)
            print(x)
            self.m_dataViewList_trans_bulan.AppendItem(x)




    def search_tb_fakta_penjualan(self,event,cur,query_args):
        query = []
        print("masuk ke button search")

        nama_brg_args = self.m_cariBrg_combo.GetValue()
        bulan_args = self.m_combo_bln.GetValue()
        thn_args =self.m_thn_combo.GetValue()


        if nama_brg_args != "":
            query.append("tb_dimensi_barang.nama_barang = '%s'"%nama_brg_args)

        if bulan_args != "":
            query.append("tb_dimensi_bulan.nama_bulan= '%s'"%bulan_args)

        if thn_args != "":
            query.append("tahun = %d"% int(thn_args))

        if len(query) > 0:
            query.insert(0,"where ")
            q_final = self.merge_query(query_args, query)

            cur.execute(q_final)
            final_val = cur
            print(q_final)
            self.m_dataViewList_trans_bulan.DeleteAllItems()
            for x, item in enumerate(final_val.fetchall(), start=1):
                print(x)
                list_item = list(item)
                list_item.insert(0, x)
                print(list_item)
                self.m_dataViewList_trans_bulan.AppendItem(list_item)


    def merge_query(self,query_first,query_append):
        q = " "
        for x,item in enumerate(query_append):


            if(x > 1 and x < len(query_append)):
                print("in")
                q+=" and "

            q+=item

        return "{0} {1}".format(query_first,q)


    def list_bulan(self,cur,query_args):
        cur.execute(query_args)
        x = cur
        val=[]

        #print(list(x.fetchall()))

        for i,item in enumerate(x.fetchall(),start=1):

            val.append(''.join(item))
            #print(item)

        return val


    def daftar_trans_tahun(self,cursor,query_args):
        cursor.execute(query_args)
        val = cursor
        btn = wx.Button(self.m_dataViewList_penjualan_tahunan, -1, "Pause " + str(1))
        btn.Bind(wx.EVT_BUTTON, lambda event, temp=1: self.onClickrow_trans_tahun(event))
        for x,item in enumerate(val,start=1):


            list_item = list(item)
            list_item.insert(0,x)

            self.m_dataViewList_penjualan_tahunan.AppendItem(list_item)

        pass


    def onClickrow_trans_tahun(self,event,cursor,query):

        val = self.m_dataViewList_penjualan_tahunan.GetSelectedRow()
        index_thn = self.m_dataViewList_penjualan_tahunan.GetValue(val,1)
        index_cabang = self.m_dataViewList_penjualan_tahunan.GetValue(val,2)
        cursor.execute(query%index_cabang)
        res = cursor
        param = res.fetchall()
        cursor.execute(qResultCabangById%param[0])
        res2 = cursor
        result_final = res2.fetchall()
        DetailTransTahun(None,result_final)


    def return_list(self,cur,list_q):
        list_val = []
        cur.execute(list_q)
        val = cur
        for x in  val.fetchall():
            list_val.append(''.join(x))
        return list_val





