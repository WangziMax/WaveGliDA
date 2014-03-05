"""
Creates colormap images that will be used in the map scatterplot.
"""

import os
import Image
import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, 1, 256).reshape(1,-1)
a = np.vstack((a,a))

maps = ['bone','gray','hot','jet','Spectral_r','RdBu_r','PRGn_r']
nmaps = len(maps) + 1
plt.ioff()
for i,m in enumerate(maps):
    print m
    plt.figure(figsize=(2.5,0.2))
    plt.axes([0, 0, 1, 1])
    plt.axis("off")
    plt.imshow(a, aspect='auto', cmap=plt.get_cmap(m), origin='lower')
    plt.savefig('./%s.jpg' % m, pad_inches=0)
    plt.close()
    outfile = './%s.bmp' % m
    img = Image.open('./%s.jpg' % m)
    img.save(outfile)
    os.remove('./%s.jpg' % m)

print ''