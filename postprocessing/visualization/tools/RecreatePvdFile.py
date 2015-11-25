import os.path
#Author Thomas Ulrich, LMU
#Recreate a pvd file (fault output for paraview) by looking through all the "fault-xxxx" folders

#INPUTS
myfolder = 'Resultstpv29Z192'
myprefix = 'tpv29Z'
PrintInterval=1500
dt=9.012937012616767E-004
tf=10.
nNodes=20

#Now writing the file
fout = open('newpvd.pvd','w')
fout.write("<?xml version='1.0' ?>\n<VTKFile type='Collection' version='0.1'>\n<Collection>\n")

iPrint=1
while(True):
	print(dt*iPrint)
	iPart=0
	for inode in range(0,nNodes):
		ti=iPrint*dt
		fname='%s-fault-00%03d/timestep-%09d.vtu' %(myprefix, inode,iPrint)
		fnpath = myfolder +'/'+ fname
		if os.path.isfile(fnpath):
			print fnpath
			fout.write("<DataSet timestep='%f' group='' part='%d' file='%s'/>\n" %(ti, iPart, fname))
			iPart = iPart+1
	if (iPrint== (int) (tf/dt)):
		break
	iPrint = iPrint + PrintInterval
	if (iPrint>tf/dt):
		iPrint=(int) (tf/dt)

fout.write("</Collection>\n</VTKFile>\n")


fout.close()
	

