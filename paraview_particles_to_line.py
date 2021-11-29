import math
import numpy as np
from vtk.numpy_interface import algorithms as algs
from vtk.numpy_interface import dataset_adapter as dsa

input0 = inputs[0]
X = input0.PointData["x [mm]"]/1000
Y = input0.PointData["y [mm]"]/1000
Z = input0.PointData["z [mm]"]/1000
pAge = input0.PointData["InjectionStepId"]

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
for jj in steps:
    
    indTmp = pn == jj

    xInd = xn[indTmp]
    yInd = yn[indTmp]
    zInd = zn[indTmp]
    ptsLen[nn] = len(xInd)
    
    coordinates = algs.make_vector(xInd, yInd, zInd)
    for ii in range(0,len(xInd)):
        pts.InsertPoint(kk,coordinates[ii,0],coordinates[ii,1],coordinates[ii,2])
        kk = kk+1
    nn = nn +1
     
pdo.SetPoints(pts)
pdo.Allocate(len(steps),1)

for jj in range(0,len(steps)-1):
    aPolyLine = vtk.vtkPolyLine()
    aPolyLine.GetPointIds().SetNumberOfIds(ptsLen[jj])
    
    if jj == 0:
        ptStart = 0
        ptsEnd = ptsLen[1]-1
    else:
        ptStart = np.sum(ptsLen[0:jj])
        ptsEnd = ptStart + ptsLen[jj]-1
          
    print(ptStart)
    print(ptsEnd)
    
    for ii in range(0,ptsLen[jj]):
        aPolyLine.GetPointIds().SetId(ii, ptStart+ii)
        

    pdo.InsertNextCell(aPolyLine.GetCellType(), aPolyLine.GetPointIds())    
