# -*- coding: utf-8 -*-
__version__ = 0.6

from matplotlib import use as mpl_use
mpl_use('WXAgg')

import sys
import wx
import lib
import numpy as np
from lib.gui__MAIN import Frame_MAIN
from matplotlib import rcParams
rcParams['mathtext.default'] = 'sf'

def main():
    import os
    path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(path)
    app = wx.App(1)
    frame = WavGliDaPro(None)

    frame.init()

    frame.Show()
    app.MainLoop()


class WavGliDaPro(Frame_MAIN):


    from lib.gui_0_help         import  func_update_help
    from lib.gui_1_import       import  func_listfiles, func_update_checkbox, func_loaddata, \
                                        func_read_selected, func_select_files, update_weather_stn
    from lib.gui_2_view_save    import  func_export_opts, func_populate_datagrid, func_savedata
    from lib.gui_3_line_plots   import  func_populate_plot_choices, update_x_params, get_yidx, func_plotxy,\
                                        update_y1_params, update_y2_params, update_ylims, update_xlims, \
                                        enable_y_properties, enable_plot_button, get_plot_properties
    from lib.gui_4_map          import  get_midx, update_m_params, func_update_mdates, trigger_m, \
                                        func_populate_map_choices, get_map_properties, \
                                        func_m_global_limits, func_plot_map
    from lib.gui_tools          import  clear_status_text, list_2_ListBox
    from lib.gui_calcs          import  func_calc_salt, func_calc_co2, convert_oxygen
    from lib.read_weather       import  read_weather_file, get_weather


    def init(self):
        
        self.StatusBar.SetStatusText('Load data by selecting files using the buttons above')
        
        # HELP FILES
        self.help_list = np.array([['About WavGliDA',        'About'],
                                   ['Changes Log',           'ChangeLog'],
                                   ['Reading Files',         'ReadingFiles'],
                                   ['Saving and Loading',    'SavingReading'],
                                   ['Plotting',              'Plotting'],
                                   ['CO2 Calculations',      'CO2calculations'],
                                   ]).T
        
        self.list_2_ListBox(self.LB_HELP, self.help_list)

        
        # SET FONTS
        if sys.platform.startswith('win'):
            font_monospace = "Lucida Sans Typewriter"
            size_monospace = 9
        elif sys.platform.startswith('darwin'):
            font_monospace = "Monaco"
            size_monospace = 10
        elif sys.platform.startswith('lin'):
            font_monospace = "Monospace"
            size_monospace = 10
        
        self.LB_Files.SetFont(      wx.Font( size_monospace, 74, 90, 90, False, font_monospace ) )
        self.TXT_HELP.SetFont(      wx.Font( size_monospace, 74, 90, 90, False, font_monospace ) )
        self.LB_Files.SetFont(      wx.Font( size_monospace, 74, 90, 90, False, font_monospace ) )
        self.TC_FileStatus.SetFont( wx.Font( size_monospace, 74, 90, 90, False, font_monospace ) )
        self.LB_HELP.SetFont(       wx.Font( size_monospace, 74, 90, 90, False, font_monospace ) )
        self.TC_weather_stn.SetFont(wx.Font( size_monospace, 74, 90, 90, False, font_monospace ) )
        self.GridData.SetDefaultCellFont(wx.Font( size_monospace-1, 74, 90, 90, False, font_monospace ) )
        
        self.StatusBar.SetFont(wx.Font( 13, 74, 90, 90, False, wx.EmptyString ) )
        
        if sys.platform.startswith('darwin') | sys.platform.startswith('win'):
            self.DirSelector.GetChildren( )[0].SetLabel('Load raw files from a directory')
            self.BTN_LoadFile.GetChildren()[0].SetLabel('Load previously saved file')
            self.FP_weather_stn.GetChildren()[0].SetLabel('Select weather station file')
        self.BTN_SaveFile.GetChildren()[0].SetLabel('Save data as *.csv')
        
        
if __name__ == "__main__":

    main()
