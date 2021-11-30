# pvpython-filters
Personal python scripts for Paraview 5.10

paraview_DiffusiveStrip is a python filter for paraview of the diffusive strip method to study scalar mixing from particle tracks. 

Input: particle tracers. Output: lines connecting points with the same age, with inverse neighbor distance and central neighborhood angle. 



Meunier, Patrice, and Emmanuel Villermaux. "The diffusive strip method for scalar mixing in two dimensions." Journal of fluid mechanics 662 (2010): 134-172.

https://www.irphe.fr/~fragmix/publis/MV2010.pdf

paraview_LavisionTecplot is a plugin for importing a tecplot-formatted volume exported from a transient Lavision 3D PIV solution. Import units mm-m/s and a user-specified DT (time scale).  

