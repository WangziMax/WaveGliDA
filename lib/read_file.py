# -*- coding: utf-8 -*-
"""

created: Sat Jan 18 22:41:29 2014
author:  Luke Gregor
"""

import numpy as np
from pandas import DataFrame
from read_lineblocks import read_licor, read_durafet, read_prawler, read_sbe63

def read_wgfile(fname, return_rawstr=False):
    """
    This function reads in a wave glider data file. It is compatible with
    Licor, Prawler, Durafet and SBE63 data.
    """

    with open(fname, 'r') as wg_file:  # read fname
        filestr = wg_file.read()

    filelines = split_filestr(filestr)

    DATA = {}
    read_list = [None,
                 read_licor,
                 read_durafet,
                 read_prawler,
                 read_sbe63]

    group_lines = []
    read_func = None  # CO2 group is always first
    for c, line in enumerate(filelines):  # read file line by line
        # TRUE when a blank line is reached and the block of lines has len > 0
        line_type = get_line_type(line)
        bool_start_group = (line_type > 0) & (line_type is not None)
        bool_end_group = (line_type < 0) & (line_type is not None)
        bool_nonsense = (line_type == 0) & (line_type is not None)

        if bool_start_group:  # if there is a keyword line
            read_func = read_list[line_type]
            group_lines = [line]

        elif bool_end_group:  # read the group that has been built

            group_lines += line,
            data_tmp = read_func(group_lines)
            for key in data_tmp:
                if not DATA.has_key(key):
                    DATA[key] = np.array(data_tmp[key])
                else:
                    DATA[key] = np.append(np.array(DATA[key]),
                                          np.array(data_tmp[key]))

            group_lines = []
            read_func = read_list[0]

        elif bool_nonsense:
            pass

        else:  # add any other lines to the previous group
            group_lines += line,

    if not DATA:
        return DataFrame()

    return DataFrame(DATA, index=DATA['wg_datetime'])


def split_filestr(filestr):
    """
    Adds a new line to the end of the file that you want to read. This is
    done to read the last block of lines which would otherwise get skipped
    because of the way the file is read. If there are already two newlines
    none will be added.
    """
    if filestr[-2:] == '\n\n':
        filelines = filestr.splitlines()
        filelines.insert(0, [])
    else:
        filelines = filestr.splitlines()
        filelines.insert(0, [])
        filelines.append([])

    return filelines


def get_line_type(line):
    """
    Lines are classified based on the start of a "paragraph"
    i.e. NORM signals that it is the start of a CO2 paragraph
    I use indicies to indicate line types:
           0 - blank
           1 - CO2
           2 - Durafet
           3 - Prawler CTD
           4 - SeaBird CTD
    """

    if line: line = line.strip().upper()
    if len(line) < 2:                               return 0
    elif line.startswith(('NORM', 'FAST', 'DEPL')): return 1
    elif line.startswith('DURAFET'):                return 2
    elif line.startswith('PRAWLER'):                return 3
    elif line.startswith('SBE63'):                  return 4
    elif line.startswith(('END', 'SW_X')):          return -1


if __name__ == "__main__":

    filename = 'D:/Desktop/WaveGlider/test_data/san53/C0002_12_16_2013'
    dat = read_wgfile(filename)
