import numpy as np

from vtk.numpy_interface import algorithms as algs

inputs = inputs[0]

UVECT = inputs.PointData["U"]

STRAINTEN = 0.5*strain(UVECT)

[DEIGVAL,DEIGVEC] = np.linalg.eig(STRAINTEN)
print(DEIGVEC.shape)

for ii in range(0,len(DEIGVAL)):
    tmpEigVal = DEIGVAL[ii,:]
    tmpEigVec = DEIGVEC[ii,:,:]

    idx = tmpEigVal.argsort()[::-1]
    tmpEigVal = tmpEigVal[idx]
    tmpEigVec = tmpEigVec[:,idx]

    DEIGVAL[ii,:] = tmpEigVal
    DEIGVEC[ii,:,:] = tmpEigVec


DV0 = DEIGVEC[0,:]
DV1 = DEIGVEC[1,:]
DV2 = DEIGVEC[2,:]

output.PointData.append(DEIGVAL,'deigVal')
output.PointData.append(DEIGVEC,'deigVec')
output.PointData.append(DV0,'dv0')
output.PointData.append(DV1,'dv1')
output.PointData.append(DV2,'dv2')
