from pylab import *

#import pygmmreg
import ConfigParser
import os

def run(f_config):
     
    #pygmmreg.gmmreg_tps_ini(f_config)
    cmd = 'gmmreg_tps %s'%f_config;
    os.system(cmd)
    c = ConfigParser.ConfigParser()
    c.read(f_config)
    mf = c.get('Files','modelfile')
    sf = c.get('Files','scenefile')
    tf = c.get('Files','afterregptsfile')

    m = load(mf)
    s = load(sf)
    t = load(tf)

    subplot(1,2,1)
    plot(s[:,0],s[:,1],'yo',markersize=10,mew=1)    
    plot(m[:,0],m[:,1],'b+',markersize=10,mew=1)
    

    subplot(1,2,2)
    plot(s[:,0],s[:,1],'yo', markersize=10,mew=1)
    plot(t[:,0],t[:,1],'b+', markersize=10,mew=1)
    width = t[:,0].max() - t[:,0].min()
    x_min = t[:,0].min() - width/10
    x_max = t[:,0].max() + width/10
    setp(gca(), 'xlim', [x_min,x_max])

    show()
    

if __name__=="__main__":
    run('./fish_full.ini')