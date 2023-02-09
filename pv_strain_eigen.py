##################################################
## In Paraview, apply as programmable filter to velocity field U
## Find the strain tensor and compute eigenvectors and eigenvalues
## output: none 
##################################################
## Daniel Carlson
## 2023 February
## Okinawa Institute of Science and Technology
##################################################




import numpy as np

from vtk.numpy_interface import algorithms as algs

inputs = inputs[0]

UVECT = inputs.PointData["U"]

STRAINTEN = 0.5*strain(UVECT)

[DEIGVAL,DEIGVEC] = np.linalg.eig(STRAINTEN)

output.PointData.append(DEIGVAL,'deigVal')
output.PointData.append(DEIGVEC,'deigVec')
