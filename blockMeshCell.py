
#!/usr/bin/env python

### Calculation of the first layer tickness

"""
Created on 04/03/2020

Formula are given from http://www.cfdyna.com/CFDHT/Y_Plus.html
Updated on 

@author: Carlo Augusto Pasquinucci
email: carlo.a.pasquinucci@gmail.com

"""

#### Version of the tool
V = 1
Sv = 0
###

### import modul
from math import log as loge

#### Input data
#First cell height
Ufreesteam=5 # [m/s]
Density=1.205 # [kg/m^3]  1.205
Viscosity=1.82e-5 # [kg/(m/s)]  1.82e-5
BLL=0.1 # [m] Bondary Layer Length (Hydraulic diameter)
yplus=30 # Desidered yplus
Internal= True #True or False

#BlockMesh
nLayer= 3
expFactor= 1.2
BLCellRatio= 0.5
snappyRefinement= 3
xLimit= 4 # [m]
yLimit= 5 # [m]
zLimit= 3 # [m]
###

### Calculation

#Reynold number
Re=Density*Ufreesteam*BLL/Viscosity

#Friction Factor
if Internal:
	CF=1/(0.79*loge(Re)-1.64)**2
else:
	CF=4*0.074/(Re**0.2)

#Friction Velocity
Uf=(CF/8)**0.5*Ufreesteam

### Result
firstHm=(yplus*Viscosity/Density/Uf*2)*2
firstHmm=firstHm*1000

print("Suggested first cell height ="+ str(firstHm)+" m")
print("Suggested first cell height = "+ str(firstHmm)+" mm")


### Calculation of the dimension of the base mesh
lastBLCell=firstHm*(1.2)**(nLayer-1)
firstCell=lastBLCell/BLCellRatio

print("Min vol cell= "+ str(firstCell))

basedMeshCell=firstCell*snappyRefinement
print("Max vol cell= "+ str(basedMeshCell))

### Calculation of the number of cells in blockMesh
xNCells=round(xLimit/basedMeshCell)
yNCells=round(yLimit/basedMeshCell)
zNCells=round(zLimit/basedMeshCell)


print("Number of cells in x direction= "+ str(xNCells))
print("Number of cells in y direction= "+ str(yNCells))
print("Number of cells in z direction= "+ str(zNCells))