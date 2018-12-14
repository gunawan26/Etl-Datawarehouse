import wx
import DatawarehouseGui
import Connector
import wx.dataview
from UpdateConfiguration import UpdateConfig
import WriteExcel


databaseDimensional = "db_dimensional"
databaseSumber = "db_supermarket"


dbSource = Connector.sql_connect(databaseSumber)  # melakukan koneksi ke database source
ds = dbSource.cursor()  # membuat kursor untuk melakukan eksekusi
dbDimen = Connector.sql_connect(databaseDimensional)
dm = dbDimen.cursor()
connection_to_config = Connector.sql_connect('db_config_data_w')
config = connection_to_config.cursor()



#=================================================================================================#
#=========================================query list==============================================#

qSearchdataFakta = 'SELECT tahun,tb_dimensi_bulan.`nama_bulan`,tb_dimensi_cabang.`nama_cabang`,SUM(total_pendapatan)' \
                   'FROM tb_fakta_trans_barang ' \
                   'INNER JOIN tb_dimensi_barang USING(id_barang) ' \
                   'INNER JOIN tb_dimensi_bulan USING (id_bulan) ' \
                   'INNER JOIN tb_dimensi_cabang USING (id_cabang)'



qSearchBulanFakta = 'SELECT tahun,tb_dimensi_bulan.`nama_bulan`,tb_dimensi_cabang.`nama_cabang`,SUM(total_pendapatan) '\
                    'FROM tb_fakta_trans_barang  '\
                    'INNER JOIN tb_dimensi_cabang USING (id_cabang) '\
                    'INNER JOIN tb_dimensi_bulan USING (id_bulan) '\
                    'GROUP BY id_cabang,id_bulan ORDER BY id_cabang,tahun,id_bulan '


qCustomerFakta = 'SELECT tb_dimensi_customer.`nama_customer` AS nama,tb_dimensi_bulan.`nama_bulan` AS bulan,tahun,tb_dimensi_cabang.`nama_cabang`,SUM(total_belanja) '\
                    'FROM tb_fakta_customer '\
                    'INNER JOIN tb_dimensi_customer USING (id_customer) '\
                    'INNER JOIN tb_dimensi_barang USING (id_barang) '\
                    'INNER JOIN tb_dimensi_bulan USING (id_bulan) '\
                    'INNER JOIN tb_dimensi_cabang USING (id_cabang) '\
                    'GROUP BY id_cabang,bulan,id_customer '

qSearchCustomerFakta = 'SELECT tb_dimensi_customer.`nama_customer` AS nama,tb_dimensi_bulan.`nama_bulan` AS bulan,tahun,tb_dimensi_cabang.`nama_cabang`,SUM(total_belanja) '\
                    'FROM tb_fakta_customer '\
                    'INNER JOIN tb_dimensi_customer USING (id_customer) '\
                    'INNER JOIN tb_dimensi_barang USING (id_barang) '\
                    'INNER JOIN tb_dimensi_bulan USING (id_bulan) '\
                    'INNER JOIN tb_dimensi_cabang USING (id_cabang) '
                    #'GROUP BY id_cabang,bulan,id_customer '

qListBulan = 'SELECT nama_bulan FROM tb_dimensi_bulan'

qListTahun = 'SELECT tahun,tb_dimensi_cabang.`nama_cabang`, total_trans FROM tb_fkt_thn_gran_tinggi INNER JOIN tb_dimensi_cabang USING (id_cabang) GROUP BY tahun,id_cabang '

qSearchTahun = 'SELECT tahun,tb_dimensi_cabang.`nama_cabang`, total_trans FROM tb_fkt_thn_gran_tinggi INNER JOIN tb_dimensi_cabang USING (id_cabang)'

qListCabang = 'SELECT tb_dimensi_cabang.nama_cabang FROM tb_dimensi_cabang'

qCariCabang = "SELECT id_cabang FROM tb_dimensi_cabang WHERE nama_cabang = '%s'"

