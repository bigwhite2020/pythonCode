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
## Class MyFrame1
###########################################################################

class MyFrame1( wx.Frame ):

    def __init__(self, parent):
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=u"测试", pos=wx.DefaultPosition, size=wx.Size( 500, 300 ),
                           style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"测试按钮1", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_button1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.SetSizer( gbSizer1 )
        self.Layout()
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu2 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"测试选项1", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_menuItem1 )

        self.m_menubar1.Append( self.m_menu2, u"测试菜单" )

        self.SetMenuBar( self.m_menubar1 )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.button1 )
        self.Bind( wx.EVT_MENU, self.test1, id=self.m_menuItem1.GetId() )

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def button1(self, event):
        # event.Skip()
        self.frame=wx.Frame(None,title =u"测试按钮窗口",size =(300,100),pos=(100,100))
        self.frame.Show()

    def test1(self, event):
        #event.Skip()
        self.frame=wx.Frame(None,title =u"测试菜单窗口",size =(300,100),pos=(500,100))
        self.frame.Show()

app = wx.App()
main=MyFrame1(None)
main.Show()
app.MainLoop()

