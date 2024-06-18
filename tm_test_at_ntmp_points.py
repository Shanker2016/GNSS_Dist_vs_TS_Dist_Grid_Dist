from prettytable import PrettyTable
from tm import calc_tm_deg

def read_from_txt(fname):
    ntmp_coord = []
    with open(fname, 'r') as fin:
        records = fin.readlines()
        for record in records[1:]:
            record = record.split()
            ptid = record[0]
            lat_deg, lat_min, lat_sec = int(record[1]), int(record[2]), float(record[3])
            lon_deg, lon_min, lon_sec = int(record[4]), int(record[5]), float(record[6])
            ht = record[7]
            northing, easting = float(record[9]), float(record[10])

            lat_dd = lat_deg + lat_min / 60.0 + lat_sec / 3600.0
            lon_dd = lon_deg + lon_min / 60.0 + lon_sec / 3600.0

            point_coord= [ptid, lat_dd, lon_dd, northing, easting]
            ntmp_coord.append(point_coord)

    return ntmp_coord


def calc_tm_deg_x(lat, lon, lon0):
    tm_tup = calc_tm_deg(lat, lon, lon0)
    return tm_tup
    

def name_x1():
    fname_wntmp = 'test_data/test_point_wntmp.txt'
    fname_entmp = 'test_data/test_point_entmp.txt'
    fname_entmp_2 = 'test_data/test_point_entmp_2.txt'

    lon0_wntmp = 81.0
    lon0_entmp = 84.0
    lon0_entmp2 = 87.0

    fname_lst = [(fname_wntmp, lon0_wntmp),
                 (fname_entmp, lon0_entmp),
                 (fname_entmp_2, lon0_entmp2)]

    ntmp_coord_computed_ew = []

    for fname, lon0 in fname_lst:
        ntmp_coord_computed = []
        ntmp_coord = read_from_txt(fname)
        for point in ntmp_coord:
            ptid = point[0]
            lat, lon = point[1], point[2]
            easting, northing = point[3], point[4]
        
            tm_tup = calc_tm_deg_x(lat,lon,lon0)            

            ntmp_coord_computed.append(point + [lon0] + list(tm_tup))
            
        ntmp_coord_computed_ew.append(ntmp_coord_computed)

    return ntmp_coord_computed_ew

def generate_table_ntmp():
    table = PrettyTable()
    table.field_names = ['Id', 'Lat', 'Lon', 'Lon0', 'CompEasting', 'BenchmarkEasting',
                         'CompNorthing', 'BenchmarkNorthing']
    
    ntmp_coord_computed_ew = name_x1()
    for ntmp in ntmp_coord_computed_ew:
        for point in ntmp:
            ptid = point[0]
            lat, lon, northing, easting = point[1], point[2], point[3], point[4]

            lon0  = point[5]

            m0, m = point[6], point[7]
            r, k, g = point[8], point[9], point[10]
            e,  n = point[11], point[12]

            table.add_row([ptid, round(lat,8), round(lon, 8), lon0, round(e, 3), round(easting, 3), round(n,3),
                           round(northing, 3)])
    return table

    #point + [lon0] + list(tm_tup)
    #point_coord= [ptid, lat_dd, lon_dd, northing, easting]
    #tm_tup = (m0, m, r, k, g, e, n)  
    
    
        
def run_read_from_txt():
    table = PrettyTable()
    table.field_names = ['PtId', 'Lat', 'Lon', 'Northing', 'Easting']
    
    fname1 = 'test_data/test_point_wntmp.txt'
    fname2 = 'test_data/test_point_entmp.txt'

    fname_lst = [fname1, fname2]
    for fname in fname_lst:
        ntmp_coord = read_from_txt(fname)
        for point in ntmp_coord:
            table.add_row(point)

    return table

def print_read_from_txt():
    table = run_read_from_txt()
    print(table)

def print_generate_table_ntmp():
    table = generate_table_ntmp()
    print(table)
    
    
    
def print_everything():
    print_read_from_txt()
    print_generate_table_ntmp()
    
if __name__ == '__main__':
    print_everything()
