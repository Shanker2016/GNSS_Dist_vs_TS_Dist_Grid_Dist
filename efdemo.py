
from datamod import hd, elev_range
from elevfactor import elevation_factor
from prettytable import PrettyTable
import pandas as pd



def elev_factor_demo_table():
    table = PrettyTable()
    columns = ['Ground Distance', 'Mean-Elevation', 'Elevation Factor', 'Ellipsoid Distance']
    table.field_names = columns

    elev_factor_demo_data = []
    
    for hm in elev_range: # hm is elevation value
        ef = elevation_factor(hm) # Elevation factor
        s0  = hd * ef # ellipsoid distance
        elev_factor_tup = [hd, hm, round(ef, 8), round(s0,3)]
        table.add_row(elev_factor_tup)

        elev_factor_demo_data.append(elev_factor_tup)
    
    df = pd.DataFrame(elev_factor_demo_data, columns = columns)
    df.to_csv('output/efdemo.csv', index = False)
    
    
    return table
        
        

def print_everything():
    table = elev_factor_demo_table()
    print(table)


if __name__ == '__main__':
    print_everything()
