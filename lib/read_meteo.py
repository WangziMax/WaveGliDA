import pandas as pd 
from pylab import *


def main():
    
    read_meteo( 'D:/Dropbox/Data/SOCCO pCO2/WGpCO2002/CSIR#1 Telemetry and weather.txt' )
    

def read_meteo( fname ):
    
    dat = pd.read_csv(fname, 
                      sep=';',
                      decimal=',')
    
    dat.index = pd.to_datetime(dat.TimeStamp)
    
    for i in find(dat.pressure_mb.str.endswith(',')):
        dat.pressure_mb[i] = dat.pressure_mb[i][:-1]
    
    dat.pressure_mb = dat.pressure_mb.str.replace(',', '.').astype(float)
    
    dat = dat.resample('H',  how='mean')
    
    dat.pressure_mb.plot(ls='none', marker='.')
    show()
    
if __name__ == "__main__":
    
    main()