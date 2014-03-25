# -*- coding: utf-8 -*-
"""

created: Sun Jan 26 08:53:54 2014
author:  Luke Gregor
"""

import wx
import numpy as np
from matplotlib import pylab as plt
from pandas import read_csv

def get_midx(self):

    licor_cmnd = self.data.licor_cmnd
    check_list = [['air_pump_off',      'atm'],
                  ['equil_pump_off',    'equ'],
                  ['span_pump_off',     'span'],
                  ['zero_pump_off',     'zero']]

    idx = np.zeros_like(licor_cmnd).astype(bool)
    for cmnd, box in check_list:
        box_obj = getattr(self, 'm_CH%s' % box )
        idx += (licor_cmnd == cmnd) * box_obj.GetValue()

    return idx


def update_m_params(self, event):

    if self.m_var.Selection == 0:
        self.trigger_m(False)
    else:
        m_choice = self.m_var.Items[self.m_var.Selection]
        self.trigger_m(True)
        if self.prettynames.has_key(m_choice):
           self.m_title.SetValue(self.prettynames[m_choice])
        else:
           self.m_title.SetValue(m_choice)

        m_dat = self.data[m_choice][self.get_midx()]
        m_lat = self.data.wg_latitude
        m_lon = self.data.wg_longitude

        self.m_cmin.SetValue(str(m_dat.min()))
        self.m_cmax.SetValue(str(m_dat.max()))

        self.func_update_mdates(None)

        self.m_south.SetValue(str(m_lat.min()))
        self.m_north.SetValue(str(m_lat.max()))
        self.m_west.SetValue(str(m_lon.min()))
        self.m_east.SetValue(str(m_lon.max()))

        self.trigger_m(True)


def func_update_mdates(self, event):

    minsteps = self.m_dmin.Value
    maxsteps = self.m_dmax.Value
    dn_min = self.m_datemin + self.m_slider_stepssize * minsteps
    dn_max = self.m_datemin + self.m_slider_stepssize * maxsteps

    if dn_min > dn_max:
        self.m_dmin.Value = self.m_dmax.Value
        self.m_dmax.Value = self.m_dmin.Value

    ds_min = plt.num2date(dn_min).strftime('%Y-%m-%d %H:%M')
    ds_max = plt.num2date(dn_max).strftime('%Y-%m-%d %H:%M')

    self.m_mindate_str.SetLabel(ds_min)
    self.m_maxdate_str.SetLabel(ds_max)


def func_m_global_limits(self, event):

    obj_list = [['north', '90'],
                ['south','-90'],
                ['east', '180'],
                ['west','-180']]

    for obj_str, val in obj_list:
        obj = getattr( self, 'm_%s' % obj_str )
        obj.SetValue(val)


def trigger_m(self, enable=True):

    obj_list = 'cmax cmin dmin dmax \
                cmaps title globrange\
                marker markersize \
                CHatm CHequ CHspan CHzero \
                north south east west \
                res coastlines rivers landfill'

    for obj_str in obj_list.split():
        obj = getattr( self, 'm_%s' % obj_str )
        obj.Enable(enable)

    self.BTN_m_plot.Enable(enable)


def func_populate_map_choices(self):

    self.prettynames = dict(read_csv('./doc/pretty_names.txt').values)

    maplist = []
    for col in self.data.keys():
        if self.data[col].dtype == np.float64:
            maplist.append(col)
    maplist.insert(0, 'Choose a variable')

    self.m_var.SetItems(maplist)
    self.m_var.SetSelection(0)

    self.m_cmaps_list = 'bone gray hot jet Spectral_r RdBu_r PRGn_r'.split()
    self.m_cmaps.Append( "./images/colormaps/bone.bmp".partition(":")[2], wx.Image.ConvertToBitmap(wx.Image("./images/colormaps/bone.bmp".partition(":")[0])));
    self.m_cmaps.Append( "./images/colormaps/gray.bmp".partition(":")[2], wx.Image.ConvertToBitmap(wx.Image("./images/colormaps/gray.bmp".partition(":")[0])));
    self.m_cmaps.Append( "./images/colormaps/hot.bmp".partition(":")[2], wx.Image.ConvertToBitmap(wx.Image("./images/colormaps/hot.bmp".partition(":")[0])));
    self.m_cmaps.Append( "./images/colormaps/jet.bmp".partition(":")[2], wx.Image.ConvertToBitmap(wx.Image("./images/colormaps/jet.bmp".partition(":")[0])));
    self.m_cmaps.Append( "./images/colormaps/Spectral_r.bmp".partition(":")[2], wx.Image.ConvertToBitmap(wx.Image("./images/colormaps/Spectral_r.bmp".partition(":")[0])));
    self.m_cmaps.Append( "./images/colormaps/RdBu_r.bmp".partition(":")[2], wx.Image.ConvertToBitmap(wx.Image("./images/colormaps/RdBu_r.bmp".partition(":")[0])));
    self.m_cmaps.Append( "./images/colormaps/PRGn_r.bmp".partition(":")[2], wx.Image.ConvertToBitmap(wx.Image(u"./images/colormaps/PRGn_r.bmp".partition(":")[0])));
    self.m_cmaps.Select(3)

    dn_data = self.data.wg_datenum
    dn_range = dn_data.max() - dn_data.min()
    self.m_datemin = dn_data.min()
    self.m_slider_stepssize = dn_range / self.m_dmin.Max - self.m_dmin.Min


def get_map_properties(self):

    selfattr = lambda s: getattr(self, 'm_%s' % s)
    selfselection = lambda s: selfattr(s).Items[selfattr(s).Selection]
    arr = lambda d: np.array(d)
    
    prop = {}
    flt_key = 'cmax cmin north south east west markersize'.split()
    str_key = 'title'.split()
    sln_key = 'marker var res'.split()
    cmp_key = 'cmaps'.split()
    bol_key = 'coastlines rivers landfill'.split()
    flt_val = arr([selfattr(s).Value     for s in flt_key]).astype(float)
    sln_val = arr([selfselection(s)      for s in sln_key])
    cmp_val = arr([selfattr(s).GetSelection() for s in cmp_key])
    str_val = arr([selfattr(s).Label     for s in str_key])
    bol_val = arr([selfattr(s).Value     for s in bol_key]).astype(bool)
    
    print cmp_val
    
    prop.update(zip(flt_key, flt_val))
    prop.update(zip(sln_key, sln_val))
    prop.update(zip(cmp_key, cmp_val))
    prop.update(zip(str_key, str_val))
    prop.update(zip(bol_key, bol_val))

    prop['marker'] = prop['marker'][0]
    prop['cmap'] = self.m_cmaps_list[prop.pop('cmaps')]

    prop['dmin'] = self.m_datemin + self.m_slider_stepssize * self.m_dmin.Value
    prop['dmax'] = self.m_datemin + self.m_slider_stepssize * self.m_dmax.Value

    return prop