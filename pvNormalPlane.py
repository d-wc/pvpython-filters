##################################################
## In Paraview, apply as programmable filter to slice plane velocity field U with name 'Slice1' 
## Find the primary flow direction and make the plane orthogonal to the flow
## output: none 
##################################################
## Daniel Carlson
## 2022 December
## Okinawa Institute of Science and Technology
##################################################


import numpy as np
from paraview import simple
from paraview import servermanager as sm
from paraview.vtk.numpy_interface import dataset_adapter as dsa

#find the source plane with some name
slicePlane = simple.FindSource('Slice1')

source_vtk = sm.Fetch(slicePlane)
vtk_data = dsa.WrapDataObject(source_vtk)

UU = vtk_data.PointData["U"]

#find the average flow on the original plane
U0 = mean(UU[:,0])
U1 = mean(UU[:,1])
U2 = mean(UU[:,2])

#align the plane to the flow
slicePlane.SliceType.Normal = [U0,U1,U2]

slicePlane.UpdatePipeline()