qResultCabangById = "SELECT tahun,tb_dimensi_barang.`nama_barang`, tb_dimensi_cabang.`nama_cabang`, total_brg_terjual, total_pendapatan FROM tb_fakta_tahun "\
                    "INNER JOIN tb_dimensi_barang USING (id_barang) "\
                    "INNER JOIN tb_dimensi_cabang USING (id_cabang) "\
                    "WHERE id_cabang = {0} AND tahun = {1}"

qSearchdataFaktaByid = 'SELECT tahun,tb_dimensi_bulan.`nama_bulan`,tb_dimensi_cabang.`nama_cabang`,tb_dimensi_barang.`nama_barang`,total_brg_terjual,total_pendapatan ' \
                    'FROM tb_fakta_trans_barang ' \
                    'INNER JOIN tb_dimensi_barang USING(id_barang) ' \
                    'INNER JOIN tb_dimensi_bulan USING (id_bulan) ' \
                    'INNER JOIN tb_dimensi_cabang USING (id_cabang) WHERE tahun = {0} '\
                    'AND tb_dimensi_bulan.nama_bulan = "{1}" AND tb_dimensi_cabang.nama_cabang = "{2}"' \



class DetailBulan(DatawarehouseGui.detail_bln_frame):

    def __init__(self,result_final_bln):
        DatawarehouseGui.detail_bln_frame.__init__(self,parent=None)
        print("open panel detail")
        for x,item in enumerate(result_final_bln,start=1):
            new_val = list(item)
            new_val.insert(0, x)
            self.m_dataViewList_penjualan_bln.AppendItem(new_val)
            self.Exit_det_bln.Bind(wx.EVT_BUTTON,self.onExit)

        self.Show()

    def onExit(self,event):
        self.Close(force=False)



#===============================================================================================#
class EventErrorDialog(DatawarehouseGui.error_Dialog_1):

    def __init__(self,parent):
        DatawarehouseGui.error_Dialog_1.__init__(self,parent)
        self.Show()


