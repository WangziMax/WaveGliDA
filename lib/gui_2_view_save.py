# -*- coding: utf-8 -*-
"""

created: Sun Jan 26 11:13:52 2014
author:  Luke Gregor
"""
from read_directory import get_wg_filenames, read_wg_filelist
import numpy as np
import os
from datetime import datetime
from pandas import read_csv
import wx
import thread
import wx.grid as wxGrid
import time

    
class HugeTable(wxGrid.PyGridTableBase):
    def __init__(self, pdDataFrame):
        wxGrid.PyGridTableBase.__init__(self)
        
        datetimes = pdDataFrame.index.to_datetime()
        self.rowLabels = [d.strftime('%Y-%m-%d    %H:%M') for d in datetimes]

        self.colLabels = pdDataFrame.keys()

        self.data = pdDataFrame.values
        
    def GetAttr(self, row, col, kind ):
        attr = wxGrid.GridCellAttr()
        attr.SetReadOnly( 1 )
        return attr
        
    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0])

    def GetValue(self, row, col):
        return self.data[row][col]

    #~ # Called when the grid needs to display column labels               
    def GetColLabelValue(self, col):
        return self.colLabels[col]

    #~ # Called when the grid needs to display row labels
    def GetRowLabelValue(self,row):
        return self.rowLabels[row]

        
def func_populate_datagrid( self, event ):

    self.StatusBar.SetStatusText('loading data into spreadsheet...')
    self.Files_Progress.SetValue(0)
    
    table = HugeTable(self.data)
    
    self.GridData.SetTable(table, True)
    
    self.StatusBar.SetStatusText('')

    self.BTN_SaveFile.Enable()
    self.BTN_SaveFile.SetPath('%s.wg.csv' % datetime.today().strftime('%Y%m%d_%H%M'))
    
    self.func_populate_plot_choices()
    self.func_populate_map_choices()
    
    
def func_export_opts( self, event ):
    
    rb_s = self.RB_ExportOpts.GetSelection()
    selected_item = self.RB_ExportOpts.GetItemLabel(rb_s)
    if selected_item == 'all rows':
        bool_func = lambda s: np.isrealobj(s)
    elif selected_item == 'pump_off':
        bool_func = lambda s: s.endswith('pump_off')
    else:
        bool_func = lambda s: s == selected_item
    
    self.save_ind = np.array( map( bool_func, self.data.licor_cmnd ) )
    
    self.StatusBar.SetStatusText("'%s' chosen (%d items)" % (selected_item, np.sum(self.save_ind)))
    
    thread.start_new_thread(self.clear_status_text, ())



def func_savedata( self, event ):
    
    self.func_export_opts( None )
    fullpath = self.BTN_SaveFile.GetPath()
    file_ext = os.path.splitext(fullpath)
    if file_ext[-1] == '.csv':
        self.data.ix[self.save_ind,:].to_csv(fullpath)
        
        self.StatusBar.SetStatusText('File saved as %s' % fullpath)
        self.clear_status_text()
    
    #~ elif file_ext[-1] == '.mat':
        #~ from scipy.io import savemat
        #~ save_dict = dict( zip( self.data.keys(), self.data.values.T ) )
        #~ savemat(fullpath, save_dict)


