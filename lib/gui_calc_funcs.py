# -*- coding: utf-8 -*-
"""

created: Sun Jan 26 11:31:16 2014
author:  Luke Gregor
"""

from gui_tools import pdDataFrame_2_numpy
from calc_salt import salinity_vec as calc_salt
import numpy as np
from pandas import Series
import wx


def func_calc_salt( self, event ):
    if hasattr(self.data, 'prwl_salt'):
        pass
    else:
        self.StatusBar.SetStatusText('calculating salinity...')
        i = np.where([key.startswith('prwl') for key in self.data.keys()])[0].max() + 1
        
        salt = Series(None, index=self.data.index)
        salt = calc_salt(self.data.prwl_cond,
                         self.data.prwl_temp,
                         np.zeros_like(self.data.prwl_cond))
        self.data.insert(i, 'prwl_salt', salt)
        self.StatusBar.SetStatusText('')

def func_calc_co2( self, event ):

    #~ info_str = ("Sadly this button does nothing."
                #~ "\nIn the future this button will calculate pCO2, fCO2 and FCO2")
    #~ dlg = wx.MessageDialog(self, info_str,'Under Construction', wx.ICON_INFORMATION)
    #~ dlg.ShowModal()
    #~ dlg.Destroy()


    from calc_co2 import calc_xco2_dry, calc_pco2, calc_fco2

    col_names = ('licor_xco2', 'licor_pres', 'licor_RH_temp', 'licor_RH',
                 'licor_temp', 'licor_cmnd', 'prwl_temp', 'prwl_salt')
                 
    # this step is NB as variables need to be numpy arrays NOT DataFrame
    col_dict = pdDataFrame_2_numpy(self.data, col_names)
    globals().update(col_dict)
    
    iequ = 'equil_pump_off' == licor_cmnd
    iatm = 'air_pump_off' == licor_cmnd
    ispn = 'span_pump_off' == licor_cmnd

    # Calculate dry xCO2 for equilibrator
    licor_xco2dry = Series(None, index=self.data.index)
    licor_xco2dry[iequ] = calc_xco2_dry(licor_xco2 [iequ],
                                        licor_pres [iequ],
                                        licor_RH_temp [iequ],
                                        licor_RH [iequ],
                                        licor_RH [ispn])
    # Calculate dry xCO2 for atmosphere
    licor_xco2dry[iatm] = calc_xco2_dry(licor_xco2 [iatm],
                                        licor_pres [iatm],
                                        licor_RH_temp [iatm],
                                        licor_RH [iatm],
                                        licor_RH [ispn])
    # Calculate pCO2
    licor_pco2 = Series(None, index=self.data.index)
    licor_pco2 = calc_pco2(licor_xco2dry,
                           licor_temp,
                           prwl_salt,
                           prwl_temp)

    # Calculate fCO2
    licor_fco2 = Series(None, index=self.data.index)
    licor_fco2 = calc_fco2(licor_pco2, prwl_temp)

    
    i = np.where([key.startswith('licor') for key in self.data.keys()])[0].max() + 1
    self.data.insert(i,   'licor_xco2dry', licor_xco2dry)
    self.data.insert(i+1, 'licor_pco2', licor_pco2)
    self.data.insert(i+2, 'licor_fco2', licor_fco2)
    self.StatusBar.SetStatusText('')
    
    self.BTN_calcCO2.SetLabel('CO2 parameters have been calculated')
    self.BTN_calcCO2.Enable(False)
    self.GridData.Scroll(1e3, 0)

