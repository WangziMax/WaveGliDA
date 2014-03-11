# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2013)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Frame_ERROR
###########################################################################

class Frame_ERROR ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.Point( 500,300 ), size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer60 = wx.BoxSizer( wx.VERTICAL )
		
		self.text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 450,350 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.text.SetMinSize( wx.Size( 450,350 ) )
		
		bSizer60.Add( self.text, 1, wx.EXPAND, 5 )
		
		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.BTN_send = wx.Button( self.m_panel11, wx.ID_ANY, u"Send Error", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.BTN_send, 1, wx.ALL, 5 )
		
		self.BTN_close = wx.Button( self.m_panel11, wx.ID_ANY, u"Close Window", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.BTN_close, 1, wx.ALL, 5 )
		
		
		self.m_panel11.SetSizer( bSizer61 )
		self.m_panel11.Layout()
		bSizer61.Fit( self.m_panel11 )
		bSizer60.Add( self.m_panel11, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer60 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.BTN_send.Bind( wx.EVT_BUTTON, self.email_error )
		self.BTN_close.Bind( wx.EVT_BUTTON, self.close_all_windows )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def email_error( self, event ):
		event.Skip()
	
	def close_all_windows( self, event ):
		event.Skip()
	

