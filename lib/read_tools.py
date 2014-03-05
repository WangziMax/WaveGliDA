# -*- coding: utf-8 -*-
"""

created: Sat Jan 18 22:41:29 2014
author:  Luke Gregor
"""

from numpy import float, floor

def convert_coords(coordinate_str, hemisphere):
    """
    The coordinates in the SDS system are given as
    degMM.mm (degree - 2 or three intigers, decimal minute)
    hemisphere is given by N/S E/W (+/-). This function
    returns +-decimal degrees depending on hemisphere
    """

    coordinate = float(coordinate_str)
    degrees = floor(coordinate/100.)
    minutes = coordinate - degrees*100.
    decmins = minutes / 60.
    degsdec = degrees + decmins

    if (hemisphere == 'S') | (hemisphere == 'W'):
        return -degsdec
    else:
        return degsdec

