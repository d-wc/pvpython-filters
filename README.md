# pvpython-filters
Personal python scripts for Paraview 5.11.


<img src="https://user-images.githubusercontent.com/41755304/151687179-ac5b0db5-89a9-4604-bc42-145774f5dfa5.png" width="500" height="500">


Diffusive Strip/Ring operate in Paraview as python filters of the diffusive strip method to study scalar mixing from particle tracks. DiffusiveRing expects a circular particle source.

Input: ParticleTracer output. Output: lines connecting points with the same age, with inverse neighbor distance, central neighborhood angle, and displacement from the parcel centroid. 

Meunier, Patrice, and Emmanuel Villermaux. "The diffusive strip method for scalar mixing in two dimensions." Journal of fluid mechanics 662 (2010): 134-172.

https://www.irphe.fr/~fragmix/publis/MV2010.pdf


pvStreamTracerCurvature operates on paraview streamlines, isolates streams by injection point, then calculates the local radius of curvature along each streamline. Used for viscoelastic instability criterion. 

Carlson, D., Toda-Peters, K., Shen, A., & Haward, S. (2022). Volumetric evolution of elastic turbulence in porous media. Journal of Fluid Mechanics, 950, A36. doi:10.1017/jfm.2022.836

https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/volumetric-evolution-of-elastic-turbulence-in-porous-media/4FDBF7BB84C2F0A5C615254B9CEA970B

pvDimensionalStrike takes a 3D volume with velocity U and a vector valid scalar "isValid", averaging valid vectors along a dimension to reduce to 2.

pvNormalPlane is applied to a slice plane with velocity U, finds the orientation of the primary flow, and rotates the plane to be orthogonal to flow

Multi-block datasets seem to break numpy, run mergeBlocks to convert the input if needed. 

