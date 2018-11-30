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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1059,705 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
		
		self.m_text_thn_start = wx.TextCtrl( sbSizer32.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer5112.Add( self.m_text_thn_start, 0, wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( sbSizer32.GetStaticBox(), wx.ID_ANY, u"Sampai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer5112.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.m_text_thn_end = wx.TextCtrl( sbSizer32.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer5112.Add( self.m_text_thn_end, 0, wx.ALL, 5 )
		
		
		sbSizer32.Add( bSizer5112, 0, 0, 5 )
		
		bSizer62 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText221 = wx.StaticText( sbSizer32.GetStaticBox(), wx.ID_ANY, u"Cabang", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText221.Wrap( -1 )
		bSizer62.Add( self.m_staticText221, 0, wx.ALL, 5 )
		
		m_choice2Choices = []
		self.m_choice2 = wx.Choice( sbSizer32.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		bSizer62.Add( self.m_choice2, 0, wx.ALL, 5 )
		
		
		sbSizer32.Add( bSizer62, 0, 0, 5 )
		
		bSizer621 = wx.BoxSizer( wx.VERTICAL )
		
		self.cari_penjualan_tahun = wx.Button( sbSizer32.GetStaticBox(), wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer621.Add( self.cari_penjualan_tahun, 0, wx.ALL, 5 )
		
		
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
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer5.SetMinSize( wx.Size( 300,50 ) ) 
		self.m_barang_static = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_barang_static.Wrap( -1 )
		bSizer5.Add( self.m_barang_static, 0, wx.ALL, 5 )
		
		m_cariBrg_comboChoices = []
		self.m_cariBrg_combo = wx.ComboBox( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), m_cariBrg_comboChoices, 0 )
		bSizer5.Add( self.m_cariBrg_combo, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		bSizer51 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer51.SetMinSize( wx.Size( 300,50 ) ) 
		self.m_staticText21 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Bulan", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer51.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		m_combo_blnChoices = []
		self.m_combo_bln = wx.ComboBox( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), m_combo_blnChoices, 0 )
		bSizer51.Add( self.m_combo_bln, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer51, 0, 0, 5 )
		
		bSizer511 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer511.SetMinSize( wx.Size( 300,50 ) ) 
		self.m_staticText211 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Tahun", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText211.Wrap( -1 )
		bSizer511.Add( self.m_staticText211, 0, wx.ALL, 5 )
		
		m_thn_comboChoices = []
		self.m_thn_combo = wx.ComboBox( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), m_thn_comboChoices, 0 )
		bSizer511.Add( self.m_thn_combo, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer511, 0, 0, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.cari_button = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.cari_button, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer6, 0, 0, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Penjualan Barang" ), wx.VERTICAL )
		
		sbSizer1.SetMinSize( wx.Size( 700,-1 ) ) 
		self.m_dataViewList_trans_bulan = wx.dataview.DataViewListCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewList_trans_bulan.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_dataViewList_trans_bulan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_dataViewList_trans_bulan.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		self.m_dataViewListNo = self.m_dataViewList_trans_bulan.AppendTextColumn( u"No" )
		self.m_dataViewListNmBrg = self.m_dataViewList_trans_bulan.AppendTextColumn( u"Nama Barang" )
		self.m_dataViewListCBulan = self.m_dataViewList_trans_bulan.AppendTextColumn( u"Bulan" )
		self.m_dataViewListTahun = self.m_dataViewList_trans_bulan.AppendTextColumn( u"Tahun" )
		self.m_dataViewListCabang = self.m_dataViewList_trans_bulan.AppendTextColumn( u"Cabang" )
		self.m_dataViewListTotTerjual = self.m_dataViewList_trans_bulan.AppendTextColumn( u"Total Terjual" )
		self.m_dataViewListTotPendapatan = self.m_dataViewList_trans_bulan.AppendTextColumn( u"Total Pendapatan" )
		sbSizer1.Add( self.m_dataViewList_trans_bulan, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer3.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"Laporan Penjualan Bulanan", True )
		self.m_panel21 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel21, wx.ID_ANY, u"Filter" ), wx.VERTICAL )
		
		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer52.SetMinSize( wx.Size( 300,50 ) ) 
		self.m_staticText22 = wx.StaticText( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText22.Wrap( -1 )
		bSizer52.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		m_comboBox32Choices = []
		self.m_comboBox32 = wx.ComboBox( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), m_comboBox32Choices, 0 )
		bSizer52.Add( self.m_comboBox32, 0, wx.ALL, 5 )
		
		
		sbSizer31.Add( bSizer52, 0, wx.EXPAND, 5 )
		
		bSizer512 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer512.SetMinSize( wx.Size( 300,50 ) ) 
		self.m_staticText212 = wx.StaticText( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Bulan", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText212.Wrap( -1 )
		bSizer512.Add( self.m_staticText212, 0, wx.ALL, 5 )
		
		m_comboBox312Choices = []
		self.m_comboBox312 = wx.ComboBox( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), m_comboBox312Choices, 0 )
		bSizer512.Add( self.m_comboBox312, 0, wx.ALL, 5 )
		
		
		sbSizer31.Add( bSizer512, 0, 0, 5 )
		
		bSizer5111 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer5111.SetMinSize( wx.Size( 300,50 ) ) 
		self.m_staticText2111 = wx.StaticText( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Tahun", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText2111.Wrap( -1 )
		bSizer5111.Add( self.m_staticText2111, 0, wx.ALL, 5 )
		
		m_comboBox3111Choices = []
		self.m_comboBox3111 = wx.ComboBox( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), m_comboBox3111Choices, 0 )
		bSizer5111.Add( self.m_comboBox3111, 0, wx.ALL, 5 )
		
		
		sbSizer31.Add( bSizer5111, 0, 0, 5 )
		
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		self.cari_button1 = wx.Button( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.cari_button1, 0, wx.ALL, 5 )
		
		
		sbSizer31.Add( bSizer61, 0, 0, 5 )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Penjualan Barang" ), wx.VERTICAL )
		
		sbSizer11.SetMinSize( wx.Size( 500,-1 ) ) 
		self.m_dataViewListCtrl21 = wx.dataview.DataViewListCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListCtrl21.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_dataViewListCtrl21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_dataViewListCtrl21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		self.m_dataViewListNo1 = self.m_dataViewListCtrl21.AppendTextColumn( u"No" )
		self.m_dataViewListNmBrg1 = self.m_dataViewListCtrl21.AppendTextColumn( u"Nama Barang" )
		self.m_dataViewListCBulan1 = self.m_dataViewListCtrl21.AppendTextColumn( u"Bulan" )
		self.m_dataViewListTahun1 = self.m_dataViewListCtrl21.AppendTextColumn( u"Tahun" )
		self.m_dataViewListCabang1 = self.m_dataViewListCtrl21.AppendTextColumn( u"Cabang" )
		self.m_dataViewListTotTerjual1 = self.m_dataViewListCtrl21.AppendTextColumn( u"Total Terjual" )
		self.m_dataViewListTotPendapatan1 = self.m_dataViewListCtrl21.AppendTextColumn( u"Total Pendapatan" )
		sbSizer11.Add( self.m_dataViewListCtrl21, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer31.Add( sbSizer11, 1, wx.EXPAND, 5 )
		
		
		bSizer31.Add( sbSizer31, 1, wx.EXPAND, 5 )
		
		
		self.m_panel21.SetSizer( bSizer31 )
		self.m_panel21.Layout()
		bSizer31.Fit( self.m_panel21 )
		self.m_notebook1.AddPage( self.m_panel21, u"Laporan Pegawai", False )
		self.m_panel211 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer311 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer311 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel211, wx.ID_ANY, u"Filter" ), wx.VERTICAL )
		
		bSizer521 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer521.SetMinSize( wx.Size( 300,50 ) ) 
		self.m_staticText222 = wx.StaticText( sbSizer311.GetStaticBox(), wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText222.Wrap( -1 )
		bSizer521.Add( self.m_staticText222, 0, wx.ALL, 5 )
		
		m_comboBox321Choices = []
		self.m_comboBox321 = wx.ComboBox( sbSizer311.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), m_comboBox321Choices, 0 )
		bSizer521.Add( self.m_comboBox321, 0, wx.ALL, 5 )
		
		
		sbSizer311.Add( bSizer521, 0, wx.EXPAND, 5 )
		
		bSizer5121 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer5121.SetMinSize( wx.Size( 300,50 ) ) 
		self.m_staticText2121 = wx.StaticText( sbSizer311.GetStaticBox(), wx.ID_ANY, u"Bulan", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText2121.Wrap( -1 )
		bSizer5121.Add( self.m_staticText2121, 0, wx.ALL, 5 )
		
		m_comboBox3121Choices = []
		self.m_comboBox3121 = wx.ComboBox( sbSizer311.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), m_comboBox3121Choices, 0 )
		bSizer5121.Add( self.m_comboBox3121, 0, wx.ALL, 5 )
		
		
		sbSizer311.Add( bSizer5121, 0, 0, 5 )
		
		bSizer51111 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer51111.SetMinSize( wx.Size( 300,50 ) ) 
		self.m_staticText21111 = wx.StaticText( sbSizer311.GetStaticBox(), wx.ID_ANY, u"Tahun", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText21111.Wrap( -1 )
		bSizer51111.Add( self.m_staticText21111, 0, wx.ALL, 5 )
		
		m_comboBox31111Choices = []
		self.m_comboBox31111 = wx.ComboBox( sbSizer311.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), m_comboBox31111Choices, 0 )
		bSizer51111.Add( self.m_comboBox31111, 0, wx.ALL, 5 )
		
		
		sbSizer311.Add( bSizer51111, 0, 0, 5 )
		
		bSizer611 = wx.BoxSizer( wx.VERTICAL )
		
		self.cari_button11 = wx.Button( sbSizer311.GetStaticBox(), wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer611.Add( self.cari_button11, 0, wx.ALL, 5 )
		
		
		sbSizer311.Add( bSizer611, 0, 0, 5 )
		
		sbSizer111 = wx.StaticBoxSizer( wx.StaticBox( sbSizer311.GetStaticBox(), wx.ID_ANY, u"Penjualan Barang" ), wx.VERTICAL )
		
		sbSizer111.SetMinSize( wx.Size( 500,-1 ) ) 
		self.m_dataViewListCtrl211 = wx.dataview.DataViewListCtrl( sbSizer111.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListCtrl211.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_dataViewListCtrl211.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_dataViewListCtrl211.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		self.m_dataViewListNo11 = self.m_dataViewListCtrl211.AppendTextColumn( u"No" )
		self.m_dataViewListNmBrg11 = self.m_dataViewListCtrl211.AppendTextColumn( u"Nama Barang" )
		self.m_dataViewListCBulan11 = self.m_dataViewListCtrl211.AppendTextColumn( u"Bulan" )
		self.m_dataViewListTahun11 = self.m_dataViewListCtrl211.AppendTextColumn( u"Tahun" )
		self.m_dataViewListCabang11 = self.m_dataViewListCtrl211.AppendTextColumn( u"Cabang" )
		self.m_dataViewListTotTerjual11 = self.m_dataViewListCtrl211.AppendTextColumn( u"Total Terjual" )
		self.m_dataViewListTotPendapatan11 = self.m_dataViewListCtrl211.AppendTextColumn( u"Total Pendapatan" )
		sbSizer111.Add( self.m_dataViewListCtrl211, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer311.Add( sbSizer111, 1, wx.EXPAND, 5 )
		
		
		bSizer311.Add( sbSizer311, 1, wx.EXPAND, 5 )
		
		
		self.m_panel211.SetSizer( bSizer311 )
		self.m_panel211.Layout()
		bSizer311.Fit( self.m_panel211 )
		self.m_notebook1.AddPage( self.m_panel211, u"Belanja Customer", False )
		
		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.Exit = wx.Menu()
		self.m_menubar1.Append( self.Exit, u"Exit" ) 
		
		self.Option = wx.Menu()
		self.m_config_menu = wx.MenuItem( self.Option, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.Option.AppendItem( self.m_config_menu )
		
		self.m_about_menu = wx.MenuItem( self.Option, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.Option.AppendItem( self.m_about_menu )
		
		self.m_menubar1.Append( self.Option, u"Option" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		
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
	

