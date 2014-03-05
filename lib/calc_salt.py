# -*- coding: utf-8 -*-
"""

created: Sun Jan 19 10:06:25 2014
author:  Luke Gregor
"""

# -*- coding: utf-8 -*-

import numpy as np

def salinity_srl(cond, T_90, P):
    """
    Calculates salinity from the a prawler CTD found on wavegliders made by
    Liquid Robitics. This code was copied from the VB code made by LiqRob.

    created:    2013-01-18
    author:     Luke Gregor
    """

    A1 =  0.0000207
    A2 = -0.000000000637
    A3 =  3.989E-15
    B1 =  0.03426
    B2 =  0.0004464
    B3 =  0.4215
    B4 = -0.003107
    C0 =  0.6766097
    C1 =  0.0200564
    C2 =  0.0001104259
    C3 = -0.00000069698
    C4 =  0.0000000010031

    a = [  0.008,
          -0.1692,
          25.3851,
          14.0941,
          -7.0261,
           2.7081]

    b = [  0.0005,
          -0.0056,
          -0.0066,
          -0.0375,
           0.0636,
          -0.0144]


    if (cond <= 0):
        return 0
    else:
        # convert Siemens/meter to mmhos/cm
        C = cond * 10
        # Convert its-90 to its-68
        # ITS68 = ITS90 * 1.00024
        t = T_90 * 1.00024
        R = C / 42.914
        val = 1 + (B1 * t) + (B2 * t * t) + (B3 * R) + (B4 * R * t)
        if val:
            RP = 1 + ((P * (A1 + P * (A2 + P * A3))) / val)
            val = RP * (C0 + (t * (C1 + t * (C2 + t * (C3 + t * C4)))))

            RT = R / val

        if RT <= 0:
            RT = 0.000001

        sum1, sum2 = 0, 0
        for i in range(6):
            temp = RT ** (i / 2.)
            # sum1 += a[i] * temp
            sum1 += a[i] * temp
            #  sum2 += b[i] * temp
            sum2 += b[i] * temp

        val = 1 + (0.0162 * (t - 15))
        if val:
            salinity = sum1 + (sum2 * (t - 15) / val)
        else:
            salinity = -99

        return salinity


def salinity_vec(cond, T_90, P):
    """
    Calculates salinity from the a prawler CTD found on wavegliders made by
    Liquid Robitics. This code was copied from the VB code made by LiqRob.

    created:    2013-01-18
    author:     Luke Gregor
    """

    salt = map(salinity_srl, cond, T_90, P)
    salt = np.array(salt)

    return salt


if __name__ == "__main__":

    print 'TESTING wg_salinity'

    temp, cond = 12.3172, 3.95357

    print 'Input:'
    print '   T = %.4f' % temp
    print '   C = %.4f' % cond
    print 'Output:'
    print '   S = %.4f' % salinity_srl(cond, temp, 0)