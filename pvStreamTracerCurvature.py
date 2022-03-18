
##################################################
## When loaded as a programmable filter in Paraview 5.10, 
## this script loads XYZ coordinates of streamline point data to calculate streamline curvature
## Input: streamlines, output: rCirc = R: radius of curvature. UROUT = sqrt(2U/R)
##################################################
## Daniel Carlson
## 2022 March
## Okinawa Institute of Science and Technology
##################################################

import math
import numpy as np

from vtk.numpy_interface import algorithms as algs


X = inputs[0].Points[:,0]
Y = inputs[0].Points[:,1]
Z = inputs[0].Points[:,2]


pSource = np.array(inputs[0].PointData["InjectedPointId"])
cohortTime = np.array(inputs[0].PointData["SeedIds"])




UPT = np.array(inputs[0].PointData["U"])
uPt = UPT[:,0]
vPt = UPT[:,1]
wPt = UPT[:,2]

stepsAll, stepCounts = np.unique(pSource, return_counts = True)
cohortSteps, stepCounts = np.unique(cohortTime, return_counts = True)

xn = np.array(X)
yn = np.array(Y)
zn = np.array(Z)

sourceID = np.array(pSource)
cohortID = np.array(cohortTime)

kk = 0
nn = 0
ptsLen = np.array([None for _ in range(len(stepsAll))])

FTOUT = 0*xn
DEFOUT = 0*xn

UOUT = 0*xn
VOUT = 0*xn
WOUT = 0*xn
radOut = 0*xn
kcOut = 0*xn
curvCoord = 0*xn
rCirc = 0*xn

PMOUT = 0*xn
UROUT = 0*yn
strainOut = 0*xn

for cohortInd in cohortSteps: 
    
    for jj in stepsAll:
    
        indTmp = np.logical_and(sourceID == jj, cohortID == cohortInd)
  
    
        xInd = xn[indTmp]
        yInd = yn[indTmp]
        zInd = zn[indTmp]
        
        uInd = uPt[indTmp]
        vInd = vPt[indTmp]
        wInd = wPt[indTmp]
        
        defInd = defMag[indTmp]
        FTOUT[indTmp]=FT[indTmp]
        

        curvTmp = 0*xInd
        strTmp = 0*xInd
        rTmp = 0*xInd+10000 #infinite radius at streamline endpoints
        windS = 1 #delta point index for finding local curvature
        
        for kk in range(windS,len(xInd)-windS):
            

            XA = np.array([xInd[kk-windS], yInd[kk-windS], zInd[kk-windS]])
            XB = np.array([xInd[kk], yInd[kk], zInd[kk]])
            XC = np.array([xInd[kk+windS], yInd[kk+windS], zInd[kk+windS]])
            
            a = np.linalg.norm(XC - XB)
            b = np.linalg.norm(XC - XA)
            c = np.linalg.norm(XB - XA)
            
           
            s = (a + b + c) / 2
            rTmp[kk] = a*b*c / 4 / np.sqrt(s * (s - a) * (s - b) * (s - c))

        rCirc[indTmp]=rTmp
        UU = np.sqrt(uPt[indTmp]**2 + vPt[indTmp]**2 + wPt[indTmp]**2)
        
        UOUT[indTmp]=UU
        UROUT[indTmp]=UU/rTmp


output.PointData.append(rCirc, 'rCirc')
output.PointData.append(UROUT, 'UROUT')
output.PointData.append(UOUT, 'UOUT')


