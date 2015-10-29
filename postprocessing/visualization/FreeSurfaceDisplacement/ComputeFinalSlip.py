import numpy as np
import os
#import matplotlib.pyplot as plt
from math import floor,sqrt

#prefix='sumatra'
#folder='OutputSumatraLong'
#nrec=5490
#nx=61
#X0=-112587.5383730000
#Y0=-222089.5187140000
#inc=2.5e4

prefix='dip10'
folder='OUTPUTDIP10/Outputdip10-inc-plas-m2'
nrec=3111
nx=50
X0=-20000.000000
Y0=-75000.000000 
inc=2.5e3


ny=nrec/nx
aDisp = np.zeros((nx,ny))

fout=open('finaldisp.dat','w')

import glob
ReceiverFileList = glob.glob('%s/%s-receiver-*' %(folder, prefix))

for id in range(0,nrec):
   mytemplate='%s/%s-receiver-%05d' %(folder, prefix, id+1)
   MatchingFiles = [s for s in ReceiverFileList if mytemplate in s]
   #Error Handling
   if len(MatchingFiles)==0:
      print("no file matching "+mytemplate)
      exit()
   elif len(MatchingFiles)>1: 
      print("more than a file matching "+mytemplate)
      print(MatchingFiles)
      exit()
   myfile=MatchingFiles[0]
   print(myfile)

   #Read coordinates
   fid = open(myfile)
   fid.readline()
   fid.readline()
   xc= float(fid.readline().split()[2])
   yc= float(fid.readline().split()[2])
   zc= float(fid.readline().split()[2])
   fid.close()

   #Read data
   test = np.loadtxt(myfile,  skiprows=5)
   dt=test[1,0]
   vx=test[:,7]
   vy=test[:,8]
   vz=test[:,9]

   #Compute displacement
   dx=np.trapz(vx,dx=dt)
   dy=np.trapz(vy,dx=dt)
   dz=np.trapz(vz,dx=dt)

   i1=int(round((xc-X0)/inc))
   j1=int(round((yc-Y0)/inc))
   aDisp[i1,j1]=sqrt(dx**2+dy**2+dz**2)
   fout.write('%d %d %e %e %e %e %e %e\n' %(i1, j1, xc, yc, zc, dx,dy,dz))
fout.close()

stop

# Generate a regular grid to interpolate the data.
xi=np.arange(X0,X0+nx*inc,inc)
yi=np.arange(Y0,Y0+nx*inc,inc)

Xi, Yi = np.meshgrid(xi, yi)

# Plot the results
plt.figure()

plt.pcolormesh(Xi,Ti,aDisp)
plt.colorbar()
#plt.axis('equal')
#plt.xlim(-20e3, 20e3)
#plt.ylim(-20e3, 0)
plt.show()
