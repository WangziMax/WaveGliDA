# -*- coding: utf-8 -*-
"""
created: Sat Jan 18 23:42:04 2014
author:  Luke Gregor
"""
import numpy as np
import calc_co2 as co2
import time


def list_2_ListBox( self, ListBox, item_list):

    item_list = np.array(item_list[0])
    for item in item_list:
        ListBox.Append(item)


def clear_status_text( self ):
    time.sleep(2)
    self.StatusBar.SetStatusText('')


def pdDataFrame_2_numpy(Data, col_names=None):

    if not col_names:
        col_names = Data.keys()

    out = {}

    for key in col_names:
        out[key] = np.array(Data[key])

    return out