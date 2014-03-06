# -*- coding: utf-8 -*-
"""
This file contains two functions to calculate xCO2

Calculate xCO2 from Licor data
created: Tue Jan 14 21:06:52 2014
author:  Luke Gregor
"""

import numpy as np
exp = np.exp
log = np.log

def calc_xco2_raw(raw1, raw2, temp, pres, coeff_zero, coeff_span):
    """xCO2 from raw voltages (calc_xco2_raw)
    --------------------------------------
    Calculates the mole fraction of CO2 (xCO2) from the raw voltage
    measurements made by the Wave Glider's Licor unit. This script
    has been adapted from the Uni Washington's VB script.
    """

    xCO2 = np.ndarray(pres.shape)
    P = np.ndarray(pres.shape)
    g = np.ndarray(pres.shape)

    xCO2[pres == 0] = np.NaN

    C = np.array([439.7123, 1255.133, 27189.37, -160374.6, 570291, -604330.8])
    a =  1.10158
    b = -0.00612178
    c = -0.266278
    d =  3.69895
    z =  0.5

    t =     temp
    t_std = 50
    p1 =    pres
    p0 =    99
    v =     raw1
    vo =    raw2

    # p1 is the measured pressure
    # po is std pressure, po = 99
    # p is the ratio of the std pressure and measured press
    P[p1 < p0] = p0 / p1[p1 < p0]
    P[p1 > p0] = p1[p1 > p0] / p0
    P[p1 == p0]= p1[p1 == p0]

    absp = (1 - ((v / vo) * coeff_zero)) * coeff_span

    # g is the empirical correction function and is a function of
    # absorptance and pressure
    a_1 = (1 / (a * (P - 1)))
    b_1 = 1 / ((1 / (b + (c * P)) + d))
    x = 1 + (1 / (a_1 + (b_1 * ((1 / (z - absp)) - (1 / z)))))
    g[p1 ==p0] = 1.
    g[p1 < p0] = x[p1 < p0]
    g[p1 > p0] = 1./x[p1 > p0]

    # s is the pressure corrected absorptance and
    # equal absorptance(absp) * correction (g)
    s = absp * g
    S = np.array([s**p for p in range(1,7)])

    # 'f is the calibration polynomial
    f = np.sum(C[:,np.newaxis] * S, axis=0)

    xCO2_raw = 10 * f * ((t + 273) / (t_std + 273))

    return xCO2_raw.round(3)


def calc_xco2_dry(xco2_raw, pres, rh_temp, rh_equil, rh_span):
    """Dry xCO2 (calc_xco2_dry)
    ------------------------
    Applies a correction for relative humidity to the mole fraction of CO2 (xCO2).
    The output is saved as licor_xco2_dry_sw

    The saturation vapour pressure of water is calculated for the Licor. The
    relative vapour pressure is then calculated by getting the difference in
    relative humidity for seawater samples and span samples. xCO2 is divided
    by this factor.

    This script is based on the VB script by Uni Washington.
    """

    satvapres = 0.61365 * exp((17.502 * rh_temp) / (240.97 + rh_temp))
    vaporpres = (rh_equil - rh_span) * satvapres/ 100.

    xco2_dry = xco2_raw / ((pres - vaporpres) / pres)

    return xco2_dry.round(3)


def calc_pco2(xco2_dry, TempC_equ, Salt, TempC_sea):
    """Calculate pCO2 (calc_pco2)
    --------------------------
    Accounts for the water vapour pressure in a sample of air and calculates
    pCO2 at seawater temperature.

    When measuring CO2 it is assumed that it is measured at 100% relative
    humidity (RH) or saturated vapour pressure (VP). However, we measure
    CO2 at a certain RH and calculate the dry mole fraction from this. This
    function calculatees the vapour pressure factor which is multilplied with
    dry xCO2 to get pCO2.

    Finally the pCO2 is corrected for equilibrator vs seawater temperatures
    using the relationship determined in Takahashi (1993).Here the Prawler CTD
    temperature is used in conjunction with the Licor equilibrator temperature.

    This script is based on the CO2SYS script originally by Lewis and Wallace
    1998. Weiss and Price (1980) in Marine Chemistry referenced by CO2SYS. If
    you'd like to calculate pCO2 from any xCO2 (not necessarily dry) it is the
    product of the pressure in the measureing chamber and xCO2.
    """

    #~ # Vapor pressure is calculated using the MIT's seawater package available at:
    #~ #    http://web.mit.edu/seawater/
    #~ # This is different to the methods defined by the CO2SYS script, but is in 
    #~ # accordance with the "Guide to best practices for ocean CO2 measurements".
    #~ def vapres_seawater(S, T):
        #~ # convert to Kelvin if needed
        #~ if T < 250:
            #~ T = T + 273.15
        #~ # coefficients
        #~ a = [-5.8002206E+03,  1.3914993E+00,
             #~ -4.8640239E-02,  4.1764768E-05,
             #~ -1.4452093E-08,  6.5459673E+00]
        #~ # equation
        #~ Pv_w = exp((a[0]/T) + a[1] + a[2]*T + a[3]*T**2 + a[4]*T**3 + a[5]*log(T))
        #~ Pv   = Pv_w  / (1. + 0.57357 * (S / (1000.-S)))
        #~ return Pv
    #~ VapPres_SW = vapres_seawater( Salt, TempC_equ ) * 1e-6
    #~ VPFac_MIT = 1. - VapPres_SW
    
    
    VPWP = exp(24.4543 - 67.4509 *(100. /(TempC_equ+ 273.15)) - 4.8489 *log((TempC_equ+ 273.15)/100.))
    VPCorrWP = exp(-0.000544 *Salt)
    VPSWWP = VPWP * VPCorrWP
    VPFac_CO2SYS = 1. - VPSWWP
    
    pco2_equ = xco2_dry * VPFac_CO2SYS
    pco2_sea = pco2_equ * exp(0.0423 * (TempC_sea - TempC_equ) )

    return pco2_equ.round(3), pco2_sea.round(3)


def calc_fco2(pco2, tempC):
    """Fugacity of CO2 (calc_fco2)
    ---------------------------
    This script calculates the fugacity of CO2. This script is based on the
    Fugacity Factor calculation in the CO2SYS script originally by Lewis
    and Wallace 1998.
    Requires pCO2 and temperature in degC for inputs.

    The fugacity of CO2 is calculating by finding the Fugacity Factor.
    This is based on Weiss, R. F., Marine Chemistry 2:203-215, 1974.
    """

    # CalculateFugacityConstants:
    # This assumes that the pressure is at one atmosphere, or close to it.
    # Otherwise, the Pres term in the exponent affects the results.
    #       Weiss, R. F., Marine Chemistry 2:203-215, 1974.
    #       Delta and B in cm3/mol

    tempK = tempC + 273.15
    RT = 83.1451 * tempK

    Delta = (57.7 - 0.118*tempK)

    b = -1636.75 \
        + 12.0408 * tempK \
        - 0.0327957 * tempK**2 \
        + 3.16528 * 0.00001 * tempK**3

    # For a mixture of CO2 and air at 1 atm (at low CO2 concentrations);
    P1atm = 1.01325
    fugfac = np.exp((b + 2 * Delta) * P1atm / RT)
    # GEOSECS and Peng assume pCO2 = fCO2, or FugFac = 1
    # FugFac(F) = 1

    fco2 = pco2 * fugfac

    return fco2.round(3)


if __name__ == "__main__":

    a, b, c = calc_pco2( 237.9585, 10, 35, 0)
    print calc_fco2( b, 10)
