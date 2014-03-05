# -*- coding: utf-8 -*-
"""

created: Sun Jan 26 11:59:52 2014
author:  Luke Gregor
"""
import sys

def TextFile_2_TextCtrl(TextCtrl, txt_file_name, pfx='', sfx=''):

    with open(pfx + txt_file_name + sfx, 'r') as file_obj:

        txt_str = file_obj.read()
        
        
    if sys.platform == 'darwin':
        txt_str = txt_str.replace('\n', '')
    TextCtrl.AppendText(txt_str)


def func_update_help( self, event ):

    idx = self.LB_HELP.GetSelection()
    self.TXT_HELP.Clear()
    TextFile_2_TextCtrl(self.TXT_HELP,
                        self.help_list[1][idx],
                        pfx='./doc/help_', sfx='.txt')
    self.TXT_HELP.ScrollPages(-10)