from datamod import *

def elevation_factor(hm):
    """
    Compute elevation factor.

    Args:
        hm (float):mean-elevation (orthometric, ellipsoidal or level height)

    Returns:
        float: Elevation factor.
    """

    # Compute elevation factor
    elevation_factor = RADIUS / (RADIUS + hm)

    return elevation_factor


def test():
    # Test the elevation_factor function
    h1 = 100.0 # Station 1 height.
    h2 = 200.0 # Station 2 height.
    hm = (h1 + h2) / 2
    EF = elevation_factor(hm)
    print("Elevation factor:", EF)

if __name__ == '__main__':
    test()
