# -*- coding: utf-8 -*-
"""

created: Mon Jan 20 16:38:53 2014
author:  Luke Gregor
"""

import wx
import numpy as np
from pandas import read_csv
from matplotlib import pylab as plt


def func_populate_plot_choices(self):

    self.prettynames = dict(read_csv('./doc/pretty_names.txt').values)

    self.x_var.SetItems(['Choose a variable','wg_latitude','wg_longitude','wg_datenum'])

    y1list = []
    y2list = []
    for col in self.data.keys():
        if self.data[col].dtype == np.float64:
            y1list.append(col)
            y2list.append(col)

    y1list.insert (0, 'Choose a variable')
    y2list.insert (0, 'No second Y-axis')

    self.y1_var.SetItems(y1list)
    self.y2_var.SetItems(y2list)

    self.x_var.SetSelection(0)
    self.y1_var.SetSelection(0)
    self.y2_var.SetSelection(0)

    self.update_y1_params(None)
    self.update_y2_params(None)


def update_x_params(self, event):

    x_choice = self.x_var.GetItems()[self.x_var.GetSelection()]

    if self.x_var.GetSelection() == 0:
        self.y1_var.SetSelection(0)
        self.y2_var.SetSelection(0)
        self.update_y1_params(None)
        self.update_y2_params(None)
    else:
        self.x_label.SetValue(self.prettynames[x_choice])
        self.x_minslide.Enable()
        self.x_maxslide.Enable()
        self.x_minslide.SetValue(0)
        self.x_maxslide.SetValue(100)

        x_data = self.data[x_choice]
        x_range = x_data.max() - x_data.min()
        self.x_slider_min = x_data.min()
        self.x_slider_stepssize = x_range / self.x_maxslide.Max - self.x_minslide.Min
        self.update_xlims(None)
        self.y1_var.Enable()

    self.enable_plot_button()


def update_y1_params(self, event):

    if self.y1_var.GetSelection() == 0:
        self.y2_var.SetSelection(0)
        self.y2_var.Disable()
        self.update_y2_params(None)
        self.enable_y_properties(False, 1)
    else:
        y_choice = self.y1_var.GetItems()[self.y1_var.GetSelection()]
        self.enable_y_properties(True, 1)
        if self.prettynames.has_key(y_choice):
           self.y1_label.SetValue(self.prettynames[y_choice])
        else:
           self.y1_label.SetValue(y_choice)

        self.update_ylims(axis=1)
        self.y2_var.Enable()

    self.enable_plot_button()


def update_y2_params(self, event):
    if self.y1_var.GetSelection() == 0:
        self.enable_y_properties(False, 2)
    elif self.y2_var.Selection ==0:
        self.enable_y_properties(False, 2)
    else:
        y_choice = self.y2_var.GetItems()[self.y2_var.GetSelection()]
        self.enable_y_properties(True, 2)
        if self.prettynames.has_key(y_choice):
           self.y2_label.SetValue(self.prettynames[y_choice])
        else:
           self.y2_label.SetValue(y_choice)
        self.update_ylims(axis=2)

    self.enable_plot_button()


def update_xlims(self, event):

    minsteps = self.x_minslide.Value
    maxsteps = self.x_maxslide.Value

    x_min = self.x_slider_min + self.x_slider_stepssize * minsteps
    x_max = self.x_slider_min + self.x_slider_stepssize * maxsteps

    if x_min > x_max:
        self.x_maxslide.Value = self.x_minslide.Value
        self.x_minslide.Value = self.x_maxslide.Value

    if self.x_var.GetSelection() == 3:
        x_minstr = plt.num2date(x_min).strftime('%Y-%m-%d %H:%M')
        x_maxstr = plt.num2date(x_max).strftime('%Y-%m-%d %H:%M')
    else:
        x_minstr = str(x_min)
        x_maxstr = str(x_max)

    self.x_min.SetLabel(x_minstr)
    self.x_max.SetLabel(x_maxstr)


def update_ylims(self, axis):

    selfattr = lambda s: getattr(self, 'y%d_%s' % (axis, s))
    y_choice = selfattr('var').GetItems()[selfattr('var').GetSelection()]

    if self.y1_var.Selection == self.y2_var.Selection:
        y_data = np.append( self.data[y_choice][self.get_yidx(1)],
                            self.data[y_choice][self.get_yidx(2)] )
        self.y1_min.SetValue(str(y_data.min()))
        self.y1_max.SetValue(str(y_data.max()))
        self.y2_min.SetValue(str(y_data.min()))
        self.y2_max.SetValue(str(y_data.max()))
    else:
        y_data = self.data[y_choice][self.get_yidx(axis)]
        selfattr('min').SetValue(str(y_data.min()))
        selfattr('max').SetValue(str(y_data.max()))


