from datamod import a, f, b, e, LON0, LAT0, k0, E0, N0
from math import degrees, radians, sin, cos, tan, sqrt

# calculate twrhonupsi
def calc_rho(fi, lamda, lamda0 = LON0):
    """
    Compute intermediate terms t, w, rho, nu, psi.

    Args:
        fi (float): latitude (in radians unit)
        lamda (float): longitude (in radian unit)

    Returns: t, w, rho, nu, psi 
    """
    t = tan(fi)
    w = lamda - lamda0
    
    rho = a*(1 - e**2)/(1 - e**2*sin(fi)**2)**(3/2)
    nu = a / (1 - e**2*sin(fi)**2)**(1/2)
    psi = nu/rho

    return(t, w, rho, nu, psi)

# calculate meridian distance
def calc_meridian_dist(fi):
    """
    Compute meridian distance of a given point.

    Args:
        fi (float): latitude (in radians unit)

    Returns: meridian distance of latitude of origin,
            and meridian distance of given point
    """
    m0 = 0.0
    A0 = 1 - (e**2/ 4) - (3 * e**4 / 64) - (5 * e**6 / 256)
    A2 = 3/8 * (e**2 + e**4/4 + 15*e**6/128)
    A4 = 15/256 * (e**4 + 3*e**6/4)
    A6 = 35*e**6 / 3072
    m = a*(A0*fi - A2*sin(2*fi) + A4*sin(4*fi) - A6*sin(6*fi))

    return (m0, m)   
    

def calc_radius_of_curvature(fi, lamda):
    """
    Compute radius of curvature to a given point.

    Args:
        fi (float): latitude (in radians unit)
        lamda (float): longitude (in radian unit)

    Returns: radius of curvature  
    """
    rho_tup = calc_rho(fi, lamda)
    rho, nu = rho_tup[2], rho_tup[3]
    r = sqrt(rho*nu*k0**2)

    return r
    

def calc_scale_factor(fi, lamda, lamda0 = LON0):
    """
    Compute point scale factor.

    Args:
        fi (float): latitude (in radians unit)
        lambda (float): longitude (in radian unit)

    Returns: scale factor
    """
    
    rho_tup = calc_rho(fi, lamda, lamda0)
    t, w, psi = rho_tup[0], rho_tup[1], rho_tup[4]
       
    term1 = w**2/2 * psi*cos(fi)**2
    term2 = w**4/24*cos(fi)**4 *(4*psi**3*(1-6*t**2) + psi**2*(1+24*t**2) - 4*psi*t**2)
    term3 = w**6/720*cos(fi)**6 * (61 - 148*t**2 + 16*t**4)
    k = k0*(1 + term1 + term2 + term3)

    return k
    

def calc_line_scale_factor():
    pass

def calc_grid_convergence(fi, lamda, lamda0 = LON0):
    """
    Compute grid convergence.

    Args:
        fi (float): latitude (in radians unit)
        lambda (float): longitude (in radian unit)

    Returns: grid convergence
    """
    rho_tup = calc_rho(fi, lamda, lamda0)
    t, w, psi = rho_tup[0], rho_tup[1], rho_tup[4]
        
    term1 = -w*sin(fi)
    term2 = -w**3/3*sin(fi)*cos(fi)**2*(2*psi**2-psi)
    term3 = -w**5/15*sin(fi)*cos(fi)**4*(psi**4*(11-24*t**2)-psi**3*(11-36*t**2)\
                                   +2*psi**2*(1-7*t**2)+psi*t**2)
    term4 = -w**7/315 * sin(fi) * cos(fi)**6*(17-26*t**2+2*t**4)
    gama = term1 + term2 + term3 + term4
    
    return gama

def lon_to_easting(fi, lamda, lamda0 = LON0):

    rho_tup = calc_rho(fi, lamda, lamda0)
    t, w, nu, psi = rho_tup[0], rho_tup[1],rho_tup[3], rho_tup[4]

    term1 = w**2/6 * cos(fi)**2 * (psi - t**2)
    term2 = w**4/120 * cos(fi)**4 *(4*psi**3*(1-6*t**2) + psi**2*(1+8*t**2) - psi*(2*t**2)\
                                  + t**4)
    term3 = w**6/5040 * cos(fi)**6 * (61 - 479*t**2 + 179*t**4 - t**6)
    E1 = k0*nu*w*cos(fi)*(1 + term1 + term2 + term3)
    E = E1 + E0

    return E
    

def lat_to_northing(fi, lamda, lamda0 = LON0):
    
    rho_tup = calc_rho(fi, lamda, lamda0)
    t, w, rho, nu, psi = rho_tup[0], rho_tup[1], rho_tup[2], rho_tup[3], rho_tup[4]

    m0,m = calc_meridian_dist(fi)
    
    term1 = w**2/2 *nu*sin(fi)*cos(fi)
    term2 = w**4/24 *nu*sin(fi)*cos(fi)**3*(4*psi**2 + psi - t**2)
    term3 = w**6/720*nu*sin(fi)*cos(fi)**5 * (8*psi**4*(11 - 24*t**2) - 28*psi**3*(1 - 6*t**2) \
                                       + psi**2*(1 - 32*t**2) - psi*(2*t**2) + t**4)
    term4 = w**8/40320 *nu*sin(fi)*cos(fi)**7 *(1385 - 3111*t**2 + 543*t**4 - t**6)
    N1 = k0*(m-m0 + term1 +term2 + term3 + term4)
    N = N1 + N0

    return N

def calc_tm_rad(fi, lamda, lamda0 = LON0):
    """
    Compute transeverse mercator parameters.

    Args:
        fi (float): latitude (in radians)
        lamda (float): longitude (in radians)
        lamda0 (float): longitude of central meridian (in radians)

    Returns: m0, m, r, k, g, e, n

    """
    
    m0, m = calc_meridian_dist(fi)              # compute meridian distance
    r = calc_radius_of_curvature(fi, lamda)     # compute roc
    k = calc_scale_factor(fi, lamda, lamda0)            # compute scale factor
    g = calc_grid_convergence(fi, lamda, lamda0)        # compute grid conv
    e = lon_to_easting(fi, lamda, lamda0)               # compute easting
    n = lat_to_northing(fi, lamda, lamda0)              # compute norting

    tm_tup = (m0, m, r, k, g, e, n)             # returns tuple of every parameters

    return tm_tup

def calc_tm_deg(fi, lamda, lamda0 = 84):
    """
    Receive fi, lamda, lamda0 in degrees,
    convert these values to radians,
    send these values to calc_tm_rad function,
    receive calculated transeverse mercator parameters from calc_tm_rad function

    Args:
        fi (float): latitude (in degrees)
        lamda (float): longitude (in degrees)
        lamda0 (float): central meridian longitude (in degrees)

    Returns: tm_tup (transeverse mercator parameters tuple from calc_tm_rad function)
    """
    
    fi, lamda, lamda0 = radians(fi), radians(lamda), radians(lamda0)
    tm_tup = calc_tm_rad(fi, lamda, lamda0)

    return tm_tup
    

def test():
    # Test
    print(calc_tm_deg(0,84))
    print(calc_tm_deg(26,84))
    print(calc_tm_deg(30,84))
    print(calc_tm_deg(26,84+55/60))
    print(calc_tm_deg(26,84-55/60))
    print(calc_tm_deg(26,85.5))
    print(calc_tm_deg(26,82.5))

if __name__ == '__main__':
    test()
