from math import sqrt, radians

# Constants Everest1830 ellipsoid
a = 6377276.345     # semi-major axis of Everest1830 (in meters)
f = 1 / 300.8017    # flattening of same ellipsoid
b = a * (1-f)       # semi-minor axis of same ellipsoid
e = sqrt((a**2 - b**2) / a**2)  # eccentricity of same ellipsoid

# Constants of MUTM84 grid
# central meridian is 84 Deg E longitude
LON0 = radians(84)  # central meridan (in radians)
LAT0 = radians(0)   # origin of latitude (in radians)
k0 = 0.9999         # scale factor along central meridian (unitless)
E0 = 500000         # false easting (in meters)
N0 = 0              # false northing (in meters)


# Constants for elevation factors
RADIUS =  6371000   # radius of the earth (in meters)

# sythetic data for elevation factor demonstration
hd = 100.0  # Horizontal distance at mean elevation (in meters)
elev_range = [0, 100, 200, 400, 500, 600, 800, 1000,
              1200, 1400, 1500, 1600, 1800, 2000, 2200,
              2400, 2500, 2600, 2800, 3000]     # Elevation range (in meters)

# synthetic data for scale factor demonstration
s = 100.0       # ellipsoid distance
latx = 28.0   # a sample latitude 
lon_spacing_relative = [0, 10, 20, 30, 40, 50, 55, 60, 70, 80, 90] # (in minutes)
lon_spacing_right_abs = [84 + value / 60.0 for value in lon_spacing_relative]
lon_spacing_left_abs = [84 - value / 60.0 for value in lon_spacing_relative]

# print ellipsoid details
def print_ellipsoid_det():
    print('\n')
    print('Ellipsoid params')
    print('work on progress...')

# print MUTM84 grid details
def print_mutm84_det():
    print('\n')
    print('proj params')
    print('work on progress...')

# print hd and elevation range details
def print_elev_range_det():
    print('Horizontal Distance:'.ljust(20), str(hd)+' m')
    print('Following is the elevation range')
    for elevation in elev_range:
        print(str(elevation)+' m')


def print_everything():
    print_elev_range_det()
    print_ellipsoid_det()
    print_mutm84_det()


if __name__ == '__main__':
    print_everything()

