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

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"测试-加法运算", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer2.Add( self.m_staticText2, 0, wx.ALL | wx.EXPAND, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"请输入第一个数字：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_textCtrl2, 0, wx.ALL | wx.EXPAND, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, u"请输入第二个数字：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_textCtrl3, 0, wx.ALL | wx.EXPAND, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"测试-加法", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button3, 0, wx.ALL | wx.EXPAND, 5 )

        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, u"计算结果:", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_textCtrl4, 0, wx.ALL | wx.EXPAND, 5 )

        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button3.Bind( wx.EVT_BUTTON, self.button )

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def button(self, event):
        num1 = int(self.m_textCtrl2.GetValue())
        num2 = int(self.m_textCtrl3.GetValue())
        numRes=str(num1+num2)
        self.m_textCtrl4.SetValue(numRes)


app = wx.App()
main=MyFrame2(None)
main.Show()
app.MainLoop()
