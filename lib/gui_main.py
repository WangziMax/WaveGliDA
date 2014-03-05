# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2013)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.combo

###########################################################################
## Class Frame_MAIN
###########################################################################

class Frame_MAIN ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Wave Glider Data Analysis", pos = wx.DefaultPosition, size = wx.Size( 900,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 900,600 ), wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		Panel_MAIN1 = wx.BoxSizer( wx.VERTICAL )
		
		self.Panel_MAIN = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Panel_MAIN.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.Panel_MAIN.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.Panel_MAIN.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		Sizer_MAIN2 = wx.BoxSizer( wx.VERTICAL )
		
		Sizer_NoteBook = wx.BoxSizer( wx.HORIZONTAL )
		
		self.MAIN = wx.Notebook( self.Panel_MAIN, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH|wx.NB_NOPAGETHEME|wx.NB_TOP )
		self.MAIN.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.MAIN.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.MAIN.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		self.Panel_HelpInfo = wx.Panel( self.MAIN, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Panel_HelpInfo.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.Panel_HelpInfo.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		bSizer98 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel10 = wx.Panel( self.Panel_HelpInfo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel10.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer37 = wx.BoxSizer( wx.VERTICAL )
		
		LB_HELPChoices = []
		self.LB_HELP = wx.ListBox( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, LB_HELPChoices, 0 )
		self.LB_HELP.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer37.Add( self.LB_HELP, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel10.SetSizer( bSizer37 )
		self.m_panel10.Layout()
		bSizer37.Fit( self.m_panel10 )
		bSizer98.Add( self.m_panel10, 1, wx.EXPAND, 5 )
		
		self.m_panel11 = wx.Panel( self.Panel_HelpInfo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel11.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial" ) )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		self.TXT_HELP = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		self.TXT_HELP.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer39.Add( self.TXT_HELP, 2, wx.EXPAND, 5 )
		
		
		self.m_panel11.SetSizer( bSizer39 )
		self.m_panel11.Layout()
		bSizer39.Fit( self.m_panel11 )
		bSizer98.Add( self.m_panel11, 2, wx.EXPAND |wx.ALL, 5 )
		
		
		self.Panel_HelpInfo.SetSizer( bSizer98 )
		self.Panel_HelpInfo.Layout()
		bSizer98.Fit( self.Panel_HelpInfo )
		self.MAIN.AddPage( self.Panel_HelpInfo, u"Help and Info", False )
		self.NBPanel_FileSelection = wx.Panel( self.MAIN, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.NBPanel_FileSelection.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		Sizer_FileSelection = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.DirSelector = wx.DirPickerCtrl( self.NBPanel_FileSelection, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DIR_MUST_EXIST )
		self.DirSelector.SetToolTipString( u"load multiple raw files" )
		
		bSizer32.Add( self.DirSelector, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.BTN_LoadFile = wx.FilePickerCtrl( self.NBPanel_FileSelection, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*wg.csv", wx.DefaultPosition, wx.DefaultSize, wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		self.BTN_LoadFile.SetToolTipString( u"Load a previously saved file (*wg.csv)" )
		
		bSizer32.Add( self.BTN_LoadFile, 1, wx.ALL, 5 )
		
		
		bSizer30.Add( bSizer32, 0, wx.EXPAND, 5 )
		
		bSizer66 = wx.BoxSizer( wx.VERTICAL )
		
		self.CB_SelectAll = wx.CheckBox( self.NBPanel_FileSelection, wx.ID_ANY, u"Select All", wx.DefaultPosition, wx.DefaultSize, wx.CHK_3STATE|wx.CHK_ALLOW_3RD_STATE_FOR_USER )
		self.CB_SelectAll.Enable( False )
		
		bSizer66.Add( self.CB_SelectAll, 0, wx.LEFT|wx.TOP, 8 )
		
		
		bSizer30.Add( bSizer66, 0, wx.EXPAND, 5 )
		
		Sizer_SelectBox = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel9 = wx.Panel( self.NBPanel_FileSelection, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		LB_FilesChoices = []
		self.LB_Files = wx.ListBox( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, LB_FilesChoices, wx.LB_MULTIPLE )
		self.LB_Files.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer31.Add( self.LB_Files, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.Button_ReadFiles = wx.Button( self.m_panel9, wx.ID_ANY, u"Read Selected Files", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Button_ReadFiles.Enable( False )
		
		bSizer31.Add( self.Button_ReadFiles, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.Files_Progress = wx.Gauge( self.m_panel9, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.Files_Progress.SetValue( 0 ) 
		bSizer31.Add( self.Files_Progress, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel9.SetSizer( bSizer31 )
		self.m_panel9.Layout()
		bSizer31.Fit( self.m_panel9 )
		Sizer_SelectBox.Add( self.m_panel9, 1, wx.EXPAND, 5 )
		
		self.m_panel7 = wx.Panel( self.NBPanel_FileSelection, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer341 = wx.BoxSizer( wx.VERTICAL )
		
		self.TC_FileStatus = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_RICH )
		self.TC_FileStatus.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer341.Add( self.TC_FileStatus, 5, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel7.SetSizer( bSizer341 )
		self.m_panel7.Layout()
		bSizer341.Fit( self.m_panel7 )
		Sizer_SelectBox.Add( self.m_panel7, 2, wx.EXPAND, 5 )
		
		
		bSizer30.Add( Sizer_SelectBox, 2, wx.EXPAND, 5 )
		
		
		Sizer_FileSelection.Add( bSizer30, 1, wx.EXPAND, 5 )
		
		
		self.NBPanel_FileSelection.SetSizer( Sizer_FileSelection )
		self.NBPanel_FileSelection.Layout()
		Sizer_FileSelection.Fit( self.NBPanel_FileSelection )
		self.MAIN.AddPage( self.NBPanel_FileSelection, u"File Selection", True )
		self.NBPanel_Data = wx.Panel( self.MAIN, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.BTN_SaveFile = wx.FilePickerCtrl( self.NBPanel_Data, wx.ID_ANY, u"test", u"Enter a filename *wg.csv", u"Comma Seperated Values (*.csv) | *.csv ; MATLAB (*.mat) | *.mat", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OVERWRITE_PROMPT|wx.FLP_SAVE )
		bSizer34.Add( self.BTN_SaveFile, 1, wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.NBPanel_Data, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer34.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.BTN_calcCO2 = wx.Button( self.NBPanel_Data, wx.ID_ANY, u"Calculate pCO2 / fCO2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BTN_calcCO2.Enable( False )
		
		bSizer34.Add( self.BTN_calcCO2, 1, wx.ALL, 5 )
		
		
		bSizer33.Add( bSizer34, 0, wx.EXPAND, 5 )
		
		self.GridData = wx.grid.Grid( self.NBPanel_Data, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.GridData.CreateGrid( 0, 0 )
		self.GridData.EnableEditing( True )
		self.GridData.EnableGridLines( True )
		self.GridData.EnableDragGridSize( False )
		self.GridData.SetMargins( 0, 0 )
		
		# Columns
		self.GridData.EnableDragColMove( True )
		self.GridData.EnableDragColSize( True )
		self.GridData.SetColLabelSize( 30 )
		self.GridData.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.GridData.EnableDragRowSize( True )
		self.GridData.SetRowLabelSize( 80 )
		self.GridData.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.GridData.SetLabelFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		# Cell Defaults
		self.GridData.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.GridData.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer33.Add( self.GridData, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.NBPanel_Data.SetSizer( bSizer33 )
		self.NBPanel_Data.Layout()
		bSizer33.Fit( self.NBPanel_Data )
		self.MAIN.AddPage( self.NBPanel_Data, u"Data", False )
		self.NBPanel_TimeSeries = wx.Panel( self.MAIN, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Sizer_XYPlots = wx.BoxSizer( wx.VERTICAL )
		
		bSizer95 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer36 = wx.BoxSizer( wx.VERTICAL )
		
		Size_MP_Xax_prop = wx.StaticBoxSizer( wx.StaticBox( self.NBPanel_TimeSeries, wx.ID_ANY, u"X - Axis" ), wx.VERTICAL )
		
		x_varChoices = []
		self.x_var = wx.Choice( self.NBPanel_TimeSeries, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, x_varChoices, 0 )
		self.x_var.SetSelection( 0 )
		Size_MP_Xax_prop.Add( self.x_var, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.x_label = wx.TextCtrl( self.NBPanel_TimeSeries, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.x_label.SetToolTipString( u"becomes the x-axis label (can also use latex math)" )
		
		Size_MP_Xax_prop.Add( self.x_label, 0, wx.ALL|wx.EXPAND, 5 )
		
		Sizer_XYProps_X21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText19 = wx.StaticText( self.NBPanel_TimeSeries, wx.ID_ANY, u"MIN", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText19.Wrap( -1 )
		Sizer_XYProps_X21.Add( self.m_staticText19, 1, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self.NBPanel_TimeSeries, wx.ID_ANY, u"MAX", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText20.Wrap( -1 )
		Sizer_XYProps_X21.Add( self.m_staticText20, 1, wx.ALL, 5 )
		
		
		Size_MP_Xax_prop.Add( Sizer_XYProps_X21, 0, wx.EXPAND, 5 )
		
		Sizer_XYProps_X2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.x_minslide = wx.Slider( self.NBPanel_TimeSeries, wx.ID_ANY, 0, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_BOTH|wx.SL_HORIZONTAL )
		self.x_minslide.Enable( False )
		
		Sizer_XYProps_X2.Add( self.x_minslide, 1, wx.ALL, 5 )
		
		self.x_maxslide = wx.Slider( self.NBPanel_TimeSeries, wx.ID_ANY, 100, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_BOTH|wx.SL_HORIZONTAL )
		self.x_maxslide.Enable( False )
		
		Sizer_XYProps_X2.Add( self.x_maxslide, 1, wx.ALL, 5 )
		
		
		Size_MP_Xax_prop.Add( Sizer_XYProps_X2, 0, wx.EXPAND, 5 )
		
		bSizer681 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.x_min = wx.StaticText( self.NBPanel_TimeSeries, wx.ID_ANY, u"min data", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.x_min.Wrap( -1 )
		self.x_min.Enable( False )
		
		bSizer681.Add( self.x_min, 1, wx.EXPAND, 5 )
		
		self.x_max = wx.StaticText( self.NBPanel_TimeSeries, wx.ID_ANY, u"max data", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.x_max.Wrap( -1 )
		self.x_max.Enable( False )
		
		bSizer681.Add( self.x_max, 1, wx.BOTTOM, 5 )
		
		
		Size_MP_Xax_prop.Add( bSizer681, 1, wx.EXPAND, 5 )
		
		
		bSizer36.Add( Size_MP_Xax_prop, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer43 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.NBPanel_TimeSeries, wx.ID_ANY, u"Figure Properties" ), wx.VERTICAL )
		
		bSizer44 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText23 = wx.StaticText( self.NBPanel_TimeSeries, wx.ID_ANY, u"Title: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer44.Add( self.m_staticText23, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.xy_title = wx.TextCtrl( self.NBPanel_TimeSeries, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.xy_title, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		sbSizer4.Add( bSizer44, 0, wx.EXPAND, 5 )
		
		
		bSizer43.Add( sbSizer4, 1, wx.ALL|wx.EXPAND|wx.TOP, 5 )
		
		
		bSizer36.Add( bSizer43, 1, wx.EXPAND, 5 )
		
		
		bSizer95.Add( bSizer36, 4, wx.EXPAND, 5 )
		
		Size_MP_Y1ax_prop1 = wx.StaticBoxSizer( wx.StaticBox( self.NBPanel_TimeSeries, wx.ID_ANY, u"Y1 - Axis" ), wx.VERTICAL )
		
		y1_varChoices = []
		self.y1_var = wx.Choice( self.NBPanel_TimeSeries, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, y1_varChoices, 0 )
		self.y1_var.SetSelection( 0 )
		self.y1_var.Enable( False )
		
		Size_MP_Y1ax_prop1.Add( self.y1_var, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.y1_label = wx.TextCtrl( self.NBPanel_TimeSeries, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.y1_label.Enable( False )
		self.y1_label.SetToolTipString( u"becomes the y1-axis label (can also use latex math)" )
		
		Size_MP_Y1ax_prop1.Add( self.y1_label, 0, wx.ALL|wx.EXPAND, 5 )
		
		Sizer_XYProps_X211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText191 = wx.StaticText( self.NBPanel_TimeSeries, wx.ID_ANY, u"MIN", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText191.Wrap( -1 )
		Sizer_XYProps_X211.Add( self.m_staticText191, 1, wx.ALL, 5 )
		
		self.m_staticText201 = wx.StaticText( self.NBPanel_TimeSeries, wx.ID_ANY, u"MAX", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText201.Wrap( -1 )
		Sizer_XYProps_X211.Add( self.m_staticText201, 1, wx.ALL, 5 )
		
		
		Size_MP_Y1ax_prop1.Add( Sizer_XYProps_X211, 0, wx.EXPAND, 5 )
		
		Sizer_XYProps_X22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.y1_min = wx.TextCtrl( self.NBPanel_TimeSeries, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.y1_min.Enable( False )
		
		Sizer_XYProps_X22.Add( self.y1_min, 1, wx.ALL, 5 )
		
		self.y1_max = wx.TextCtrl( self.NBPanel_TimeSeries, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.y1_max.Enable( False )
		
		Sizer_XYProps_X22.Add( self.y1_max, 1, wx.ALL, 5 )
		
		
		Size_MP_Y1ax_prop1.Add( Sizer_XYProps_X22, 0, wx.EXPAND, 5 )
		
		bSizer59 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer60 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer612 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText351 = wx.StaticText( self.NBPanel_TimeSeries, wx.ID_ANY, u"Line ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText351.Wrap( -1 )
		bSizer612.Add( self.m_staticText351, 0, wx.ALIGN_CENTER|wx.TOP, 5 )
		
		self.y1_color = wx.ColourPickerCtrl( self.NBPanel_TimeSeries, wx.ID_ANY, wx.Colour( 0, 22, 179 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.y1_color.Enable( False )
		
		bSizer612.Add( self.y1_color, 1, wx.ALL|wx.EXPAND, 5 )
		
		y1_linestyleChoices = [ u"-", u"--", u"-.", u":", u"None" ]
		self.y1_linestyle = wx.Choice( self.NBPanel_TimeSeries, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, y1_linestyleChoices, 0 )
		self.y1_linestyle.SetSelection( 0 )
		self.y1_linestyle.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.y1_linestyle.Enable( False )
		
		bSizer612.Add( self.y1_linestyle, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.y1_linewidth = wx.SpinCtrl( self.NBPanel_TimeSeries, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 2 )
		self.y1_linewidth.Enable( False )
		
		bSizer612.Add( self.y1_linewidth, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer60.Add( bSizer612, 1, wx.EXPAND, 5 )
		
		bSizer611 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3511 = wx.StaticText( self.NBPanel_TimeSeries, wx.ID_ANY, u"Markers", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3511.Wrap( -1 )
		bSizer611.Add( self.m_staticText3511, 0, wx.ALIGN_CENTER|wx.TOP, 5 )
		
		self.y1_markerfacecolor = wx.ColourPickerCtrl( self.NBPanel_TimeSeries, wx.ID_ANY, wx.Colour( 0, 22, 179 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.y1_markerfacecolor.Enable( False )
		
		bSizer611.Add( self.y1_markerfacecolor, 1, wx.ALL|wx.EXPAND, 5 )
		
		y1_markerChoices = [ u"None", u"o", u".", u",", u"v", u"^", u"<", u">", u"s", u"*", u"+", u"x" ]
		self.y1_marker = wx.Choice( self.NBPanel_TimeSeries, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, y1_markerChoices, 0 )
		self.y1_marker.SetSelection( 0 )
		self.y1_marker.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.y1_marker.Enable( False )
		
		bSizer611.Add( self.y1_marker, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.y1_markersize = wx.SpinCtrl( self.NBPanel_TimeSeries, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 5 )
		self.y1_markersize.Enable( False )
		
		bSizer611.Add( self.y1_markersize, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer60.Add( bSizer611, 1, wx.EXPAND, 5 )
		
		
		bSizer59.Add( bSizer60, 0, wx.EXPAND, 5 )
		
		
		bSizer59.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText202 = wx.StaticText( self.NBPanel_TimeSeries, wx.ID_ANY, u"Choose Licor Mode", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText202.Wrap( -1 )
		bSizer59.Add( self.m_staticText202, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer361 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer371 = wx.BoxSizer( wx.VERTICAL )
		
		self.y1_CHequ = wx.CheckBox( self.NBPanel_TimeSeries, wx.ID_ANY, u"EQU", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.y1_CHequ.SetValue(True) 
		self.y1_CHequ.Enable( False )
		
		bSizer371.Add( self.y1_CHequ, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.y1_CHzero = wx.CheckBox( self.NBPanel_TimeSeries, wx.ID_ANY, u"ZERO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.y1_CHzero.Enable( False )
		
		bSizer371.Add( self.y1_CHzero, 0, wx.ALL, 5 )
		
		
		bSizer361.Add( bSizer371, 1, wx.EXPAND, 5 )
		
		bSizer38 = wx.BoxSizer( wx.VERTICAL )
		
		self.y1_CHatm = wx.CheckBox( self.NBPanel_TimeSeries, wx.ID_ANY, u"ATM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.y1_CHatm.Enable( False )
		
		bSizer38.Add( self.y1_CHatm, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.y1_CHspan = wx.CheckBox( self.NBPanel_TimeSeries, wx.ID_ANY, u"SPAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.y1_CHspan.Enable( False )
		
		bSizer38.Add( self.y1_CHspan, 0, wx.ALL|wx.LEFT, 5 )
		
		
		bSizer361.Add( bSizer38, 1, wx.EXPAND|wx.LEFT, 5 )
		
		
		bSizer59.Add( bSizer361, 0, wx.EXPAND|wx.LEFT, 20 )
		
		
		Size_MP_Y1ax_prop1.Add( bSizer59, 4, wx.EXPAND, 5 )
		
		
		bSizer95.Add( Size_MP_Y1ax_prop1, 4, wx.ALL|wx.EXPAND, 5 )
		
		Size_MP_Y2ax_prop = wx.StaticBoxSizer( wx.StaticBox( self.NBPanel_TimeSeries, wx.ID_ANY, u"Y2 - Axis" ), wx.VERTICAL )
		
		y2_varChoices = []
		self.y2_var = wx.Choice( self.NBPanel_TimeSeries, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, y2_varChoices, 0 )
		self.y2_var.SetSelection( 0 )
		self.y2_var.Enable( False )
		
		Size_MP_Y2ax_prop.Add( self.y2_var, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.y2_label = wx.TextCtrl( self.NBPanel_TimeSeries, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.y2_label.Enable( False )
		self.y2_label.SetToolTipString( u"becomes the y2-axis label (can also use latex math)" )
		
		Size_MP_Y2ax_prop.Add( self.y2_label, 0, wx.ALL|wx.EXPAND, 5 )
		
		Sizer_XYProps_X2111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1911 = wx.StaticText( self.NBPanel_TimeSeries, wx.ID_ANY, u"MIN", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText1911.Wrap( -1 )
		Sizer_XYProps_X2111.Add( self.m_staticText1911, 1, wx.ALL, 5 )
		
		self.m_staticText2011 = wx.StaticText( self.NBPanel_TimeSeries, wx.ID_ANY, u"MAX", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText2011.Wrap( -1 )
		Sizer_XYProps_X2111.Add( self.m_staticText2011, 1, wx.ALL, 5 )
		
		
		Size_MP_Y2ax_prop.Add( Sizer_XYProps_X2111, 0, wx.EXPAND, 5 )
		
		Sizer_XYProps_X221 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.y2_min = wx.TextCtrl( self.NBPanel_TimeSeries, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.y2_min.Enable( False )
		
		Sizer_XYProps_X221.Add( self.y2_min, 1, wx.ALL, 5 )
		
		self.y2_max = wx.TextCtrl( self.NBPanel_TimeSeries, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.y2_max.Enable( False )
		
		Sizer_XYProps_X221.Add( self.y2_max, 1, wx.ALL, 5 )
		
		
		Size_MP_Y2ax_prop.Add( Sizer_XYProps_X221, 0, wx.EXPAND, 5 )
		
		bSizer601 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer67 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer6121 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText43 = wx.StaticText( self.NBPanel_TimeSeries, wx.ID_ANY, u"Line", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		bSizer6121.Add( self.m_staticText43, 0, wx.ALIGN_CENTER|wx.TOP, 5 )
		
		self.y2_color = wx.ColourPickerCtrl( self.NBPanel_TimeSeries, wx.ID_ANY, wx.Colour( 62, 148, 20 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.y2_color.Enable( False )
		
		bSizer6121.Add( self.y2_color, 1, wx.ALL|wx.EXPAND, 5 )
		
		y2_linestyleChoices = [ u"-", u"--", u"-.", u":", u"None" ]
		self.y2_linestyle = wx.Choice( self.NBPanel_TimeSeries, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, y2_linestyleChoices, 0 )
		self.y2_linestyle.SetSelection( 0 )
		self.y2_linestyle.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.y2_linestyle.Enable( False )
		
		bSizer6121.Add( self.y2_linestyle, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.y2_linewidth = wx.SpinCtrl( self.NBPanel_TimeSeries, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 2 )
		self.y2_linewidth.Enable( False )
		
		bSizer6121.Add( self.y2_linewidth, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer67.Add( bSizer6121, 1, wx.EXPAND, 5 )
		
		bSizer6111 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText44 = wx.StaticText( self.NBPanel_TimeSeries, wx.ID_ANY, u"Markers", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		bSizer6111.Add( self.m_staticText44, 0, wx.ALIGN_CENTER|wx.TOP, 5 )
		
		self.y2_markerfacecolor = wx.ColourPickerCtrl( self.NBPanel_TimeSeries, wx.ID_ANY, wx.Colour( 62, 148, 20 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.y2_markerfacecolor.Enable( False )
		
		bSizer6111.Add( self.y2_markerfacecolor, 1, wx.ALL|wx.EXPAND, 5 )
		
		y2_markerChoices = [ u"None", u"o", u".", u",", u"v", u"^", u"<", u">", u"s", u"*", u"+", u"x" ]
		self.y2_marker = wx.Choice( self.NBPanel_TimeSeries, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, y2_markerChoices, 0 )
		self.y2_marker.SetSelection( 0 )
		self.y2_marker.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.y2_marker.Enable( False )
		
		bSizer6111.Add( self.y2_marker, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.y2_markersize = wx.SpinCtrl( self.NBPanel_TimeSeries, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 5 )
		self.y2_markersize.Enable( False )
		
		bSizer6111.Add( self.y2_markersize, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer67.Add( bSizer6111, 1, wx.EXPAND, 5 )
		
		
		bSizer601.Add( bSizer67, 0, wx.EXPAND, 5 )
		
		
		bSizer601.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText2021 = wx.StaticText( self.NBPanel_TimeSeries, wx.ID_ANY, u"Choose Licor Mode", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText2021.Wrap( -1 )
		bSizer601.Add( self.m_staticText2021, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer3611 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer3711 = wx.BoxSizer( wx.VERTICAL )
		
		self.y2_CHequ = wx.CheckBox( self.NBPanel_TimeSeries, wx.ID_ANY, u"EQU", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.y2_CHequ.Enable( False )
		
		bSizer3711.Add( self.y2_CHequ, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.y2_CHzero = wx.CheckBox( self.NBPanel_TimeSeries, wx.ID_ANY, u"ZERO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.y2_CHzero.Enable( False )
		
		bSizer3711.Add( self.y2_CHzero, 0, wx.ALL, 5 )
		
		
		bSizer3611.Add( bSizer3711, 1, wx.EXPAND, 5 )
		
		bSizer381 = wx.BoxSizer( wx.VERTICAL )
		
		self.y2_CHatm = wx.CheckBox( self.NBPanel_TimeSeries, wx.ID_ANY, u"ATM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.y2_CHatm.SetValue(True) 
		self.y2_CHatm.Enable( False )
		
		bSizer381.Add( self.y2_CHatm, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.y2_CHspan = wx.CheckBox( self.NBPanel_TimeSeries, wx.ID_ANY, u"SPAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.y2_CHspan.Enable( False )
		
		bSizer381.Add( self.y2_CHspan, 0, wx.ALL|wx.LEFT, 5 )
		
		
		bSizer3611.Add( bSizer381, 1, wx.EXPAND|wx.LEFT, 5 )
		
		
		bSizer601.Add( bSizer3611, 0, wx.EXPAND|wx.LEFT, 20 )
		
		
		Size_MP_Y2ax_prop.Add( bSizer601, 1, wx.EXPAND, 5 )
		
		
		bSizer95.Add( Size_MP_Y2ax_prop, 4, wx.ALL|wx.EXPAND, 5 )
		
		
		Sizer_XYPlots.Add( bSizer95, 1, wx.EXPAND, 5 )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		self.BTN_plot = wx.Button( self.NBPanel_TimeSeries, wx.ID_ANY, u"Plot Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BTN_plot.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.BTN_plot.Enable( False )
		
		bSizer42.Add( self.BTN_plot, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		Sizer_XYPlots.Add( bSizer42, 0, wx.EXPAND, 5 )
		
		
		self.NBPanel_TimeSeries.SetSizer( Sizer_XYPlots )
		self.NBPanel_TimeSeries.Layout()
		Sizer_XYPlots.Fit( self.NBPanel_TimeSeries )
		self.MAIN.AddPage( self.NBPanel_TimeSeries, u"Time Series", False )
		self.NBPanel_Map = wx.Panel( self.MAIN, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer421 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer68 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer65 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.NBPanel_Map, wx.ID_ANY, u"C-axis Properties" ), wx.VERTICAL )
		
		m_varChoices = []
		self.m_var = wx.Choice( self.NBPanel_Map, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_varChoices, 0 )
		self.m_var.SetSelection( 0 )
		sbSizer5.Add( self.m_var, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_title = wx.TextCtrl( self.NBPanel_Map, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_title.Enable( False )
		
		sbSizer5.Add( self.m_title, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer571 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText32 = wx.StaticText( self.NBPanel_Map, wx.ID_ANY, u"MAX", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText32.Wrap( -1 )
		bSizer571.Add( self.m_staticText32, 1, wx.TOP, 5 )
		
		self.m_staticText31 = wx.StaticText( self.NBPanel_Map, wx.ID_ANY, u"MIN", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText31.Wrap( -1 )
		bSizer571.Add( self.m_staticText31, 1, wx.TOP, 5 )
		
		
		sbSizer5.Add( bSizer571, 0, wx.EXPAND, 5 )
		
		bSizer561 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_cmin = wx.TextCtrl( self.NBPanel_Map, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cmin.Enable( False )
		
		bSizer561.Add( self.m_cmin, 1, wx.BOTTOM|wx.LEFT|wx.RIGHT, 5 )
		
		self.m_cmax = wx.TextCtrl( self.NBPanel_Map, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cmax.Enable( False )
		
		bSizer561.Add( self.m_cmax, 1, wx.BOTTOM|wx.LEFT|wx.RIGHT, 5 )
		
		
		sbSizer5.Add( bSizer561, 0, wx.EXPAND, 5 )
		
		bSizer6112 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_markerChoices = [ u"o - circle", u"^ - triangle up", u"v - triangle down", u"< - triangle left", u"> - triangle right", u"s - square", u"D - diamond", u"p - pentagon", u"h - hexagon", u"8 - octagon" ]
		self.m_marker = wx.Choice( self.NBPanel_Map, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_markerChoices, 0 )
		self.m_marker.SetSelection( 0 )
		self.m_marker.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_marker.Enable( False )
		
		bSizer6112.Add( self.m_marker, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_markersize = wx.SpinCtrl( self.NBPanel_Map, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 50 )
		self.m_markersize.Enable( False )
		
		bSizer6112.Add( self.m_markersize, 1, wx.ALL, 5 )
		
		
		sbSizer5.Add( bSizer6112, 0, wx.EXPAND, 5 )
		
		self.m_cmaps = wx.combo.BitmapComboBox( self.NBPanel_Map, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", wx.CB_READONLY ) 
		self.m_cmaps.Enable( False )
		self.m_cmaps.SetMinSize( wx.Size( 285,-1 ) )
		
		sbSizer5.Add( self.m_cmaps, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer65.Add( sbSizer5, 0, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self.NBPanel_Map, wx.ID_ANY, u"Choose Licor modes" ), wx.VERTICAL )
		
		bSizer3612 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer3612.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer3712 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_CHequ = wx.CheckBox( self.NBPanel_Map, wx.ID_ANY, u"EQU", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_CHequ.SetValue(True) 
		self.m_CHequ.Enable( False )
		
		bSizer3712.Add( self.m_CHequ, 0, wx.ALL, 5 )
		
		self.m_CHzero = wx.CheckBox( self.NBPanel_Map, wx.ID_ANY, u"ZERO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_CHzero.Enable( False )
		
		bSizer3712.Add( self.m_CHzero, 0, wx.ALL, 5 )
		
		
		bSizer3612.Add( bSizer3712, 1, wx.EXPAND, 5 )
		
		bSizer382 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_CHatm = wx.CheckBox( self.NBPanel_Map, wx.ID_ANY, u"ATM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_CHatm.Enable( False )
		
		bSizer382.Add( self.m_CHatm, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_CHspan = wx.CheckBox( self.NBPanel_Map, wx.ID_ANY, u"SPAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_CHspan.Enable( False )
		
		bSizer382.Add( self.m_CHspan, 0, wx.ALL|wx.LEFT, 5 )
		
		
		bSizer3612.Add( bSizer382, 1, wx.EXPAND|wx.LEFT, 5 )
		
		
		bSizer3612.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		sbSizer10.Add( bSizer3612, 0, wx.EXPAND, 5 )
		
		
		bSizer65.Add( sbSizer10, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer68.Add( bSizer65, 0, wx.EXPAND, 5 )
		
		bSizer57 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.NBPanel_Map, wx.ID_ANY, u"Date Range" ), wx.VERTICAL )
		
		bSizer46 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_dmin = wx.Slider( self.NBPanel_Map, wx.ID_ANY, 0, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_BOTH )
		self.m_dmin.Enable( False )
		
		bSizer46.Add( self.m_dmin, 1, wx.ALL, 5 )
		
		self.m_dmax = wx.Slider( self.NBPanel_Map, wx.ID_ANY, 100, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_BOTH|wx.SL_HORIZONTAL )
		self.m_dmax.Enable( False )
		
		bSizer46.Add( self.m_dmax, 1, wx.ALL, 5 )
		
		
		sbSizer6.Add( bSizer46, 0, wx.EXPAND, 5 )
		
		bSizer471 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_mindate_str = wx.StaticText( self.NBPanel_Map, wx.ID_ANY, u"Start date", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_mindate_str.Wrap( -1 )
		self.m_mindate_str.Enable( False )
		
		bSizer471.Add( self.m_mindate_str, 1, wx.ALL, 5 )
		
		self.m_maxdate_str = wx.StaticText( self.NBPanel_Map, wx.ID_ANY, u"End date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_maxdate_str.Wrap( -1 )
		self.m_maxdate_str.Enable( False )
		
		bSizer471.Add( self.m_maxdate_str, 1, wx.ALL, 5 )
		
		
		sbSizer6.Add( bSizer471, 0, wx.EXPAND, 5 )
		
		
		bSizer57.Add( sbSizer6, 0, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.NBPanel_Map, wx.ID_ANY, u"Latitude and Longitude Limits" ), wx.VERTICAL )
		
		bSizer53 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_north = wx.TextCtrl( self.NBPanel_Map, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_north.Enable( False )
		
		bSizer53.Add( self.m_north, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer7.Add( bSizer53, 0, wx.EXPAND, 5 )
		
		bSizer54 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_west = wx.TextCtrl( self.NBPanel_Map, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_west.Enable( False )
		
		bSizer54.Add( self.m_west, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText30 = wx.StaticText( self.NBPanel_Map, wx.ID_ANY, u"N\nW                       E\nS", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText30.Wrap( -1 )
		bSizer54.Add( self.m_staticText30, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_east = wx.TextCtrl( self.NBPanel_Map, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_east.Enable( False )
		
		bSizer54.Add( self.m_east, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer7.Add( bSizer54, 0, wx.EXPAND, 5 )
		
		bSizer55 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_south = wx.TextCtrl( self.NBPanel_Map, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_south.Enable( False )
		
		bSizer55.Add( self.m_south, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer7.Add( bSizer55, 0, wx.EXPAND, 5 )
		
		self.m_globrange = wx.Button( self.NBPanel_Map, wx.ID_ANY, u"Global Limits", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_globrange.Enable( False )
		
		sbSizer7.Add( self.m_globrange, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 20 )
		
		
		bSizer57.Add( sbSizer7, 0, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self.NBPanel_Map, wx.ID_ANY, u"Plot Options" ), wx.VERTICAL )
		
		bSizer64 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText33 = wx.StaticText( self.NBPanel_Map, wx.ID_ANY, u"Draw: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		bSizer64.Add( self.m_staticText33, 1, wx.ALL, 5 )
		
		self.m_coastlines = wx.CheckBox( self.NBPanel_Map, wx.ID_ANY, u"Coastlines", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_coastlines.SetValue(True) 
		self.m_coastlines.Enable( False )
		
		bSizer64.Add( self.m_coastlines, 1, wx.ALL, 5 )
		
		self.m_landfill = wx.CheckBox( self.NBPanel_Map, wx.ID_ANY, u"Landfill", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_landfill.SetValue(True) 
		self.m_landfill.Enable( False )
		
		bSizer64.Add( self.m_landfill, 1, wx.ALL, 5 )
		
		self.m_rivers = wx.CheckBox( self.NBPanel_Map, wx.ID_ANY, u"Rivers", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_rivers.Enable( False )
		
		bSizer64.Add( self.m_rivers, 1, wx.ALL, 5 )
		
		
		sbSizer9.Add( bSizer64, 0, wx.EXPAND, 5 )
		
		bSizer63 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText311 = wx.StaticText( self.NBPanel_Map, wx.ID_ANY, u"Resolution", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_staticText311.Wrap( -1 )
		bSizer63.Add( self.m_staticText311, 0, wx.ALL, 10 )
		
		m_resChoices = [ u"crude", u"low", u"intermediate", u"high" ]
		self.m_res = wx.Choice( self.NBPanel_Map, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_resChoices, 0 )
		self.m_res.SetSelection( 2 )
		self.m_res.Enable( False )
		
		bSizer63.Add( self.m_res, 0, wx.ALL|wx.LEFT, 7 )
		
		
		sbSizer9.Add( bSizer63, 1, wx.EXPAND, 5 )
		
		
		bSizer57.Add( sbSizer9, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer68.Add( bSizer57, 1, wx.EXPAND, 5 )
		
		
		bSizer421.Add( bSizer68, 1, wx.EXPAND, 5 )
		
		self.BTN_m_plot = wx.Button( self.NBPanel_Map, wx.ID_ANY, u"Plot map", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BTN_m_plot.Enable( False )
		
		bSizer421.Add( self.BTN_m_plot, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.NBPanel_Map.SetSizer( bSizer421 )
		self.NBPanel_Map.Layout()
		bSizer421.Fit( self.NBPanel_Map )
		self.MAIN.AddPage( self.NBPanel_Map, u"Scatter Map", False )
		
		Sizer_NoteBook.Add( self.MAIN, 1, wx.EXPAND, 5 )
		
		
		Sizer_MAIN2.Add( Sizer_NoteBook, 1, wx.EXPAND, 5 )
		
		
		self.Panel_MAIN.SetSizer( Sizer_MAIN2 )
		self.Panel_MAIN.Layout()
		Sizer_MAIN2.Fit( self.Panel_MAIN )
		Panel_MAIN1.Add( self.Panel_MAIN, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( Panel_MAIN1 )
		self.Layout()
		self.StatusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.LB_HELP.Bind( wx.EVT_LISTBOX, self.func_update_help )
		self.DirSelector.Bind( wx.EVT_DIRPICKER_CHANGED, self.func_listfiles )
		self.BTN_LoadFile.Bind( wx.EVT_FILEPICKER_CHANGED, self.func_loaddata )
		self.CB_SelectAll.Bind( wx.EVT_CHECKBOX, self.func_select_files )
		self.LB_Files.Bind( wx.EVT_LISTBOX, self.func_update_checkbox )
		self.Button_ReadFiles.Bind( wx.EVT_BUTTON, self.func_read_selected )
		self.BTN_SaveFile.Bind( wx.EVT_FILEPICKER_CHANGED, self.func_savedata )
		self.BTN_calcCO2.Bind( wx.EVT_BUTTON, self.func_calc_co2 )
		self.x_var.Bind( wx.EVT_CHOICE, self.update_x_params )
		self.x_minslide.Bind( wx.EVT_SCROLL, self.update_xlims )
		self.x_maxslide.Bind( wx.EVT_SCROLL, self.update_xlims )
		self.y1_var.Bind( wx.EVT_CHOICE, self.update_y1_params )
		self.y1_CHequ.Bind( wx.EVT_CHECKBOX, self.update_y1_params )
		self.y1_CHzero.Bind( wx.EVT_CHECKBOX, self.update_y1_params )
		self.y1_CHatm.Bind( wx.EVT_CHECKBOX, self.update_y1_params )
		self.y1_CHspan.Bind( wx.EVT_CHECKBOX, self.update_y1_params )
		self.y2_var.Bind( wx.EVT_CHOICE, self.update_y2_params )
		self.y2_CHequ.Bind( wx.EVT_CHECKBOX, self.update_y2_params )
		self.y2_CHzero.Bind( wx.EVT_CHECKBOX, self.update_y2_params )
		self.y2_CHatm.Bind( wx.EVT_CHECKBOX, self.update_y2_params )
		self.y2_CHspan.Bind( wx.EVT_CHECKBOX, self.update_y2_params )
		self.BTN_plot.Bind( wx.EVT_BUTTON, self.func_plotxy )
		self.m_var.Bind( wx.EVT_CHOICE, self.update_m_params )
		self.m_CHequ.Bind( wx.EVT_CHECKBOX, self.update_m_params )
		self.m_CHzero.Bind( wx.EVT_CHECKBOX, self.update_m_params )
		self.m_CHatm.Bind( wx.EVT_CHECKBOX, self.update_m_params )
		self.m_CHspan.Bind( wx.EVT_CHECKBOX, self.update_m_params )
		self.m_dmin.Bind( wx.EVT_SCROLL, self.func_update_mdates )
		self.m_dmax.Bind( wx.EVT_SCROLL, self.func_update_mdates )
		self.m_globrange.Bind( wx.EVT_BUTTON, self.func_m_global_limits )
		self.BTN_m_plot.Bind( wx.EVT_BUTTON, self.func_plot_map )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def func_update_help( self, event ):
		event.Skip()
	
	def func_listfiles( self, event ):
		event.Skip()
	
	def func_loaddata( self, event ):
		event.Skip()
	
	def func_select_files( self, event ):
		event.Skip()
	
	def func_update_checkbox( self, event ):
		event.Skip()
	
	def func_read_selected( self, event ):
		event.Skip()
	
	def func_savedata( self, event ):
		event.Skip()
	
	def func_calc_co2( self, event ):
		event.Skip()
	
	def update_x_params( self, event ):
		event.Skip()
	
	def update_xlims( self, event ):
		event.Skip()
	
	
	def update_y1_params( self, event ):
		event.Skip()
	
	
	
	
	
	def update_y2_params( self, event ):
		event.Skip()
	
	
	
	
	
	def func_plotxy( self, event ):
		event.Skip()
	
	def update_m_params( self, event ):
		event.Skip()
	
	
	
	
	
	def func_update_mdates( self, event ):
		event.Skip()
	
	
	def func_m_global_limits( self, event ):
		event.Skip()
	
	def func_plot_map( self, event ):
		event.Skip()
	

