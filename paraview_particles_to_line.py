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

for jj in steps:
    
    indTmp = pn == jj
    print(indTmp)
    xInd = xn[indTmp]
    yInd = yn[indTmp]
    zInd = zn[indTmp]

    coordinates = algs.make_vector(xInd, yInd, zInd)
    pts = vtk.vtkPoints()
    pts.SetData(dsa.numpyTovtkDataArray(coordinates, 'Points'))
    output.SetPoints(pts)

    ptIds = vtk.vtkIdList()
    ptIds.SetNumberOfIds(len(xInd))
      
    for i in range(len(xInd)):
       #Add the points to the line. The first value indicates
       #the order of the point on the line. The second value
       #is a reference to a point in a vtkPoints object. Depends
       #on the order that Points were added to vtkPoints object.
       #Note that this will not be associated with actual points
       #until it is added to a vtkPolyData object which holds a
       #vtkPoints object.
       ptIds.SetId(i, i)
       
    
    print(jj)

    difPt = 0*xInd

    difPt[0] = math.sqrt((xInd[2]-xInd[0])**2 + (yInd[2]-yInd[0])**2 + (zInd[2]-zInd[0])**2)
    difPt[-1] = math.sqrt((xInd[-1]-xInd[-1-2])**2 + (yInd[-1]-yInd[-1-2])**2 + (zInd[-1]-zInd[-1-2])**2)
    for i in range(1,len(xInd)-1):
       difPt[i] = math.sqrt((xInd[i+1]-xInd[i-1])**2 + (yInd[i+1]-yInd[i-1])**2 + (zInd[i+1]-zInd[i-1])**2)

    # Allocate the number of 'cells' that will be added. We are just
    # adding one vtkPolyLine 'cell' to the vtkPolyData object.
    output.Allocate(8,8)

    output.PointData.append(difPt, 'pyPts')
    output.PointData.append(pn[indTmp], 'pypts' + str(jj))

    # Add the poly line 'cell' to the vtkPolyData object.\output.PointData.append(index, 'Index')
    output.InsertNextCell(vtk.VTK_POLY_LINE, ptIds)
