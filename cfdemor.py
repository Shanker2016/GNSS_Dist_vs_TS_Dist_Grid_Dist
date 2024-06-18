from math import sqrt
from elevfactor import elevation_factor
from tm import calc_tm_deg
from prettytable import PrettyTable
import pandas as pd



def read_from_txt(fname):
    gnss_coord = {}
    
    with open(fname, 'r') as fin:
        records = fin.readlines()
        
        for record in records[1:]:
            record = record.split()
            
            ptid =  record[0]
            lat_deg, lat_min, lat_sec = int(record[1]), int(record[2]), float(record[3])
            lon_deg, lon_min, lon_sec = int(record[4]), int(record[5]), float(record[6])
            ht = float(record[7])
            easting, northing = float(record[8]), float(record[9])

            lat_dd = lat_deg + lat_min / 60.0 + lat_sec / 3600.0
            lon_dd = lon_deg + lon_min / 60.0 + lon_sec / 3600.0

            point_coord= [ptid, lat_dd, lon_dd, ht, easting, northing]

            gnss_coord[ptid] = point_coord

    return gnss_coord

def read_from_txt_ts(fname):
    ts_dist = {}
    
    with open(fname, 'r') as fin:
        records = fin.readlines()
        
        for record in records[1:]:
            record = record.split()

            pt1, pt2, dist = record[0], record[1], float(record[2])
            side = pt1 + '-' + pt2
            ts_dist[side] = dist
            
    return ts_dist
    


def comb_factor_demo_real_table():
    table = PrettyTable()
    fields = ['Side', 'GridDist', 'K', 'EllipDist', 'MeanElev',
                         'ElevFactor' ,'GroudDist', 'CombFactor', 'GroundDist2',
                         'MeasGroundDist', 'DiffMeasComp']
    table.field_names = fields

    ts_dist = read_from_txt_ts('ts_distance_kailali.txt')
    gnss_coord = read_from_txt('gnss_point_kailali.txt')

    comb_factor_real_data = []

    for side in ts_dist:
        side1 = side.split("-")
        ptid1, ptid2 = side1[0], side1[1]
        lat1, lon1 = gnss_coord[ptid1][1],gnss_coord[ptid1][2]
        lat2, lon2 = gnss_coord[ptid2][1],gnss_coord[ptid2][2]
        x1, y1 = gnss_coord[ptid1][4],gnss_coord[ptid1][5]
        x2, y2 = gnss_coord[ptid2][4],gnss_coord[ptid2][5]
        ht1, ht2 = gnss_coord[ptid1][3],gnss_coord[ptid2][3]
        
        s0 = sqrt((x2-x1)**2 + (y2-y1)**2)

        k1 = calc_tm_deg(lat1, lon1, lamda0 = 81.0)[3]
        k2 = calc_tm_deg(lat2, lon2, lamda0 = 81.0)[3]
        km = (k1 + k2) / 2
        K = (k1 + k2 + 4*km) / 6
        s = s0 * 1 / K
        
        hm = (ht1 + ht2) / 2
        ef = elevation_factor(hm)

        hd = s * 1 / ef

        cf = K * ef
        hd_cf = s0 * 1 / cf

        hd_meas = ts_dist[side]
        hd_delta = hd - hd_meas
        
        #print(x1, y1)        
        #print(ptid1, ptid2)

        comb_factor_tup = [side, round(s0, 3), round(K, 8), round(s, 3),
                           round(hm, 3), round(ef, 8), round(hd, 3), round(cf, 8),
                           round(hd_cf, 3), hd_meas, round(hd_delta, 3)]
        table.add_row(comb_factor_tup)

        comb_factor_real_data.append(comb_factor_tup)

    df = pd.DataFrame(comb_factor_real_data, columns = fields)
    df.to_csv('output/cfdemor.csv', index = False)

    return table


def print_everything():
    table = comb_factor_demo_real_table()
    print(table)

    read_from_txt_ts('ts_distance_kailali.txt')


if __name__ == '__main__':
    print_everything()
