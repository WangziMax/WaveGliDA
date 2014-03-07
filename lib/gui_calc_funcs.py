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

    self.StatusBar.SetStatusText('calculating CO2 parameters...')
    
    if 'licor_pco2_sea' in self.data.keys():
        return None
    
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
    pco2_equ = Series(None, index=self.data.index)
    pco2 = Series(None, index=self.data.index)
    pco2_equ, pco2 = calc_pco2(licor_xco2dry, licor_temp, prwl_salt, prwl_temp)
    pco2_atm = np.array(pco2)[iatm].repeat(10)
    pco2_sea = np.array(pco2)[iequ].repeat(10)

    # Calculate fCO2
    fco2 = Series(None, index=self.data.index)
    fco2 = calc_fco2(pco2, prwl_temp)
    fco2_atm = np.array(fco2)[iatm].repeat(10)
    fco2_sea = np.array(fco2)[iequ].repeat(10)
    
    # Calculate delta fco2
    dfco2 = fco2_sea - fco2_atm
    
    i = np.where([key.startswith('licor') for key in self.data.keys()])[0].max() + 1
    
    self.data.insert(i,   'licor_xco2dry', licor_xco2dry)
    self.data.insert(i+1, 'licor_pco2_equ', pco2_equ)
    self.data.insert(i+2, 'licor_pco2_atm', pco2_atm)
    self.data.insert(i+3, 'licor_pco2_sea', pco2_sea)
    self.data.insert(i+4, 'licor_fco2_atm', fco2_atm)
    self.data.insert(i+5, 'licor_fco2_sea', fco2_sea)
    self.data.insert(i+6, 'licor_dfco2', dfco2)
    self.StatusBar.SetStatusText('')
    
    
