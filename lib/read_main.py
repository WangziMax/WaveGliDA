# -*- coding: utf-8 -*-
"""

created: Sat Jan 18 23:05:26 2014
author:  Luke Gregor
"""

import os
import re
import numpy as np
from read_file import read_wgfile
from datetime import datetime as dt

def get_wg_filenames(dirname):
    """
    The function takes the directory and looks if there are any wave glider
    files in the folder. The files are then sorted by date. A custom date
    can be added, American is default [m d Y].
    """

    strptime = dt.strptime
    file_list = np.array(os.listdir(dirname))
    fullpath_list, file_datetime, is_wg = [], [], []
    for filename in file_list:
        filepath = os.path.join(dirname, filename)
        wg_id, file_date = filename.split('_', 1)
        if is_wg_file(filepath):
            file_datetime += strptime(file_date, '%m_%d_%Y'),
            fullpath_list += filepath,

    idx = np.argsort(np.array(file_datetime))

    return np.array(fullpath_list)[idx]


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


def read_wg_filelist(file_list, progress_obj=None, verbose=False):
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

    if progress_obj:
        progress_obj.SetRange(len(file_list))

    dat = None
    for c, fullpath in enumerate(file_list):
        # adding file data to the dat info
        if not dat:  # for the first iteration create the object
            dat = read_wgfile(fullpath)
        else:        # for following iterations append the data
            dat = dat.append(read_wgfile(fullpath))

        if progress_obj:
            progress_obj.SetValue(c+1)
        elif verbose:
            print os.path.split(fullpath)[-1]

    if dat: # if there are no files in the dir, returns None
        return dat.sort_index().drop_duplicates()
    else:
        return None


if __name__ == "__main__":
    dirname = 'D:/Desktop/C0001_SAN53'

    file_list = get_wg_filenames(dirname)
    dat = read_wg_filelist(file_list, verbose=True)