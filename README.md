WaveGliDA (0.5)
===============
WAVe GLIder Data Analysis is a program to read, calculate and plot raw Wave Glider files. 
For more info read the help and info files in this panel.
 
* version:    0.5 
* date:       6 March 2014
* author:     Luke Gregor
* email:      luke.gregor@outlook.com

####A. INFORMATION
This program is designed to process and read wave glider data. It reads raw files grouped in one folder. There are basic plotting and mapping tools to asses the data. The data can also be saved as a CSV.


####B. INSTALLATION
For this program to work you need Python 2.7 with the following packages installed:
* numpy
* scipy
* matplotlib
* pandas
* wx
* basemap

I recommend that you download [Canopy dist by Enthought](https://www.enthought.com/downloads/). The free distribution contains all the packages you'll need and is compatible with Windows, Linux and MAC.
I've also tested the Anaconda (by Continuum) distribution of Python, but this distribution does not work in Mac OS X due to issues with the WX package. 


####C. RUNNING
To run the program navigate to the WaveGliDA directory and type: 
`python '.../WaveGliDA.pyc'`


####E. TO DO
1. pco2 calculations
2. help for the maps
3. glider speed
5. a list of standard plots for xyplots
6. Salinity does not show on xyplot options when importing data
9. Troubleshoot the errors that pop up in the terminal

