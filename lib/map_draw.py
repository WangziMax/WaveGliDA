from matplotlib import pylab as plt
import numpy as np

def func_plot_map(self, event):
    prop = self.get_map_properties()
    lat = prop.pop('south'), prop.pop('north')
    lon = prop.pop('west' ), prop.pop('east')
    dlim = prop.pop('dmin'), prop.pop('dmax')

    prop
    map_obj = bath_map(lat, lon, **prop)

    x = self.data.wg_longitude
    y = self.data.wg_latitude
    t = self.data.wg_datenum

    idx_dtime = (t >= dlim[0]) * (t <= dlim[1])
    idx_cords = (x > lon[0]) * (x < lon[1]) * \
                (y > lat[0]) * (y < lat[1])
    idx_licor = self.get_midx()
    idx = idx_dtime * idx_cords * idx_licor

    x = x[idx]
    y = y[idx]
    c = self.data[ prop['var'] ][idx]

    x, y = map_obj(x, y)

    map_obj.scatter(x, y,
                    prop['markersize'],
                    c,
                    marker=prop['marker'],
                    cmap=prop['cmap'],
                    linewidths=0)
    plt.clim(prop['cmin'], prop['cmax'])
    plt.title(prop['title'])
    plt.colorbar()
    plt.show()


def bath_map(lat,lon,**kwargs):
    """
    Plots a map (using Basemap) for the defined area.
    Can choose to have bathymetry (bath = 'contours/color/both/marble')
    x,y are scatter points which will be plotted on the map

    lats = [min,max]
    lons = [min,max]
    cmap = cm.---
    bath = [contour,color,both]
    """
    from mpl_toolkits.basemap import Basemap
#    from scipy.io.netcdf import netcdf_file


#    bath  = kwargs.pop('bath','color')
#    cmap  = kwargs.pop('cmap',cm.Spectral_r)
#    title = kwargs.pop('title',None)
#    pvmin = kwargs.pop('pvmin',None)
    rivers = kwargs.pop('rivers',False)
    landfill = kwargs.pop('landfill',True)
    coastlines = kwargs.pop('coastlines',True)
    figsz = kwargs.pop('figsz',None)
    res = kwargs.pop('res','i')
#    lvls  = kwargs.pop('lvls',np.arange(-6000,000,500))

    # SETTING DOMAIN
    minLat, maxLat = map(float, lat)
    minLon, maxLon = map(float, lon)
    lond = maxLon-minLon
    latd = maxLat-minLat

    # SETTING FIGURE SIZE
    coord_ratio = latd/lond
    if not figsz:
        figsz = [8,8]
        if coord_ratio > 1:
            figsz[0] = figsz[0] / coord_ratio
        else:
            figsz[1] = figsz[1] * coord_ratio

    # MAP
#    fig = plt.figure(figsize=figsz)
    m = Basemap(llcrnrlon  = minLon,
              llcrnrlat  = minLat,
              urcrnrlon  = maxLon,
              urcrnrlat  = maxLat,
              resolution = res[0],
              projection = 'cyl',
              #~ lon_0 = minLon+(maxLon-minLon)/2,
              #~ lat_0 = minLat+(maxLat-minLat)/2,
              area_thresh=100000)
    # MAP FEATURES

    if landfill:
        m.fillcontinents(color='#DEDEDE')
    if coastlines:
        m.drawcoastlines(linewidth=1)
    if rivers:
        m.drawrivers()

#    if not pvmax: pvmax = 0

    # BATHYMETRY

#    if bath and (bath!='marble') and (bath!='none'):
#        print "\t processing bathymetry"
#        bathfile = '/home/luke/Dropbox/Data/ETOPO/ETOPO1_Ice_g_gmt4.grd'
#        nc = netcdf_file(bathfile,'r')
#
#        ncX = nc.variables['x'][::i]
#        ncY = nc.variables['y'][::i]
#        ncZ = nc.variables['z'][::i,::i]
#        ncXind = (ncX>minLon-.0002) & (ncX<maxLon+.0002)
#        ncYind = (ncY>minLat-.0002) & (ncY<maxLat+.0002)
#
#        X = ncX[ncXind]
#        Y = ncY[ncYind]
#        Z = sp.array([z[ncXind] for z in ncZ[ncYind]])
#        X,Y = m(*meshgrid( X, Y))
#
#    if (bath is 'color') or (bath is 'both'):
#        print "\t plotting colour bathymetry "
#        m.pcolormesh(X,Y,Z,cmap=cmap,vmin=pvmin,vmax=pvmax)
#        colorbar()
#
#    if (bath is 'contour') or (bath is 'both'):
#        print "\t plotting contour bathymetry"
#
#        contours = m.contour(X,Y,Z,levels=lvls,colors='gray',linestyles='-',linewidths=1.,alpha=1.0)#
#        clabel(contours,fmt='%.0f', fontsize=6)


    # GRIDLINES
    pstep = None
    mstep = None
    for degs in [.1,.5,1,5,10,20,50,100]:
        if (latd<=degs) & (not pstep): pstep = degs/10.
        if (lond<=degs) & (not mstep): mstep = degs/10.

    if not pstep: pstep=20
    if not mstep: mstep=20

    if pstep>mstep:mstep=pstep
    if mstep>pstep:pstep=mstep

    dec = -int(np.ceil(np.log10(pstep)))
    parallels = np.arange(np.around(minLat, dec),
                          np.around(maxLat, dec)+pstep,
                          pstep)
    meridians = np.arange(np.around(minLon, dec),
                          np.around(maxLon, dec)+mstep,
                          mstep)

    if len(meridians)>5: meridians = meridians[0::2]
    if len(parallels)>5: parallels = parallels[0::2]

    m.drawparallels(parallels,color='k',labels=[1,0,0,0],linewidth=0.5,dashes=[1,3])
    m.drawmeridians(meridians,color='k',labels=[0,0,0,1],linewidth=0.5,dashes=[1,3])

    return m


if __name__=='__main__':

    """
    To make selection map appear faster remove the colour shading
    by adding the option: bm = None
    if nothing is selected the global range will be applied

    bathmap options:
    bath = bathymetry output type (contour, [color], both)
    lvls = contour levels [np.arange(-6000,8000,500)]
    cmap = colormap used  [cm.Sepctral_r]
    pvmin = minimum depth for color bathymetry [min depth]
    pvmax = maximum depth for color bathymetry [0m]
    resin = coastline resolution  (f,[i],l,c)

    add scatter of plot data
    """
#    globmap()

    lat = [-34.5,-34]
    lon = [18, 18.5]

#    print lat ,lon
    m = bath_map(lat,lon,
        #~ bath  = 'color',
        #~ lvls = [-200,-500,-1000],
        #~ cmap  = cm.jet,
        #~ pvmin = -1000,
        #~ pvmax = 0,
        resin = 'i',
        #~ figsz = [10,10]
        )


    #~ m.drawcoastlines(linewidth=1.0)
    #~ m.drawrivers(linewidth=1.0,color='gray')
    #~ m.drawcountries(linewidth=1.0)
    #~ m.drawmapscale(16,-34.5,16,-32.5,150,barstyle='fancy',units='km',fontsize=6)

    #~ sname = 'C:/Users/Luke/Desktop/map.pdf'
    #~ savefig(sname)
    show()
