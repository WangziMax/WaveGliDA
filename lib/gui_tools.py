# -*- coding: utf-8 -*-
"""

created: Sat Jan 18 23:42:04 2014
author:  Luke Gregor
"""

import numpy as np
import calc_co2 as co2


class dict2obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [dict2obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, dict2obj(b) if isinstance(b, dict) else b)


def TextFile_2_TextCtrl(TextCtrl, txt_file_name, pfx='', sfx=''):

    with open(pfx + txt_file_name + sfx) as file_obj:

        txt_str = file_obj.read()

    TextCtrl.AppendText(txt_str)


def list_2_ListBox(ListBox, item_list):

    item_list = np.array(item_list[0])
    for item in item_list:
        ListBox.Append(item)


def get_pretty_name(var_name, input_file='./doc/pretty_names.txt'):

    with open(input_file) as file_obj:
        pretty_lines = file_obj.read().splitlines()

    for line in pretty_lines:
        if line.startswith(var_name):
            return line.split(',')[-1].strip()
        else:
            pass
    return ''


def pdDataFrame_2_numpy(Data, col_names=None):

    if not col_names:
        col_names = Data.keys()

    out = {}

    for key in col_names:
        out[key] = np.array(Data[key])

    return out


def modify_docstring(docstring):
    """Removes single \n and maintains \n\n"""

    docstring = docstring.replace('  ',   '')

    docstring = docstring.replace('\n\n', '\Q')
    docstring = docstring.replace('\n-', '\l=')
    docstring = docstring.replace('-\n', '=\l')

    docstring = docstring.replace('\n',   ' ')

    docstring = docstring.replace('\l=', '\n-')
    docstring = docstring.replace('=\l', '-\n')
    docstring = docstring.replace('\Q', '\n\n')

    return docstring

def make_pco2_help():
    """Goes into calc_co2 and gets all the docstrings. This is for updating
    help_CO2_calculations.txt"""

    help_str = """CO2 Calculations
    ================
    *** UNDER CONSTRUCTION -- CURRENTLY NOT WORKING ***

    The CO2 calculations are shown by function. See './doc/calc_co2.py' for more


    """.replace('  ', '')

    co2_funcs = [co2.calc_xco2_raw,
                 co2.calc_xco2_dry,
                 co2.calc_pco2,
                 co2.calc_fco2]

    for func in co2_funcs:
        help_str += modify_docstring(func.__doc__)
        help_str += '\n\n\n'

    with open('../doc/help_CO2calculations.txt', 'w') as file_obj:
        file_obj.write(help_str)


if __name__ == "__main__":
    make_pco2_help()
    import compiler

    compiler.compileFile('../WaveGliDA.py')
