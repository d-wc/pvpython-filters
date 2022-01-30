# pvpython-filters
Personal python scripts for Paraview 5.10

![image](https://user-images.githubusercontent.com/41755304/151687132-faa0a122-8709-4952-97c8-f323cf1da35d.png| width=50)



Diffusive Strip/Ring operate in Paraview as python filters of the diffusive strip method to study scalar mixing from particle tracks. DissusiveRing expects a circular particle source.

Input: ParticleTracer output. Output: lines connecting points with the same age, with inverse neighbor distance, central neighborhood angle, and displacement from the parcel centroid. 

Meunier, Patrice, and Emmanuel Villermaux. "The diffusive strip method for scalar mixing in two dimensions." Journal of fluid mechanics 662 (2010): 134-172.

https://www.irphe.fr/~fragmix/publis/MV2010.pdf


