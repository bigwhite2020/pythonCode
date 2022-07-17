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
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=u"窗体1", pos=wx.DefaultPosition, size=wx.Size( 250, 100 ),
                           style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gbSizer1=wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button1=wx.Button( self, wx.ID_ANY, u"打开第二个窗体", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_button1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText1=wx.StaticText( self, wx.ID_ANY, u"回调文本框", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        gbSizer1.Add( self.m_staticText1, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl1=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_textCtrl1, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.SetSizer( gbSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.button1 )

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
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=u"窗体2", pos=wx.DefaultPosition, size=wx.Size( 250, 100 ),
                           style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gbSizer2=wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button2=wx.Button( self, wx.ID_ANY, u"传递给窗体1", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_button2, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl2=wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_textCtrl2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.SetSizer( gbSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button2.Bind( wx.EVT_BUTTON, self.button2 )

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def button2(self, event):
        event.Skip()


