# -*- coding: utf-8 -*-
"""

created: Sat Jan 18 22:41:29 2014
author:  Luke Gregor
"""
import numpy as np
import pylab as plt
from pandas import DataFrame


def read_licor(lines):
    """
    Reads a block of licor data from waveglider raw files.
    This contains the following variables:
        temperature [C]             -   temp_degC
        licor pressure [kPa]        -   licor_pres
        xCO2 [um/mm]                -   xco2_ummm
        oxygen saturation [%]       -   o2_sat
        relative humidity [%]       -   rel_hum

    created: 2014-01-08
    author:  Luke Gregor
    """

    dat = {}

    while not lines[0]:
        lines.pop(0)
    glider = np.array(lines[0].split())                          # WAVEGLIDER INFO
    gps_data = lines[1].split()                                  # GPS DATA
    diagnost = np.array(lines[2].split())[:4]                    # DIAGNOSTICS
    co2calc = np.array(lines[-1].split())[[1, 3]].astype(float)  # CO2 CALCULATION
    co2calc = np.array(co2calc, ndmin=2).repeat(10, axis=0)

    try:
        cycles = np.array(map(str.split, lines[3:-1])).astype(float)
    except:
        # Items are not space seperated, but rather index based. IDX = new item idx
        cycles = np.ndarray([10, 17])
        IDX = [0,3,9,15,22,28,36,42,48,52,55,59,64,69,78,84,93,99]
        for i, line in enumerate(lines[3:-1]):
            for j in range(len(IDX)-1):
                cycles[i, j] = line[ IDX[j] : IDX[j+1]].strip()

    # SORTING OUT TIMES (1440 = mins in a day)
    dat['wg_datenum'] = plt.datestr2num(' '.join(glider[3:5]))
    dat['wg_datenum'] = dat['wg_datenum'] + (cycles[:,0]-cycles[0,0]) / 1440
    # the following two lines deal with sampling that crosses the hour mark
    idx = dat['wg_datenum'] < dat['wg_datenum'][0]
    dat['wg_datenum'][idx] = dat['wg_datenum'][idx] + (1./24)
    dat['wg_datetime'] = plt.num2date(dat['wg_datenum'])

    # LATITUDES AND LONGITUDES
    dat['wg_latitude']  = convert_coords(gps_data[2], gps_data[3])
    dat['wg_longitude'] = convert_coords(gps_data[4], gps_data[5])

    # COMMANDS          PUMP ON          PUMP OFF         CALIBRATION
    dat['licor_cmnd'] = [
                     'zero_pump_on',  'zero_pump_off', 'zero_post_cal',
                     'span_pump_on',  'span_pump_off', 'span_post_cal',
                     'equil_pump_on', 'equil_pump_off',
                     'air_pump_on',   'air_pump_off']
    # GLIDER INFO
    glider_hdr =    ['licor_cycle',
                     'licor_x1',        'licor_x2',
                     'wg_date',          'wg_time',
                     'wg_location',      'wg_unit']
    # DIAGNOSTIC DATA
    diagnost_hdr =  ['wg_battery_logic',        # 0
                     'wg_battery_transmitter',  # 1
                     'licor_zero_coeff',        # 2
                     'licor_span_coeff']        # 3
    # CYCLES       VARIABLE           STANDARD DEVIATION
    cycles_hdr =    ['licor_minutes',                       # min
                     'licor_temp',    'licor_tempstd',      # deg C
                     'licor_pres',    'licor_pressstd',     # kPa
                     'licor_xco2',    'licor_xco2std',      # ppm
                     'licor_o2sat',   'licor_o2std',        # %
                     'licor_RH',      'licor_RHstd',        # %
                     'licor_RH_temp', 'licor_RH_tempstd',   # deg C
                     'licor_raw1',    'licor_raw1std',
                     'licor_raw2',    'licor_raw2std']
    # CO2_MEAS      ATMOSPHERIC             SEAWATER
    co2calc_hdr = ['licor_sw_xco2_dry',     'licor_atm_xco2_dry']


    # Turn the arrays into a dictionary
    dat.update( zip( glider_hdr, glider.T))
    dat.update( zip( diagnost_hdr, diagnost.T))
    dat.update( zip( cycles_hdr, cycles.T))
    dat.update( zip( co2calc_hdr, co2calc.T))

    # some boring number formatting
    dat['licor_zero_coeff'] = float(dat['licor_zero_coeff'])
    dat['licor_span_coeff'] = float(dat['licor_span_coeff'])

    # Create a pandas.DataFrame from the dictionary
    # This fills each key to have as many items as the index = 10
    dat = DataFrame(dat, index=range(10))

    return dat.to_dict(outtype='list')


def read_prawler(lines):
    """
    Reads Prawler CTD data found on the Liquid Robotics wave gliders.

    created: Wed Jan 08 22:12:19 2014
    author:  Luke Gregor
    """


    data = np.array([s[:-1].strip().split(',') for s in lines[1:-1]]).astype(float)
    head = ['prwl_pres', 'prwl_temp', 'prwl_cond']

    dat = {}
    dat.update(zip( head, data.T))
    # Create a pandas.DataFrame from the dictionary
    # This fills each key to have as many items as the index = 10
    dat = DataFrame(dat, index=range(10))

    return dat.to_dict(outtype='list')


def read_durafet(lines):

    data = np.array(lines[1].split(), ndmin=2).repeat(10, 0)
    
    data_str = data[:, :2]
    data_flt = data[:, 2:].astype(float)
    head_str = ['duft_date',        'duft_time']
    head_flt = ['duft_battery',
                'duft_unknown',
                'duft_fet_intV',    'duft_fet_extV',
                'duft_pHV',
                'duft_ctrl_temp',
                'duft_presV']

    dat = {}
    dat.update( zip( head_flt, data_flt.T))
    dat.update( zip( head_str, data_str.T))
    # Create a pandas.DataFrame from the dictionary
    # This fills each key to have as many items as the index = 10
    dat = DataFrame(dat, index=range(10))
    
    return dat.to_dict(outtype='list')


def read_sbe63(lines):

    data = np.array(lines[1].split()).astype(float)
    head = ["sb63_phase",           "sbe63_phase_stdev",
            "sbe63_thermistorV",    "sbe63_thermistorV_stdev",
            "sbe63_oxygen",         "sbe63_oxygen_stdev",
            "sbe63_temp",           "sbe63_temp_stdev",
            "sbe63_unknown"]
    
    dat = {}
    dat.update( zip( head, data.T))
    # Create a pandas.DataFrame from the dictionary
    # This fills each key to have as many items as the index = 10
    dat = DataFrame(dat, index=range(10))
    
    return dat.to_dict(outtype='list')


def convert_coords(coordinate_str, hemisphere):
    """
    The coordinates in the SDS system are given as
    degMM.mm (degree - 2 or three intigers, decimal minute)
    hemisphere is given by N/S E/W (+/-). This function
    returns +-decimal degrees depending on hemisphere
    """

    coordinate = np.float(coordinate_str)
    degrees = np.floor(coordinate/100.)
    minutes = coordinate - degrees*100.
    decmins = minutes / 60.
    degsdec = degrees + decmins

    if (hemisphere == 'S') | (hemisphere == 'W'):
        return -degsdec
    else:
        return degsdec

