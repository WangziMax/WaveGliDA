# -*- coding: utf-8 -*-
"""

created: Sun Jan 26 09:22:17 2014
author:  Luke Gregor
"""
from matplotlib import pylab as plt
import numpy as np


def func_plotxy(self, event):

    def get_axis_data(self, axis=1):
        axis_int = axis
        axis = 'y%d' % axis
        y = self.data[prop[axis].pop('var')]
        x = self.data[prop['x']['var']]

        idx = self.get_yidx(axis=axis_int)* \
                (x >= prop['x'] ['min'])  * \
                (x <= prop['x'] ['max'])  * \
                (y >= prop[axis]['min'])  * \
                (y <= prop[axis]['max'])

        x = np.array( x [ idx ] )
        y = np.array( y [ idx ] )
        return x, y, prop

    prop = self.get_plot_properties()
    if not prop:
        return None

    x1, y1, prop = get_axis_data(self, axis=1)

    x_lims  = prop['x']['min'], prop['x']['max']
    y1_lims = prop['y1'].pop('min'), prop['y1'].pop('max')

    plt.figure()

    if prop['x']['var'] == 'wg_datenum':
        plt.plot_date(x1, y1, **prop['y1'])
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.2)
    else:
        plt.plot(x1, y1, **prop['y1'])

    plt.xlim(x_lims)
    plt.ylim(y1_lims)
    plt.ylabel(prop['y1']['label'], color=prop['y1']['color'], size=14)
    plt.yticks(color=prop['y1']['color'])

    if prop.has_key('y2'):
        x2, y2, prop = get_axis_data(self, axis=2)

        x_lims  = prop['x']. pop('min'), prop['x']. pop('max')
        y2_lims = prop['y2'].pop('min'), prop['y2'].pop('max')

        plt.twinx()
        if prop['x']['var'] == 'wg_datenum':
            plt.plot_date(x2, y2, **prop['y2'])
        else:
            plt.plot(x2, y2, **prop['y2'])

        plt.xlim(x_lims)
        plt.ylim(y2_lims)
        plt.ylabel(prop['y2']['label'], color=prop['y2']['color'], size=14)
        plt.yticks(color=prop['y2']['color'])

    plt.title(self.xy_title.GetValue())

    plt.show()