#================================ Menu option untuk proses ETL =============================#
class MenuOption(DatawarehouseGui.Etl_setting):


    def __init__(self,parent,evt_handler):
        DatawarehouseGui.Etl_setting.__init__(self,parent)
        #self.Show()
        #self.load_detail_info(dm,ds)
        self.setTimer = True
        print("masuk lagi")
        self.Bind(wx.EVT_BUTTON,lambda event:self.on_update(event,evt_handler),self.update_btn)
        self.load_detail_info(dm,ds)
        self.Cancel_btn_etl.Bind(wx.EVT_BUTTON,self.on_exit)
        self.Bind(wx.EVT_BUTTON,self.reload_config,self.m_button9)
        self.Bind(wx.EVT_BUTTON,lambda event:self.truncate_all_db(event,evt_handler),self.m_button_truncate)
        self.on_timer()
        #self.Bind(wx.EVT_UPDATE_UI,lambda event:eventHandler.onreload_daftar_trans_tahun(ev,dm,qListTahun),self.update_btn)
        #self.update_btn.Bind(wx.UPDATE_UI_PROCESS_ALL,self.on_update)

    def reload_config(self,event):

        dbSource.rollback()
        dbDimen.rollback()
        up = UpdateConfig(connection_to_config, config, dbDimen, dm, dbSource, ds)
        val_data = up.update_val(dm, ds)
        counter = 0
        value_information = up.get_last_update(config)
        self.m_last_update_val.SetLabelText(value_information[0])
        self.m_batch_val.SetLabelText(str(value_information[1]))
        self.m_dataViewEtl.DeleteAllItems()
        for key, val in val_data.items():
            counter += 1
            data = [counter, key, val]
            print(data)
            self.m_dataViewEtl.AppendItem(data)
        pass

    def on_timer(self):
        if(self.setTimer):
            self.auto_reload()
            print("masuk")
            wx.CallLater(2000,self.on_timer)

        pass


    def auto_reload(self):

        dbSource.rollback()
        dbDimen.rollback()
        up = UpdateConfig(connection_to_config, config, dbDimen, dm, dbSource, ds)
        val_data = up.update_val(dm, ds)
        counter = 0
        value_information = up.get_last_update(config)
        self.m_last_update_val.SetLabelText(value_information[0])
        self.m_batch_val.SetLabelText(str(value_information[1]))
        self.m_dataViewEtl.DeleteAllItems()
        for key, val in val_data.items():
            counter += 1
            data = [counter, key, val]
            print(data)
            self.m_dataViewEtl.AppendItem(data)


        pass

    def reload_config(self,event):
        dbSource.rollback()
        dbDimen.rollback()
        up = UpdateConfig(connection_to_config, config, dbDimen, dm, dbSource, ds)
        val_data = up.update_val(dm, ds)
        counter = 0
        value_information = up.get_last_update(config)
        self.m_last_update_val.SetLabelText(value_information[0])
        self.m_batch_val.SetLabelText(str(value_information[1]))
        self.m_dataViewEtl.DeleteAllItems()
        for key, val in val_data.items():
            counter += 1
            data = [counter, key, val]
            print(data)
            self.m_dataViewEtl.AppendItem(data)
        pass

    def load_detail_info(self,dm,ds):

        up_conf = UpdateConfig(connection_to_config, config, dbDimen, dm, dbSource, ds)
        val_data  = up_conf.update_val(dm,ds)
        counter = 0
        value_information = up_conf.get_last_update(config)
        self.m_last_update_val.SetLabelText(value_information[0])
        self.m_batch_val.SetLabelText(str(value_information[1]))

        for key,val in val_data.items():
            counter+=1
            data = [counter,key,val]
            print(data)
            self.m_dataViewEtl.AppendItem(data)


    def on_update(self,event,evt_handler):
        id = event.GetId()
        print(id)
        up_conf2 = UpdateConfig(connection_to_config, config, dbDimen, dm, dbSource, ds)
        val = up_conf2.on_update(ds,dm,dbDimen,config)
        if val is True:
            wx.MessageBox('Database sudah Paling Baru', 'Sukses', wx.OK)

        else:
            eventHandler.onreload_daftar_trans_tahun(evt_handler, dm, qListTahun)
            eventHandler.on_reload_tb_fakta_penjualan(evt_handler,dm, qSearchBulanFakta)
            eventHandler.on_reload_daftar_trans_customer(evt_handler,dm,qCustomerFakta)
            list_cabang = (eventHandler.return_list(evt_handler,dm, qListCabang))
            evt_handler.m_choice2.Set(list_cabang)
            self.m_dataViewEtl.DeleteAllItems()
            wx.MessageBox('Database berhasil di Perbaharui', 'Sukses', wx.OK)
        print("update successful")
        self.reload_detail()
        dbDimen.rollback()
        dbSource.rollback()

    def truncate_all_db(self,event,evt_handler):
        up_conf3 = UpdateConfig(connection_to_config, config, dbDimen, dm, dbSource, ds)
        up_conf3.truncate_all()
        dbDimen.rollback()
        dbSource.rollback()
        print("sukses di kosongkan")
        wx.MessageBox('Database berhasil di Kosongkan', 'Sukses', wx.OK)
        self.reload_config(event)
        eventHandler.onreload_daftar_trans_tahun(evt_handler, dm, qListTahun)
        eventHandler.on_reload_tb_fakta_penjualan(evt_handler, dm, qSearchBulanFakta)
        eventHandler.on_reload_daftar_trans_customer(evt_handler, dm, qCustomerFakta)
        list_cabang = (eventHandler.return_list(evt_handler, dm, qListCabang))
        evt_handler.m_choice2.Set(list_cabang)
        pass




    def reload_detail(self):
        up_conf3 = UpdateConfig(connection_to_config, config, dbDimen, dm, dbSource, ds)
        val_data = up_conf3.update_val(dm, ds)
        counter = 0
        value_information = up_conf3.get_last_update(config)
        self.m_last_update_val.SetLabelText(value_information[0])
        self.m_batch_val.SetLabelText(str(value_information[1]))

        for key,val in val_data.items():
            counter+=1
            data = [counter,key,val]
            self.m_dataViewEtl.AppendItem(data)

        pass

    def on_exit(self,event):
        print("close the app")
        self.setTimer = False
        self.Close(force=False)



