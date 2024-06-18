
from math import degrees
from tm import calc_tm_deg
from prettytable import PrettyTable


def test_tm_at_standard_points():
    table = PrettyTable()
    table.field_names = ['Id', 'Lat', 'Lon',
                         'MeridDistOrig', 'MeridDist', 'RadOfCurv', 'ScaleFactor',
                         'GridConv', 'Easting', 'Northing']
    
    standard_points = [('Origin', 0, 84.0),
                       ('Southern', 26.0, 84.0),
                       ('Northern', 30.0, 84.0),
                       ('Standard-line-right', 26.0,84.0+55.0/60.0),
                       ('Standard-line-left', 26.0,84.0-55.0/60.0),
                       ('Right-edge', 26.0,85.5),
                       ('Left-edge', 26.0,82.5)]

    for point in standard_points:
        point_name = point[0]
        lat, lon = point[1], point[2]
        tm_tup = calc_tm_deg(lat,lon)
        
        merid_dist1 = tm_tup[0]
        merid_dist2 = tm_tup[1]
        roc = tm_tup[2]
        sf = tm_tup[3]
        g = degrees(tm_tup[4])
        easting= tm_tup[5]
        northing = tm_tup[6]

        tm_params_lst = [merid_dist1, round(merid_dist2,3), round(roc,3),
                         round(sf, 8), round(g, 6), round(easting, 3), round(northing, 3)]

        

        point_lst = [point_name, lat, round(lon,6)]

        table.add_row(point_lst + tm_params_lst)
    

    return table



def print_everything():
    table = test_tm_at_standard_points()
    print(table)


if __name__ == '__main__':
    print_everything()

