#!/bin/sh
awk 'i==0 {print "x,y,z,dz";i=1} {printf "%f,%f,%f,%f\n",$3,$4,$5,$8}' finaldisp.dat > finaldisp.csv
