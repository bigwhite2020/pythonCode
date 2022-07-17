# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4( wx.Frame ):

    def __init__(self, parent):
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size( 624, 300 ), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gbSizer5 = wx.GridBagSizer( 0, 0 )
        gbSizer5.SetFlexibleDirection( wx.BOTH )
        gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        gbSizer7 = wx.GridBagSizer( 0, 0 )
        gbSizer7.SetFlexibleDirection( wx.BOTH )
        gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button34 = wx.Button( self, wx.ID_ANY, u"时间戳转换", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer7.Add( self.m_button34, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button35 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer7.Add( self.m_button35, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button36 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer7.Add( self.m_button36, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button37 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer7.Add( self.m_button37, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer5.Add( gbSizer7, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer8 = wx.GridBagSizer( 0, 0 )
        gbSizer8.SetFlexibleDirection( wx.BOTH )
        gbSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button41 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer8.Add( self.m_button41, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button42 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer8.Add( self.m_button42, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button43 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer8.Add( self.m_button43, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button44 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer8.Add( self.m_button44, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer5.Add( gbSizer8, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        self.SetSizer( gbSizer5 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button34.Bind( wx.EVT_BUTTON, self.button1 )

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def button1(self, event):
        event.Skip()


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2( wx.Frame ):

    def __init__(self, parent):
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size( 500, 300 ), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gbSizer4 = wx.GridBagSizer( 0, 0 )
        gbSizer4.SetFlexibleDirection( wx.BOTH )
        gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        gbSizer5 = wx.GridBagSizer( 0, 0 )
        gbSizer5.SetFlexibleDirection( wx.BOTH )
        gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button13 = wx.Button( self, wx.ID_ANY, u"获取当前时间戳", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_button13, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_textCtrl1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer4.Add( gbSizer5, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer7 = wx.GridBagSizer( 0, 0 )
        gbSizer7.SetFlexibleDirection( wx.BOTH )
        gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button14 = wx.Button( self, wx.ID_ANY, u"转换日期格式为时间戳", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer7.Add( self.m_button14, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer7.Add( self.m_textCtrl4, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer7.Add( self.m_textCtrl5, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer4.Add( gbSizer7, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gbSizer8 = wx.GridBagSizer( 0, 0 )
        gbSizer8.SetFlexibleDirection( wx.BOTH )
        gbSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button15 = wx.Button( self, wx.ID_ANY, u"转换时间戳为日期格式", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer8.Add( self.m_button15, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer8.Add( self.m_textCtrl6, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer8.Add( self.m_textCtrl7, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer4.Add( gbSizer8, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        self.SetSizer( gbSizer4 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button13.Bind( wx.EVT_BUTTON, self.button1_1 )
        self.m_button14.Bind( wx.EVT_BUTTON, self.button1_2 )
        self.m_button15.Bind( wx.EVT_BUTTON, self.button1_3 )

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def button1_1(self, event):
        event.Skip()

    def button1_2(self, event):
        event.Skip()

    def button1_3(self, event):
        event.Skip()

    def timestamp_to_date(time_stamp, format_string="%Y-%m-%d %H:%M:%S"):
        time_array = time.localtime(t/1000)
        str_date = time.strftime( format_string, time_array )
        return str_date


