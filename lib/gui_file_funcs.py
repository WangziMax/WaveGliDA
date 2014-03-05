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


def func_listfiles(self, event):
    wg_dir = self.DirSelector.GetPath()

    self.file_list = get_wg_filenames(wg_dir)
    file_list = [os.path.split(fname)[-1] for fname in self.file_list]

    self.CB_SelectAll.Set3StateValue(0)
    self.Button_ReadFiles.Enable( False )
    self.LB_Files.SetItems(file_list)
    self.CB_SelectAll.Enable(True)


def func_select_files( self, event ):
    if self.CB_SelectAll.Get3StateValue() == 0:
        self.Button_ReadFiles.Enable( False )
        for i in self.LB_Files.GetSelections():
            self.LB_Files.SetSelection(i, False)
    elif self.CB_SelectAll.Get3StateValue() == 1:
        self.Button_ReadFiles.Enable( True )
        for i in range(len(self.LB_Files.Items)):
            self.LB_Files.SetSelection(i, True)
    elif self.CB_SelectAll.Get3StateValue() == 2:
        self.Button_ReadFiles.Enable( True )


def func_update_checkbox( self, event ):
    num_selections = len(self.LB_Files.GetSelections())
    num_items = len(self.LB_Files.Items)
    if num_selections == 0:
        self.CB_SelectAll.Set3StateValue(0)
        self.Button_ReadFiles.Enable( False )
    elif num_selections == num_items:
        self.CB_SelectAll.Set3StateValue(1)
        self.Button_ReadFiles.Enable( True )
    else:
        self.CB_SelectAll.Set3StateValue(2)
        self.Button_ReadFiles.Enable( True )


def func_read_selected( self, event ):

    join = os.path.join
    all_list =  np.array(self.LB_Files.Items)
    selection = np.array(self.LB_Files.GetSelections())
    dir_path =  self.DirSelector.GetPath()

    file_list = [join(dir_path, fname) for fname in all_list[selection]]

    self.data = read_wg_filelist(file_list,
                                 progress_obj=self.Files_Progress,
                                 statusbar_obj=self.StatusBar)
    
    self.func_calc_salt( None )
    
    self.TC_FileStatus.Clear()
    self.TC_FileStatus.AppendText(self.data.__str__())
    self.TC_FileStatus.SetInsertionPoint(0)
    self.func_populate_datagrid()


def func_loaddata( self, event ):

    fullpath = self.BTN_LoadFile.GetPath()
    file_ext = os.path.splitext(fullpath)[-1]

    if file_ext == '.csv':
        try:
            self.data = read_csv(fullpath, index_col='wg_datetime')
            self.Files_Progress.SetValue(100)
            self.TC_FileStatus.AppendText(self.data.__str__())
            self.TC_FileStatus.SetInsertionPoint(0)
        except ValueError:
            error_str = "The file you have selected is not a valid WavGliDaPro file:"
            error_str += "\n%s does not have the column 'wg_datetime'" % fullpath
            error_str += "\n\n Try loading the raw files if all else fails."
            dlg = wx.MessageDialog(self, error_str,'Import Error', wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
            return None

    for key in self.data.keys():
        if key.startswith('Unnamed'):
            self.data.pop(key)
    
    self.func_calc_salt( None )
    
    self.func_populate_datagrid()
#        self.func_calc_salt(None)


def func_savedata( self, event ):

    fullpath = self.BTN_SaveFile.GetPath()
    file_ext = os.path.splitext(fullpath)
    if file_ext[-1] == '.csv':
        self.data.to_csv(fullpath)
        
    elif file_ext[-1] == '.mat':
        from scipy.io import savemat
        save_dict = dict( zip( self.data.keys(), self.data.values.T ) )
        savemat(fullpath, save_dict)
    


def func_populate_datagrid( self ):

    self.StatusBar.SetStatusText('loading data into spreadsheet...')
    datetimes = self.data.index.to_datetime()

    while len(self.data.keys()) >= self.GridData.NumberCols:
        self.GridData.AppendCols()
    while len(self.data.keys()) < self.GridData.NumberCols:
        self.GridData.DeleteCols()
    while len(datetimes) >= self.GridData.NumberRows:
        self.GridData.AppendRows()
    while len(datetimes) < self.GridData.NumberRows:
        self.GridData.DeleteRows()

    for c, col in enumerate(self.data.iteritems()):
        self.GridData.SetColLabelValue(c, col[0])
    for r, dt in enumerate(datetimes):
        self.GridData.SetRowLabelValue(r, dt.strftime('%Y-%m-%d  %H:%M'))

    self.GridData.AutoSizeColumns()
    self.GridData.SetRowLabelSize(120)

    data = self.data.values.astype(str)
    Grid = self.GridData
    R, C = data.shape
    for c in range(C):
        for r in np.arange(R):
            Grid.SetCellValue(r, c, data[r,c])

    self.BTN_SaveFile.Enable()
    self.BTN_SaveFile.SetPath('%s_wg.csv' % datetime.today().strftime('%Y%m%d_%H%M'))
    self.StatusBar.SetStatusText('')
    self.func_populate_plot_choices()
    self.func_populate_map_choices()

    
    