def enable_plot_button(self):

    if self.x_var.Selection * self.y1_var.Selection:
        self.BTN_plot.Enable()
    else:
        self.BTN_plot.Disable()


def enable_y_properties(self, enable=True, axis=1):

    obj_list = 'max min label \
                color linestyle linewidth \
                markerfacecolor marker markersize \
                CHatm CHequ CHspan CHzero'

    for obj_str in obj_list.split():
        obj = getattr( self, 'y%d_%s' % (axis, obj_str) )
        obj.Enable(enable)


def get_yidx(self, axis=1):

    licor_cmnd = self.data.licor_cmnd
    check_list = [['air_pump_off',      'atm'],
                  ['equil_pump_off',    'equ'],
                  ['span_pump_off',     'span'],
                  ['zero_pump_off',     'zero']]

    idx = np.zeros_like(licor_cmnd).astype(bool)
    for cmnd, box in check_list:
        box_obj = getattr(self, 'y%d_CH%s' % (axis, box) )
        idx += (licor_cmnd == cmnd) * box_obj.GetValue()

    return idx


def get_plot_properties(self):

    def get_x_props(self):
        selfattr = lambda s: getattr(self, s)
        selfselection = lambda s: selfattr(s).Items[selfattr(s).Selection]

        minsteps = self.x_minslide.Value
        maxsteps = self.x_maxslide.Value

        x_min = self.x_slider_min + self.x_slider_stepssize * minsteps
        x_max = self.x_slider_min + self.x_slider_stepssize * maxsteps

        prop = {'var': selfselection('x_var'),
                'min': x_min,
                'max': x_max}

        return prop


    def get_y_props(self, axis):
        selfattr = lambda s: getattr(self, 'y%d_%s' % (axis, s))
        selfselection = lambda s: selfattr(s).Items[selfattr(s).Selection]
        arr = lambda d: np.array(d)

        flt_key = 'max min linewidth markersize'.split()
        clr_key = 'color markerfacecolor'.split()
        sln_key = 'var linestyle marker'.split()
        str_key = 'label'.split()

        prop = {}
        flt_val = arr([selfattr(s).Value  for s in flt_key]).astype(float)
        clr_val = arr([selfattr(s).GetColour() for s in clr_key]).astype(float)/255.
        sln_val = arr([selfselection(s)   for s in sln_key])
        str_val = arr([selfattr(s).Value  for s in str_key])

        prop.update(zip(flt_key, flt_val))
        prop.update(zip(clr_key, clr_val))
        prop.update(zip(sln_key, sln_val))
        prop.update(zip(str_key, str_val))

        return prop


    x_prop_dict = get_x_props(self)
    y1_prop_dict = get_y_props(self, 1)

    error_str = "Your axes ranges are not valid:"
    if x_prop_dict['min'] > x_prop_dict['max']:
        error_str += "\nX-MIN is larger than X-MAX"
    if y1_prop_dict['min'] > y1_prop_dict['max']:
        error_str += "\nY1-MIN is larger than Y1-MAX"

    if self.y2_var.Selection:
        y2_prop_dict = get_y_props(self, 2)
        if y2_prop_dict['min'] > y2_prop_dict['max']:
            error_str += "\nY2-MIN is larger than Y2-MAX"

    if len(error_str) > 35:
        print len(error_str)
        dlg = wx.MessageDialog(self, error_str,'Min-Max Error', wx.ICON_WARNING)
        dlg.ShowModal()
        dlg.Destroy()
        return None

    elif self.y2_var.Selection:
        prop_dict = {'x' :  x_prop_dict,
                     'y1': y1_prop_dict,
                     'y2': y2_prop_dict}
        return prop_dict

    else:
        prop_dict =  {'x':  x_prop_dict,
                      'y1': y1_prop_dict}
        return prop_dict


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

    plt.subplot(111)

    if prop['x']['var'] == 'wg_datenum':
        plt.plot_date(x1, y1, **prop['y1'])
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.2)
    else:
        plt.plot(x1, y1, **prop['y1'])

    plt.xlim(x_lims)
    plt.ylim(y1_lims)
    plt.ylabel(prop['y1']['label'], color=prop['y1']['color'])
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
        plt.ylabel(prop['y2']['label'], color=prop['y2']['color'])
        plt.yticks(color=prop['y2']['color'])

    plt.title(self.xy_title.GetValue())

    plt.show()