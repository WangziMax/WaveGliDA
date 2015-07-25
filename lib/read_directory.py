# -*- coding: utf-8 -*-
"""

created: Sat Jan 18 23:05:26 2014
author:  Luke Gregor
"""

import os
import re
import numpy as np
from glob import glob
from pandas import DataFrame, concat
from read_lineblocks import get_line_type, read_licor, read_durafet,\
    read_prawler, read_sbe63


def get_wg_filenames(dirname):
    """
    The function takes the directory and looks if there are any wave glider
    files in the folder. The files are then sorted by date. A custom date
    can be added, American is default [m d Y].
    """

    file_list = np.array(glob('%s/*' % dirname))
    idx = np.array(map(os.path.isfile, file_list))

    return file_list[idx]


def is_wg_file(filepath, glider_id=None):
    """
    Uses regular expressions to determine whether the file is a glider file or
    not. If the file names have different date format change the order of the
    pattern.
    """

    pattern = ['[A-Z][0-9]{4}',  # Glider ID
               '[0-9]{2}',       # month
               '[0-9]{2}',       # day
               '[0-9]{4}$',      # year
               ]

    pattern = '_'.join(pattern)

    isfile = os.path.isfile(filepath)
    iswaveglider = bool(re.search(pattern, filepath))

    if isfile & iswaveglider:
        return True
    else:
        return False


def read_wg_filelist(file_list, self):
    """
    Overview
    --------
    Description
        Reads a group of raw wave glider files in a folder and returns a
        DataFrame

    Input
        Full path to a directory containing wave glider files.

    Output
        A pandas.DataFrame object that can be treated as a
        dictionary of an object.

    Details
    -------
    Reads only glider files where the format is C####_MM_DD_YYYY. Where the
    first 5 chars are the wave glider name. If it does not meet this format
    the file is not read in. You will have to change the code if it does not
    meet this format.

    The files are read in chronological order (uses datetime to sort files).
    If files are not in this order, you may have to change the code. to read
    the files.

    Calls a whole bunch of other read_* functions that read the file and the
    line blocks in that file.

    """

    self.Files_Progress.SetRange(len(file_list))

    dat = []
    for c, fullpath in enumerate(file_list):
        # adding file data to the dat info
        try:
            dat.append(read_wgfile(fullpath))
        except:
            self.ImportErrors += '              %s\n' % os.path.split(
                fullpath)[-1]


        self.Files_Progress.SetValue(c + 1)
        self.StatusBar.SetStatusText(
            'reading %s' % os.path.split(fullpath)[-1])

    if dat:  # if there are no files in the dir, returns None
        dat = concat(dat)
        self.StatusBar.SetStatusText('')
        dat = dat.sort_index().drop_duplicates()
        return dat
    else:
        return None


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


if __name__ == "__main__":
    dirname = '/Users/luke/GitProjects/WaveGliDA/TestData/C0001_SAN53'

    file_list = get_wg_filenames(dirname)
    dat = read_wg_filelist(file_list)
