"""
Create a new module called genpolar.py. Within this module, create a generator called rtrings which will yield the radius and theta co-ordinate values for concentric rings of points in the X-Y plane (including a single point at the origin). It should be callable as below:
rtrings(rmax=5., nrings=5, multi=6)
where rmax is the maximum radius to extend to, nrings is the number of concentric rings to produce and multi is a multiplier which indicates how many points should be in each ring such that 
For reference, calling rtrings with the above parameters would yield radius and theta values that if plotted would look like the figure below (Note you are not expected to make this plot).
"""
import numpy as np

def rtrings(rmax = 5 , nrings = 5, multi = 6):
    scale = rmax/nrings
    for rings in np.arange(nrings+1):
        radius = scale*rings
        if radius ==0:
            yield 0,0
        else:
            for theta in (2*np.pi/(rings*multi))*np.arange(rings*multi):
                yield radius , theta
