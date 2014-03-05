# -*- coding: utf-8 -*-
"""
Wave Glider Data Analysis
=========================
version: 0.2
created: 26 Jan 2014
author:  Luke Gregor

TO DO
-----
Important
    pco2 calculations
    help for the maps
Nice but not NB
    glider speed
    more file types to support
    a list of standard plots for xyplots
"""
from matplotlib import use as mpl_use
mpl_use('WXAgg')

import sys
import wx
import lib
import numpy as np
from lib.gui_main import Frame_MAIN

def main():
    import os
    path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(path)
    app = wx.App(0)
    frame = WavGliDaPro(None)

    frame.init()

    frame.Show()
    app.MainLoop()


class WavGliDaPro(Frame_MAIN):


    from lib.gui_help_funcs import func_update_help
    from lib.gui_file_funcs import func_listfiles, func_update_checkbox, func_loaddata, \
         func_read_selected, func_populate_datagrid, func_savedata, func_select_files
    from lib.gui_calc_funcs import func_calc_salt, func_calc_co2
    from lib.gui_plot_funcs import func_populate_plot_choices, update_x_params, get_yidx,\
         update_y1_params, update_y2_params, update_ylims, func_plotxy, update_xlims, \
         enable_y_properties, enable_plot_button, get_plot_properties
    from lib.plot_draw import func_plotxy
    from lib.gui_map_funcs import get_midx, update_m_params, func_update_mdates, \
         trigger_m, func_populate_map_choices, get_map_properties, func_m_global_limits
    from lib.map_draw import func_plot_map


    def init(self):
        
        # HELP FILES
        self.help_list = np.array([['About WavGliDA',        'About'],
                                   ['Reading Files',         'ReadingFiles'],
                                   ['Saving and Loading',    'SavingReading'],
                                   ['Plotting',              'Plotting'],
                                   ['CO2 Calculations',      'CO2calculations'],
                                   ]).T
        self.DirSelector.GetChildren( )[0].SetLabel('Load multiple raw files from a directory')
        self.BTN_LoadFile.GetChildren()[0].SetLabel('Load previously saved file')
        self.BTN_SaveFile.GetChildren()[0].SetLabel('Save data as *.csv')
        
        lib.list_2_ListBox(self.LB_HELP, self.help_list)

        
        # SET FONTS
        if sys.platform.startswith('win'):
            font_sansserif = "Broadway"
            size_sansserif = 9
            font_monospace = "Lucida Console"
            size_monospace = 9
        elif sys.platform.startswith('darwin'):
            font_monospace = "Lucida Console"
            size_monospace = 9
        else:
            pass
        self.LB_Files.SetFont(     wx.Font( size_monospace, 74, 90, 90, False, font_monospace ) )
        self.TXT_HELP.SetFont(     wx.Font( size_monospace, 74, 90, 90, False, font_monospace ) )
        self.LB_Files.SetFont(     wx.Font( size_monospace, 74, 90, 90, False, font_monospace ) )
        self.TC_FileStatus.SetFont(wx.Font( size_monospace, 74, 90, 90, False, font_monospace ) )
        self.LB_HELP.SetFont(      wx.Font( size_monospace, 74, 90, 90, False, font_monospace ) )
    

if __name__ == "__main__":

    main()
