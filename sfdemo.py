
from datamod import s, latx, lon_spacing_relative
from tm import calc_tm_deg
from prettytable import PrettyTable
import pandas as pd


def scale_factor_demo_table():
    table = PrettyTable()
    fields = ['EllipDist', 'LonSpacing', 'Lat', 'LonDD', 'ScaleFactor', 'GridDist']
    table.field_names = fields

    scale_factor_demo_data = []

    for lon_space in lon_spacing_relative:        
        lon_dd = 84.0 + lon_space / 60.0
        
        sf = calc_tm_deg(latx, lon_dd)[3]
        s0 = s * sf

        scale_factor_lst = [s, lon_space, latx, round(lon_dd,8), round(sf, 8), round(s0, 3)]
        table.add_row(scale_factor_lst)

        scale_factor_demo_data.append(scale_factor_lst)

    df = pd.DataFrame(scale_factor_demo_data, columns = fields)
    df.to_csv('output/sfdemo.csv', index = False)

    return table

def print_everything():
    table = scale_factor_demo_table()
    print(table)


if __name__ == '__main__':
    print_everything()