#================================ Detail Transaksi tahun =============================#
class DetailTransTahun(DatawarehouseGui.MyFrame4):

    def __init__(self,parent,result_final):
        DatawarehouseGui.MyFrame4.__init__(self,parent)
        self.show_transaksi_tahunan(result_final)
        self.Show()
        self.Exit_det.Bind(wx.EVT_BUTTON, self.exit_page)


    def show_transaksi_tahunan(self,result_final):

        for x,item in enumerate(result_final,start=1):
            new_val = list(item)
            new_val.insert(0,x)

            self.m_dataViewList_penjualan_tahunan.AppendItem(new_val)
            print(str(new_val))

        pass


    def reload_transaksi_tahunan(self,result_final):
        self.m_dataViewList_penjualan_tahunan.DeleteAllItems()
        self.show_transaksi_tahunan(result_final)
        pass


    def exit_page(self,event):
        print("close the panel")
        self.Close(force=False)


class eventHandler(DatawarehouseGui.MyFrame1):

    def __init__(self,parent):
        #MyEtl(ds,dm,dbDimen)
        list_bulan = []
        list_cabang = []

        DatawarehouseGui.MyFrame1.__init__(self,parent)

        """Report Untuk Transaksi Bulanan"""
        self.tampil_tb_fakta_penjualan(dm,qSearchBulanFakta)
        bulan = self.list_bulan(dm,qListBulan)
        list_cabang = (self.return_list(dm,qListCabang))
        list_cabang.insert(0,"Semua-Cabang")
        self.m_choice2.Set(list_cabang)

        """Report untuk Transaksi Tahun"""
        self.daftar_trans_tahun(dm,qListTahun)
        self.daftar_transaksi_customer(dm,qCustomerFakta)
        self.Bind(wx.EVT_BUTTON, lambda event: self.onclick_cari_laporan_tahunan(event, dm, qSearchTahun),self.cari_penjualan_tahun)
        self.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, lambda event:self.onClickrow_trans_tahun(event,dm,qCariCabang),self.m_dataViewList_penjualan_tahunan)
        self.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, lambda event: self.onClickrow_trans_bulan(event, dm, qCariCabang),self.m_dataViewList_trans_bulan)
        self.cari_button.Bind(wx.EVT_BUTTON, lambda event:self.search_tb_fakta_penjualan(event,dm,qSearchdataFakta))
        self.Bind(wx.EVT_MENU,self.on_open_etlmenu,self.etl_menu)
        self.Bind(wx.EVT_MENU,lambda event :self.on_exit(event),self.m_menuItem_exit)
        self.Bind(wx.EVT_MENU,lambda event:self.on_save_excel(event),self.m_menuItem3)



        self.Bind(wx.EVT_BUTTON,lambda event:self.search_customer_trans(dm,qSearchCustomerFakta),self.cari_button1_customer)
        self.Bind(wx.EVT_BUTTON,lambda event:self.onreload_daftar_trans_tahun(dm,qListTahun),self.m_bpButton2)
        self.Bind(wx.EVT_BUTTON, lambda event: self.on_reload_tb_fakta_penjualan(dm, qSearchBulanFakta), self.m_bpButton21)
        self.Bind(wx.EVT_BUTTON, lambda event: self.on_reload_daftar_trans_customer(dm, qCustomerFakta),self.m_bpButton22)

        #=====================custom combo box==========================#

        pass


    def on_save_excel(self,event):
        w = WriteExcel.writeExcel()
        w.save_file(dbDimen)

        print("test")
        pass
    def on_exit(self,event):

        dlg = wx.MessageBox("Apakah Anda Yakin Ingin Keluar","info",wx.ICON_INFORMATION | wx.YES_NO)

        if dlg == 2:
            print("masuk")
            self.Close(force=False)

        pass
    def onclick_cari_laporan_tahunan(self,event,cur,query_args):
        query = []
        tahun_start_param = self.m_text_thn_start.GetValue()
        tahun_end_param = self.m_text_thn_end.GetValue()
        error_result = False

        cabang_param = self.m_choice2.GetString(self.m_choice2.GetCurrentSelection())
        print("masuk")
        if tahun_start_param == "" or tahun_end_param == "":
            wx.MessageBox('Input Tahun Tidak Lengkap', 'Warning', wx.OK | wx.ICON_WARNING)
            error_result = True

        else:
            query.append("tahun BETWEEN {0} AND {1} ".format(int(tahun_start_param),int(tahun_end_param)))
            if cabang_param == "" or cabang_param == "":
                wx.MessageBox('Pilih Cabang Yang Ingin Dipilih', 'Warning', wx.OK | wx.ICON_WARNING)
                error_result = True
            else:
                if(cabang_param != 'Semua-Cabang'):
                    query.append(" tb_dimensi_cabang.`nama_cabang` = '{0}'".format(cabang_param))


        if(len(query)>0 and error_result == False):

            query.insert(0,"where ")
            q_final = self.merge_query(query_args, query)
            q_final = q_final+"GROUP BY tahun,id_cabang "
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

    def on_reload_tb_fakta_penjualan(self,cur,query_args):
        self.m_combo_bln.SetValue("")
        self.m_thn_combo.Clear()
        self.m_dataViewList_trans_bulan.DeleteAllItems()
        self.tampil_tb_fakta_penjualan(cur,query_args)



    def search_tb_fakta_penjualan(self,event,cur,query_args):
        query = []
        print("masuk ke button search")

        bulan_args = self.m_combo_bln.GetValue()
        thn_args =self.m_thn_combo.GetValue()

        if bulan_args == "":
            wx.MessageBox('Input Bulan Tidak Lengkap', 'Warning', wx.OK | wx.ICON_WARNING)

        else:
            if thn_args == "":
                wx.MessageBox('Input Tahun Tidak Lengkap', 'Warning', wx.OK | wx.ICON_WARNING)

            else:

                if bulan_args != "":
                    query.append("tb_dimensi_bulan.nama_bulan= '%s'"%bulan_args)

                if thn_args != "":
                    query.append("tahun = %d"% int(thn_args))

                if len(query) > 0:
                    query.insert(0,"where ")
                    q_final = self.merge_query(query_args, query)
                    q_final = q_final+ ' GROUP BY id_cabang,tahun,id_bulan ORDER BY id_cabang'
                    print(q_final)
                    cur.execute(q_final)
                    self.m_dataViewList_trans_bulan.DeleteAllItems()
                    final_val = cur
                    #print(final_val.fetchall()[0][0])
                    for x, item in enumerate(final_val.fetchall(), start=1):
                        print(item[0])
                        if item[0] is not None:
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
        for i,item in enumerate(x.fetchall(),start=1):
            val.append(''.join(item))
        return val


    def daftar_trans_tahun(self,cursor,query_args):
        cursor.execute(query_args)
        val = cursor
        # btn = wx.Button(self.m_dataViewList_penjualan_tahunan, -1, "Pause " + str(1))
        # btn.Bind(wx.EVT_BUTTON, lambda event, temp=1: self.onClickrow_trans_tahun(event))
        for x,item in enumerate(val,start=1):
            print(item)
            list_item = list(item)
            list_item.insert(0,x)
            self.m_dataViewList_penjualan_tahunan.AppendItem(list_item)
        pass


    def onreload_daftar_trans_tahun(self,cursor,query_args):
        cursor.execute(query_args)
        val = cursor
        self.m_text_thn_start.Clear()
        self.m_text_thn_end.Clear()
        self.m_choice2.Clear()
        self.m_dataViewList_penjualan_tahunan.DeleteAllItems()
        for x,item in enumerate(val,start=1):
            list_item = list(item)
            list_item.insert(0,x)
            self.m_dataViewList_penjualan_tahunan.AppendItem(list_item)
        pass


    def daftar_transaksi_customer(self,cursor,query_args):
        cursor.execute(query_args)
        val = cursor
        for x,item in enumerate(val,start=1):
            print(item)

            list_item = list(item)
            list_item.insert(0,x)
            self.m_dataViewList_customer.AppendItem(list_item)

        pass


    def on_reload_daftar_trans_customer(self,cursor,query_args):
        self.m_nama_customer.Clear()
        self.m_combo_bln1.SetValue("")
        self.m_thn_combo1.Clear()
        self.m_dataViewList_customer.DeleteAllItems()
        self.daftar_transaksi_customer(cursor,query_args)
        pass


    def onClickrow_trans_tahun(self,event,cursor,query):

        val = self.m_dataViewList_penjualan_tahunan.GetSelectedRow()
        index_thn = self.m_dataViewList_penjualan_tahunan.GetValue(val,1)
        index_cabang = self.m_dataViewList_penjualan_tahunan.GetValue(val,2)
        cursor.execute(query%index_cabang)
        res = cursor
        param = res.fetchone()
        print(param[0])
        cursor.execute(qResultCabangById.format(param[0],index_thn))
        res2 = cursor
        result_final = res2.fetchall()
        DetailTransTahun(None,result_final)


    def onClickrow_trans_bulan(self,event,cursor,query):

        val = self.m_dataViewList_trans_bulan.GetSelectedRow()
        thn = self.m_dataViewList_trans_bulan.GetValue(val,1)
        bln = self.m_dataViewList_trans_bulan.GetValue(val,2)
        cabang = self.m_dataViewList_trans_bulan.GetValue(val,3)
        print(qSearchdataFaktaByid.format(thn,bln,cabang))
        cursor.execute(qSearchdataFaktaByid.format(thn,bln,cabang))
        val_cur = cursor

        return_val = val_cur.fetchall()

        bln = DetailBulan(return_val)



        pass


    def return_list(self,cur,list_q):
        list_val = []
        cur.execute(list_q)
        val = cur
        for x in  val.fetchall():
            list_val.append(''.join(x))
        return list_val


    def on_open_etlmenu(self,event):
        m_option = MenuOption(None,self)
        m_option.Update()
        m_option.Show()



    def search_customer_trans(self,cur,query_args):
        q = []
        nm_customer = self.m_nama_customer.GetValue()
        bln = self.m_combo_bln1.GetValue()
        thn = self.m_thn_combo1.GetValue()

        if nm_customer != "":
            q.append("tb_dimensi_customer.`nama_customer` = '{0}'".format(nm_customer))
        if bln != "":
            q.append("tb_dimensi_bulan.`nama_bulan` = '{0}'".format(bln))
        if thn != "":
            q.append("tahun = {0}".format(thn))

        if len(q) > 0:
            q.insert(0, "where ")
            q_final = self.merge_query(query_args, q)+ 'GROUP BY tahun,tb_dimensi_bulan.`nama_bulan`,tb_dimensi_cabang.`nama_cabang`'
            print(q_final)
            cur.execute(q_final)
            final_val = cur
            self.m_dataViewList_customer.DeleteAllItems()
            for x, item in enumerate(final_val.fetchall(), start=1):
                print(item[0])
                if item[0] is not None:
                    list_item = list(item)
                    list_item.insert(0, x)
                    print(list_item)
                    self.m_dataViewList_customer.AppendItem(list_item)

        pass


