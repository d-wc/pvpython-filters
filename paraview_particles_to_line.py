import math
import numpy as np
from vtk.numpy_interface import algorithms as algs
from vtk.numpy_interface import dataset_adapter as dsa

input0 = inputs[0]
X = input0.PointData["x [mm]"]/1000
Y = input0.PointData["y [mm]"]/1000
Z = input0.PointData["z [mm]"]/1000
pAge = input0.PointData["InjectionStepId"]
coordinates = algs.make_vector(X, Y, Z)
pts = vtk.vtkPoints()
pts.SetData(dsa.numpyTovtkDataArray(coordinates, 'Points'))
output.SetPoints(pts)
output.PointData.append(index, 'Index')
output.PointData.append(pAge, 'pAge')
ptIds = vtk.vtkIdList()
ptIds.SetNumberOfIds(len(X))
for i in range(len(X)):
   #Add the points to the line. The first value indicates
   #the order of the point on the line. The second value
   #is a reference to a point in a vtkPoints object. Depends
   #on the order that Points were added to vtkPoints object.
   #Note that this will not be associated with actual points
   #until it is added to a vtkPolyData object which holds a
   #vtkPoints object.
   ptIds.SetId(i, i)

difPt = 0*X

difPt[0] = math.sqrt((X[2]-X[0])**2 + (Y[2]-Y[0])**2 + (Z[2]-Z[0])**2)
difPt[-1] = math.sqrt((X[-1]-X[-1-2])**2 + (Y[-1]-Y[-1-2])**2 + (Z[-1]-Z[-1-2])**2)
for i in range(1,len(X)-1):
   difPt[i] = math.sqrt((X[i+1]-X[i-1])**2 + (Y[i+1]-Y[i-1])**2 + (Z[i+1]-Z[i-1])**2)

# Allocate the number of 'cells' that will be added. We are just
# adding one vtkPolyLine 'cell' to the vtkPolyData object.
output.Allocate(1, 1)
output.PointData.append(difPt, 'pyPts')
# Add the poly line 'cell' to the vtkPolyData object.\output.PointData.append(index, 'Index')
output.InsertNextCell(vtk.VTK_POLY_LINE, ptIds)
print(ptIds)