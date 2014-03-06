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
    
    
    NormCursor = self.MAIN.GetCursor()
    BusyCursor = wx.StockCursor(wx.CURSOR_WAIT)
    self.MAIN.SetCursor(BusyCursor)
    
    self.ImportErrors = ''
    self.TC_FileStatus.Clear()
    
    self.data = read_wg_filelist(file_list, self)
    
    num_import_errors = len(self.ImportErrors.splitlines())
    self.TC_FileStatus.AppendText('================\n')
    self.TC_FileStatus.AppendText(' IMPORT SUMMARY\n')
    self.TC_FileStatus.AppendText('================\n')
    self.TC_FileStatus.AppendText('Total Files:  %d\n' % len(file_list))
    self.TC_FileStatus.AppendText('Successful:   %d\n' % (len(file_list) - num_import_errors))
    self.TC_FileStatus.AppendText('Failed:       %d (names below)\n' % num_import_errors)
    self.TC_FileStatus.AppendText(self.ImportErrors)
    self.func_calc_salt( None )
    self.func_calc_co2 ( None )
    
    date_sta, date_end = self.data.__str__().split('\n')[1].split(',')[1].strip().split(' to ')
    date_sta = datetime.strptime(date_sta.split('+')[0], '%Y-%m-%d %H:%M:%S')
    date_end = datetime.strptime(date_end.split('+')[0], '%Y-%m-%d %H:%M:%S')
    self.TC_FileStatus.AppendText('\n')
    self.TC_FileStatus.AppendText('==============\n')
    self.TC_FileStatus.AppendText(' DATA SUMMARY \n')
    self.TC_FileStatus.AppendText('==============\n')
    self.TC_FileStatus.AppendText('Start \t')
    self.TC_FileStatus.AppendText('%s \n' % date_sta.strftime('%H:%M - %d %b %Y'))
    self.TC_FileStatus.AppendText('End   \t')
    self.TC_FileStatus.AppendText('%s \n\n' % date_end.strftime('%H:%M - %d %b %Y'))
    self.TC_FileStatus.AppendText('\n'.join(self.data.__str__().split('\n')[2:-1]))
    self.TC_FileStatus.SetInsertionPoint(0)
    
    self.func_populate_datagrid( None )
    
    self.MAIN.SetCursor(NormCursor)


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
    
    self.TC_FileStatus.Clear()
    NormCursor = self.MAIN.GetCursor()
    BusyCursor = wx.StockCursor(wx.CURSOR_WAIT)
    self.MAIN.SetCursor(BusyCursor)
    
    self.func_calc_salt( None )
    self.func_calc_co2( None )
    
    date_sta, date_end = self.data.__str__().split('\n')[1].split(',')[1].strip().split(' to ')
    date_sta = datetime.strptime(date_sta.split('+')[0], '%Y-%m-%d %H:%M:%S')
    date_end = datetime.strptime(date_end.split('+')[0], '%Y-%m-%d %H:%M:%S')
    self.TC_FileStatus.AppendText('\n')
    self.TC_FileStatus.AppendText('==============\n')
    self.TC_FileStatus.AppendText(' DATA SUMMARY \n')
    self.TC_FileStatus.AppendText('==============\n')
    self.TC_FileStatus.AppendText('Start \t')
    self.TC_FileStatus.AppendText('%s \n' % date_sta.strftime('%H:%M - %d %b %Y'))
    self.TC_FileStatus.AppendText('End   \t')
    self.TC_FileStatus.AppendText('%s \n\n' % date_end.strftime('%H:%M - %d %b %Y'))
    self.TC_FileStatus.AppendText('\n'.join(self.data.__str__().split('\n')[2:-1]))
    self.TC_FileStatus.SetInsertionPoint(0)
    
    self.func_populate_datagrid( None )
    
    self.MAIN.SetCursor(NormCursor)


def func_savedata( self, event ):

    fullpath = self.BTN_SaveFile.GetPath()
    file_ext = os.path.splitext(fullpath)
    if file_ext[-1] == '.csv':
        self.data.to_csv(fullpath)
        
    elif file_ext[-1] == '.mat':
        from scipy.io import savemat
        save_dict = dict( zip( self.data.keys(), self.data.values.T ) )
        savemat(fullpath, save_dict)
    


def func_populate_datagrid( self, event ):

    self.StatusBar.SetStatusText('loading data into spreadsheet...')
    self.Files_Progress.SetValue(0)
    
    table = HugeTable(self.data)
    
    self.GridData.SetTable(table, True)
    
    self.StatusBar.SetStatusText('')

    self.BTN_SaveFile.Enable()
    self.BTN_calcCO2.Enable()
    self.BTN_SaveFile.SetPath('%s.wg.csv' % datetime.today().strftime('%Y%m%d_%H%M'))
    
    self.func_populate_plot_choices()
    self.func_populate_map_choices()
