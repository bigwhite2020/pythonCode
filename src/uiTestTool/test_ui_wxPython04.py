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
## Class MyFrame2
###########################################################################

class MyFrame2( wx.Frame ):

    def __init__(self, parent):
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size( 500, 300 ), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_button5 = wx.Button( self, wx.ID_ANY, u"测试按钮", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button5, 0, wx.ALL | wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer1.Add( self.m_staticText4, 0, wx.ALL | wx.EXPAND, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, u"请输入内容", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_textCtrl3, 0, wx.ALL | wx.EXPAND, 5 )

        self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_checkBox1, 0, wx.ALL | wx.EXPAND, 5 )

        self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.m_gauge1.SetValue( 0 )
        bSizer1.Add( self.m_gauge1, 0, wx.ALL | wx.EXPAND, 5 )

        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_timer1 = wx.Timer()
        self.m_timer1.SetOwner( self, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button5.Bind( wx.EVT_BUTTON, self.button )
        self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.checkbox )

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def button(self, event):
        self.m_gauge1.SetValue(50)

    def checkbox(self, event):
        self.m_gauge1.SetValue(100)

app = wx.App()
main=MyFrame2(None)
main.Show()
app.MainLoop()


