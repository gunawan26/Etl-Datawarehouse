# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 970,636 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0|wx.ALWAYS_SHOW_SB )
		self.m_notebook1.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial Unicode MS" ) )
		
		self.m_panel22 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.ALWAYS_SHOW_SB )
		self.m_panel22.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_panel22.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_panel22.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer32 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel22, wx.ID_ANY, u"Filter" ), wx.VERTICAL )
		
		bSizer5112 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer5112.SetMinSize( wx.Size( 300,50 ) ) 
		self.m_staticText2112 = wx.StaticText( sbSizer32.GetStaticBox(), wx.ID_ANY, u"Tahun", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText2112.Wrap( -1 )
		bSizer5112.Add( self.m_staticText2112, 0, wx.ALL, 5 )
		
		self.m_text_thn_start = wx.TextCtrl( sbSizer32.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		bSizer5112.Add( self.m_text_thn_start, 0, wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( sbSizer32.GetStaticBox(), wx.ID_ANY, u"Sampai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer5112.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.m_text_thn_end = wx.TextCtrl( sbSizer32.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		bSizer5112.Add( self.m_text_thn_end, 0, wx.ALL, 5 )
		
		
		sbSizer32.Add( bSizer5112, 0, 0, 5 )
		
		bSizer62 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText221 = wx.StaticText( sbSizer32.GetStaticBox(), wx.ID_ANY, u"Cabang", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText221.Wrap( -1 )
		bSizer62.Add( self.m_staticText221, 0, wx.ALL, 5 )
		
		m_choice2Choices = [ u"-" ]
		self.m_choice2 = wx.Choice( sbSizer32.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 130,-1 ), m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		self.m_choice2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer62.Add( self.m_choice2, 0, wx.ALL, 5 )
		
		
		sbSizer32.Add( bSizer62, 0, 0, 5 )
		
		bSizer621 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cari_penjualan_tahun = wx.Button( sbSizer32.GetStaticBox(), wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		bSizer621.Add( self.cari_penjualan_tahun, 0, wx.ALL, 5 )
		
		self.m_bpButton2 = wx.BitmapButton( sbSizer32.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"res/iconfinder_refresh-01_186390 (1).png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,30 ), wx.BU_AUTODRAW|wx.RAISED_BORDER|wx.SIMPLE_BORDER )
		bSizer621.Add( self.m_bpButton2, 0, wx.ALL, 5 )
		
		
		sbSizer32.Add( bSizer621, 0, 0, 5 )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( sbSizer32.GetStaticBox(), wx.ID_ANY, u"Penjualan Barang" ), wx.VERTICAL )
		
		sbSizer12.SetMinSize( wx.Size( 700,-1 ) ) 
		self.m_dataViewList_penjualan_tahunan = wx.dataview.DataViewListCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewList_penjualan_tahunan.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_dataViewList_penjualan_tahunan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_dataViewList_penjualan_tahunan.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		self.m_dataViewListNo2 = self.m_dataViewList_penjualan_tahunan.AppendTextColumn( u"No" )
		self.m_dataViewListTahun2 = self.m_dataViewList_penjualan_tahunan.AppendTextColumn( u"Tahun" )
		self.m_dataViewListCabang2 = self.m_dataViewList_penjualan_tahunan.AppendTextColumn( u"Cabang" )
		self.m_dataViewListTotPendapatan2 = self.m_dataViewList_penjualan_tahunan.AppendTextColumn( u"Total Pendapatan" )
		sbSizer12.Add( self.m_dataViewList_penjualan_tahunan, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer32.Add( sbSizer12, 1, wx.EXPAND, 5 )
		
		
		bSizer32.Add( sbSizer32, 1, wx.EXPAND, 5 )
		
		
		self.m_panel22.SetSizer( bSizer32 )
		self.m_panel22.Layout()
		bSizer32.Fit( self.m_panel22 )
		self.m_notebook1.AddPage( self.m_panel22, u"Laporan Penjualan Tahunan", False )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.ALWAYS_SHOW_SB )
		self.m_panel2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_panel2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"Filter" ), wx.VERTICAL )
		
		bSizer51 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer51.SetMinSize( wx.Size( 300,50 ) ) 
		self.m_staticText21 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Bulan", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer51.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		m_combo_blnChoices = []
		self.m_combo_bln = wx.ComboBox( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), m_combo_blnChoices, 0 )
		bSizer51.Add( self.m_combo_bln, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer51, 0, 0, 5 )
		
		bSizer511 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer511.SetMinSize( wx.Size( 300,50 ) ) 
		self.m_staticText211 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Tahun", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText211.Wrap( -1 )
		bSizer511.Add( self.m_staticText211, 0, wx.ALL, 5 )
		
		m_thn_comboChoices = []
		self.m_thn_combo = wx.ComboBox( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), m_thn_comboChoices, 0 )
		bSizer511.Add( self.m_thn_combo, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer511, 0, 0, 5 )
		
		bSizer622 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2211 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Cabang", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText2211.Wrap( -1 )
		bSizer622.Add( self.m_staticText2211, 0, wx.ALL, 5 )
		
		m_choice21Choices = [ u"-" ]
		self.m_choice21 = wx.Choice( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice21Choices, 0 )
		self.m_choice21.SetSelection( 0 )
		self.m_choice21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer622.Add( self.m_choice21, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer622, 0, 0, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cari_button = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.cari_button, 0, wx.ALL, 5 )
		
		self.m_bpButton21 = wx.BitmapButton( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"res/iconfinder_refresh-01_186390 (1).png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer6.Add( self.m_bpButton21, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer6, 0, 0, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Penjualan Barang" ), wx.VERTICAL )
		
		sbSizer1.SetMinSize( wx.Size( 700,-1 ) ) 
		self.m_dataViewList_trans_bulan = wx.dataview.DataViewListCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewList_trans_bulan.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_dataViewList_trans_bulan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_dataViewList_trans_bulan.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		self.m_dataViewListNo = self.m_dataViewList_trans_bulan.AppendTextColumn( u"No" )
		self.m_dataViewListTahun = self.m_dataViewList_trans_bulan.AppendTextColumn( u"Tahun" )
		self.m_dataViewListCBulan = self.m_dataViewList_trans_bulan.AppendTextColumn( u"Bulan" )
		self.m_dataViewListCabang = self.m_dataViewList_trans_bulan.AppendTextColumn( u"Cabang" )
		self.m_dataViewListTotPendapatan = self.m_dataViewList_trans_bulan.AppendTextColumn( u"Total Pendapatan" )
		sbSizer1.Add( self.m_dataViewList_trans_bulan, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer3.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"Laporan Penjualan Bulanan", False )
		self.m_panel21_cust = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.ALWAYS_SHOW_SB )
		self.m_panel21_cust.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_panel21_cust.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_panel21_cust.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel21_cust, wx.ID_ANY, u"Filter" ), wx.VERTICAL )
		
		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer52.SetMinSize( wx.Size( 300,50 ) ) 
		self.m_customer_static1 = wx.StaticText( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Nama Customer", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_customer_static1.Wrap( -1 )
		bSizer52.Add( self.m_customer_static1, 0, wx.ALL, 5 )
		
		self.m_nama_customer = wx.TextCtrl( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer52.Add( self.m_nama_customer, 0, wx.ALL, 5 )
		
		
		sbSizer31.Add( bSizer52, 0, wx.EXPAND, 5 )
		
		bSizer512 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer512.SetMinSize( wx.Size( 300,50 ) ) 
		self.m_staticText212 = wx.StaticText( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Bulan", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText212.Wrap( -1 )
		bSizer512.Add( self.m_staticText212, 0, wx.ALL, 5 )
		
		m_combo_bln1Choices = []
		self.m_combo_bln1 = wx.ComboBox( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), m_combo_bln1Choices, 0 )
		bSizer512.Add( self.m_combo_bln1, 0, wx.ALL, 5 )
		
		
		sbSizer31.Add( bSizer512, 0, 0, 5 )
		
		bSizer5111 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer5111.SetMinSize( wx.Size( 300,50 ) ) 
		self.m_staticText2111 = wx.StaticText( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Tahun", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText2111.Wrap( -1 )
		bSizer5111.Add( self.m_staticText2111, 0, wx.ALL, 5 )
		
		m_thn_combo1Choices = []
		self.m_thn_combo1 = wx.ComboBox( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), m_thn_combo1Choices, 0 )
		bSizer5111.Add( self.m_thn_combo1, 0, wx.ALL, 5 )
		
		
		sbSizer31.Add( bSizer5111, 0, 0, 5 )
		
		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cari_button1_customer = wx.Button( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.cari_button1_customer, 0, wx.ALL, 5 )
		
		self.m_bpButton22 = wx.BitmapButton( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"res/iconfinder_refresh-01_186390 (1).png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer61.Add( self.m_bpButton22, 0, wx.ALL, 5 )
		
		
		sbSizer31.Add( bSizer61, 0, 0, 5 )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Pembelian Customer" ), wx.VERTICAL )
		
		sbSizer11.SetMinSize( wx.Size( 700,-1 ) ) 
		self.m_dataViewList_customer = wx.dataview.DataViewListCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		self.m_dataViewList_customer.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_dataViewList_customer.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_dataViewList_customer.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		self.m_dataViewListNo1 = self.m_dataViewList_customer.AppendTextColumn( u"No" )
		self.m_dataViewListNm_customer = self.m_dataViewList_customer.AppendTextColumn( u"Nama Customer" )
		self.m_dataViewListColumn38 = self.m_dataViewList_customer.AppendTextColumn( u"ID customer" )
		self.m_dataViewListCBulan1 = self.m_dataViewList_customer.AppendTextColumn( u"Bulan" )
		self.m_dataViewListTahun1 = self.m_dataViewList_customer.AppendTextColumn( u"Tahun" )
		self.m_dataViewListCabang1 = self.m_dataViewList_customer.AppendTextColumn( u"Cabang" )
		self.m_dataViewListTot_belanja = self.m_dataViewList_customer.AppendTextColumn( u"Total Transaksi" )
		sbSizer11.Add( self.m_dataViewList_customer, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer31.Add( sbSizer11, 1, wx.EXPAND, 5 )
		
		
		bSizer31.Add( sbSizer31, 1, wx.EXPAND, 5 )
		
		
		self.m_panel21_cust.SetSizer( bSizer31 )
		self.m_panel21_cust.Layout()
		bSizer31.Fit( self.m_panel21_cust )
		self.m_notebook1.AddPage( self.m_panel21_cust, u"Laporan Pembelian Customer", True )
		
		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.Option = wx.Menu()
		self.etl_menu = wx.MenuItem( self.Option, wx.ID_ANY, u"proses ETL", wx.EmptyString, wx.ITEM_NORMAL )
		self.Option.AppendItem( self.etl_menu )
		
		self.m_menuItem3 = wx.MenuItem( self.Option, wx.ID_ANY, u"Simpan Excel", wx.EmptyString, wx.ITEM_NORMAL )
		self.Option.AppendItem( self.m_menuItem3 )
		
		self.m_menuItem_exit = wx.MenuItem( self.Option, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.Option.AppendItem( self.m_menuItem_exit )
		
		self.m_menubar1.Append( self.Option, u"Pilihan" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, 0, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.test, id = wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def test( self, event ):
		event.Skip()
	

###########################################################################
## Class Frame_detail_cust
###########################################################################

class Frame_detail_cust ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 894,444 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Detail Penjualan Per Cabang" ), wx.VERTICAL )
		
		sbSizer12.SetMinSize( wx.Size( 700,-1 ) ) 
		self.m_dataViewList_detail_customer = wx.dataview.DataViewListCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewList_detail_customer.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_dataViewList_detail_customer.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_dataViewList_detail_customer.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		self.m_dataViewListNo2 = self.m_dataViewList_detail_customer.AppendTextColumn( u"No" )
		self.m_dataViewListNama_customer = self.m_dataViewList_detail_customer.AppendTextColumn( u"Nama" )
		self.m_dataViewListID_cust = self.m_dataViewList_detail_customer.AppendTextColumn( u"ID Customer" )
		self.m_dataViewListBln = self.m_dataViewList_detail_customer.AppendTextColumn( u"Bulan" )
		self.m_dataViewListTahun = self.m_dataViewList_detail_customer.AppendTextColumn( u"Tahun" )
		self.m_dataViewListColumn41 = self.m_dataViewList_detail_customer.AppendTextColumn( u"Nama Barang" )
		self.m_dataViewListBnykBrg = self.m_dataViewList_detail_customer.AppendTextColumn( u"Banyak barang" )
		self.m_dataViewListTotal_belanja = self.m_dataViewList_detail_customer.AppendTextColumn( u"Total Transaksi" )
		self.m_dataViewListNama_cabang = self.m_dataViewList_detail_customer.AppendTextColumn( u"Nama Cabang" )
		sbSizer12.Add( self.m_dataViewList_detail_customer, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.Exit_det = wx.Button( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.Exit_det, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer24.Add( sbSizer12, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer24 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.test, id = wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def test( self, event ):
		event.Skip()
	

###########################################################################
## Class detail_bln_frame
###########################################################################

class detail_bln_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 747,443 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel8, wx.ID_ANY, u"Detail Penjualan Bulanan" ), wx.VERTICAL )
		
		sbSizer12.SetMinSize( wx.Size( 700,-1 ) ) 
		bSizer39 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		sbSizer12.Add( bSizer39, 0, wx.EXPAND, 5 )
		
		self.m_dataViewList_penjualan_bln = wx.dataview.DataViewListCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewList_penjualan_bln.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_dataViewList_penjualan_bln.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_dataViewList_penjualan_bln.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		self.m_dataViewListNo = self.m_dataViewList_penjualan_bln.AppendTextColumn( u"No" )
		self.m_dataViewListTahun = self.m_dataViewList_penjualan_bln.AppendTextColumn( u"Tahun" )
		self.m_dataViewListBulan = self.m_dataViewList_penjualan_bln.AppendTextColumn( u"Bulan" )
		self.m_dataViewListCabang = self.m_dataViewList_penjualan_bln.AppendTextColumn( u"Cabang" )
		self.m_dataViewListBarang = self.m_dataViewList_penjualan_bln.AppendTextColumn( u"Barang" )
		self.m_dataViewListTerjual = self.m_dataViewList_penjualan_bln.AppendTextColumn( u"Total Terjual" )
		self.m_dataViewListPendapatan = self.m_dataViewList_penjualan_bln.AppendTextColumn( u"Total Pendapatan" )
		sbSizer12.Add( self.m_dataViewList_penjualan_bln, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.Exit_det_bln = wx.Button( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.Exit_det_bln, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer24.Add( sbSizer12, 1, wx.EXPAND, 5 )
		
		
		self.m_panel8.SetSizer( bSizer24 )
		self.m_panel8.Layout()
		bSizer24.Fit( self.m_panel8 )
		bSizer31.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer31 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.test, id = wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def test( self, event ):
		event.Skip()
	

###########################################################################
## Class error_Dialog_1
###########################################################################

class error_Dialog_1 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 340,210 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer22.Add( bSizer23, 1, wx.EXPAND, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer22.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer22 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class load_bar
###########################################################################

class load_bar ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 454,158 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 12,-1 ), wx.TAB_TRAVERSAL )
		bSizer27.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Loading", wx.Point( -1,-1 ), wx.Size( 200,-1 ), 0|wx.TRANSPARENT_WINDOW )
		self.m_staticText16.Wrap( -1 )
		self.m_staticText16.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer27.Add( self.m_staticText16, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer26.Add( bSizer27, 0, 0, 5 )
		
		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 ) 
		self.m_gauge1.SetMinSize( wx.Size( 400,25 ) )
		
		bSizer26.Add( self.m_gauge1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer26 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 669,406 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Detail Penjualan Per Cabang" ), wx.VERTICAL )
		
		sbSizer12.SetMinSize( wx.Size( 700,-1 ) ) 
		self.m_dataViewList_penjualan_tahunan = wx.dataview.DataViewListCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewList_penjualan_tahunan.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_dataViewList_penjualan_tahunan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_dataViewList_penjualan_tahunan.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		self.m_dataViewListNo2 = self.m_dataViewList_penjualan_tahunan.AppendTextColumn( u"No" )
		self.m_dataViewListTahun2 = self.m_dataViewList_penjualan_tahunan.AppendTextColumn( u"Tahun" )
		self.m_dataViewListDetBrg = self.m_dataViewList_penjualan_tahunan.AppendTextColumn( u"Barang" )
		self.m_dataViewListCabang2 = self.m_dataViewList_penjualan_tahunan.AppendTextColumn( u"Cabang" )
		self.m_dataViewListTotTerjual = self.m_dataViewList_penjualan_tahunan.AppendTextColumn( u"Total Terjual" )
		self.m_dataViewListTotPendapatan2 = self.m_dataViewList_penjualan_tahunan.AppendTextColumn( u"Total Pendapatan" )
		sbSizer12.Add( self.m_dataViewList_penjualan_tahunan, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.Exit_det = wx.Button( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.Exit_det, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer24.Add( sbSizer12, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer24 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.test, id = wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def test( self, event ):
		event.Skip()
	

###########################################################################
## Class Etl_setting
###########################################################################

class Etl_setting ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 538,342 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"ETL Process" ), wx.VERTICAL )
		
		self.m_dataViewEtl = wx.dataview.DataViewListCtrl( sbSizer10.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewEtl.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		self.m_dataViewListColumn34 = self.m_dataViewEtl.AppendTextColumn( u"No" )
		self.m_dataViewListColumn35 = self.m_dataViewEtl.AppendTextColumn( u"Nama Tabel" )
		self.m_dataViewListColumn36 = self.m_dataViewEtl.AppendTextColumn( u"Jumlah Row baru" )
		sbSizer10.Add( self.m_dataViewEtl, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_last_update = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Last Update:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_last_update.Wrap( -1 )
		bSizer30.Add( self.m_last_update, 0, wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer30.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.m_last_update_val = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_last_update_val.Wrap( -1 )
		bSizer30.Add( self.m_last_update_val, 0, wx.ALL, 5 )
		
		
		bSizer29.Add( bSizer30, 0, 0, 5 )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_static_text_batch = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Batch", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_static_text_batch.Wrap( -1 )
		bSizer31.Add( self.m_static_text_batch, 0, wx.ALL, 5 )
		
		self.m_staticText251 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText251.Wrap( -1 )
		bSizer31.Add( self.m_staticText251, 0, wx.ALL, 5 )
		
		self.m_batch_val = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_batch_val.Wrap( -1 )
		bSizer31.Add( self.m_batch_val, 0, wx.ALL, 5 )
		
		
		bSizer29.Add( bSizer31, 1, wx.EXPAND, 5 )
		
		
		sbSizer10.Add( bSizer29, 0, 0, 5 )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.update_btn = wx.Button( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Insert", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.update_btn, 0, wx.ALL, 5 )
		
		self.m_button9 = wx.Button( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button9, 0, wx.ALL, 5 )
		
		self.m_button_truncate = wx.Button( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Truncate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button_truncate, 0, wx.ALL, 5 )
		
		self.Cancel_btn_etl = wx.Button( sbSizer10.GetStaticBox(), wx.ID_ANY, u"cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.Cancel_btn_etl, 0, wx.ALL, 5 )
		
		
		sbSizer10.Add( bSizer28, 0, 0, 5 )
		
		
		self.SetSizer( sbSizer10 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

