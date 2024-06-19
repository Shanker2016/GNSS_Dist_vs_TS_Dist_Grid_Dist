
Computing Transverse Mercator

These integrated modules compute scale factor; elevation factor; and combined factor.
Scale factor is due to Transverse Mercator projection.
Elevation factor is due to elevation of site where distance measurements took place.

Combined factor = scale factor X elevation factor.

Data setting/ parameters module:
	>> datamod.py : contains Everest1830 ellipsoid parameters; MUTM projection parameters, Earth Radius, and others.

Transverse Mercator computing module:
	>> tm : calculate meridian distance, calculate radius of curvature, calculate scale factor, calculate grid convergence, calculate easting and northing
	>> tm_test_at_ntmp_points: test of tm module's correctness with ENTMP and WNTMP coordinates
	>> tm_test_at_standard_points: test of tm module's correctness at central meridian, at secant lines, and edge of zone
	>> sfdemo.py : compute scale factor at various longitude intervals. It is a demonstration module.

Elevation factor computing module:
	>> elevfactor.py : computes elevation factor.
	>> efdemo.py : compute elevation factor at various interval of elevation. It is a demonstration module.

Combined factor computing module:
	>> cfdemo.py : computes combined factor. Combined factor = Scale Factor X Elevation Factor.
	>> cfdemor.py : similar to cfdemo.py but for different data input.
	
Link to paper:
	>> DOI: https://doi.org/10.3126/njg.v23i1.66049 
	
	