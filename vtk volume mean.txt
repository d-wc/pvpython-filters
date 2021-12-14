import math
import numpy as np
from vtk.numpy_interface import algorithms as algs
from vtk.numpy_interface import dataset_adapter as dsa

UU = inputs[0].PointData["U"]

U0 = mean(UU[:,0])
U1 = mean(UU[:,1])
U2 = mean(UU[:,2])


output.PointData.append(U0, 'Um0')
output.PointData.append(U1, 'Um1')
output.PointData.append(U2, 'Um2')