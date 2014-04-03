import pandas as pd 
from pylab import *


def main():
    
    dat = read_weather_file( 'D:/Dropbox/Data/SOCCO pCO2/WGpCO2002/CSIR#1 Telemetry and weather.txt' )
    return dat


def get_weather( self ):
    
    if not self.FP_weather_stn.GetPath():
        return
    
    elif self.FP_weather_stn.GetPath().endswith('.txt'):
        self.StatusBar.SetStatusText('Importing Weather Data')
        fname = self.FP_weather_stn.GetPath()
        
        wthr_data = read_weather_file( fname ).tz_localize('UTC')
        self.data = self.data.join( wthr_data, how='left' )
        
        for key in wthr_data.keys():
            self.data[key] = self.data[key].fillna(method='pad')
        
        


def read_weather_file( fname ):
    
    dat = pd.read_csv(fname, 
                      sep='\t')
    
    dat.index = pd.to_datetime(dat.TimeStamp)

    dat = dat.resample('H',  how='mean')
    
    dct = {}
    for key in dat.keys():
        dct[ 'wthr_'+key ] = dat[key]
    
    dat = pd.DataFrame(dct)
    
    return dat
    
    
if __name__ == "__main__":
    out = main()