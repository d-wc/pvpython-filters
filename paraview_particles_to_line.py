##################################################
## Via a programmable filter in Paraview 5.10, 
## this script loads XYZ coordinates of particles from particleTracer to link neighbors in time
## Input: particle tracks, output: neighbor lines and neighbor displacement (neighborDist)
##################################################
## Daniel Carlson
## 2021 Nov
##################################################

import math
import numpy as np
from vtk.numpy_interface import algorithms as algs
from vtk.numpy_interface import dataset_adapter as dsa

input0 = inputs[0]
X = input0.PointData["x [mm]"]/1000 #Change XYZ and scale to your coordinate names
Y = input0.PointData["y [mm]"]/1000
Z = input0.PointData["z [mm]"]/1000
pAge = input0.PointData["InjectionStepId"] #default injection name in time from particleTracer

steps=np.unique(pAge)

xn = np.array(X)
yn = np.array(Y)
zn = np.array(Z)
pn = np.array(pAge)

pdo = self.GetPolyDataOutput()
pts = vtk.vtkPoints()

kk = 0
nn = 0
ptsLen = np.array([None for _ in range(len(steps))])

difOut = 0*xn

for jj in steps:
    
    indTmp = pn == jj

    xInd = xn[indTmp]
    yInd = yn[indTmp]
    zInd = zn[indTmp]
    ptsLen[nn] = len(xInd)
    
    difPt = 0*xInd

    difPt[0] = math.sqrt((xInd[2]-xInd[0])**2 + (yInd[2]-yInd[0])**2 + (zInd[2]-zInd[0])**2)
    difPt[-1] = math.sqrt((xInd[-1]-xInd[-1-2])**2 + (yInd[-1]-yInd[-1-2])**2 + (zInd[-1]-zInd[-1-2])**2)
    for i in range(1,len(xInd)-1):
       difPt[i] = math.sqrt((xInd[i+1]-xInd[i-1])**2 + (yInd[i+1]-yInd[i-1])**2 + (zInd[i+1]-zInd[i-1])**2)
    
    difOut[indTmp] = difPt
    coordinates = algs.make_vector(xInd, yInd, zInd)
    for ii in range(0,len(xInd)):
        pts.InsertPoint(kk,coordinates[ii,0],coordinates[ii,1],coordinates[ii,2])
        kk = kk+1
    nn = nn +1

output.PointData.append(difOut, 'neighborDist')     
pdo.SetPoints(pts)
pdo.Allocate(len(steps),1)

for jj in range(0,len(steps)-1):
    aPolyLine = vtk.vtkPolyLine()
    aPolyLine.GetPointIds().SetNumberOfIds(ptsLen[jj])
    
    if jj == 0:
        ptStart = 0
    else:
        ptStart = np.sum(ptsLen[0:jj])
          
    for ii in range(0,ptsLen[jj]):
        aPolyLine.GetPointIds().SetId(ii, ptStart+ii)
        
    pdo.InsertNextCell(aPolyLine.GetCellType(), aPolyLine.GetPointIds())    
    
