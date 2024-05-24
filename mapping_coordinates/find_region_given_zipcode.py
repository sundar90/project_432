import pandas as pd
import ast

def find_if_coord_inside(boundary,coord):
    # boundary = ast.literal_eval(boundary)
    x_min,x_max = min([coord[0] for coord in boundary]),max([coord[0] for coord in boundary])
    y_min,y_max = min([coord[1] for coord in boundary]),max([coord[1] for coord in boundary])
    x = coord[0]
    y = coord[1]
    if (x_min <= x <= x_max) and (y_min <= y <= y_max):
        return True
    return False

class FindLocationOfCoords:
    def __init__(self,coord):
        self.df_comm = pd.read_csv('./lookup_tables/community_coordinates.csv')
        self.df_comm['coordinates'] = self.df_comm['coordinates'].apply(ast.literal_eval)
        self.df_zip = pd.read_csv('./lookup_tables/zipcode_coordinates.csv')
        self.df_zip['coordinates'] = self.df_zip['coordinates'].apply(ast.literal_eval)
        self.coord = coord

    def find_zipcode(self):
        try:
            self.df_zip['match_found'] = self.df_zip.apply(lambda x: find_if_coord_inside(x['coordinates'],self.coord),axis='columns')
            return self.df_zip[self.df_zip['match_found'] == True]['zip'].values.tolist()
        except Exception as e:
            return []

    def find_community_area(self):
        try:
            self.df_comm['match_found'] = self.df_comm.apply(lambda x: find_if_coord_inside(x['coordinates'],self.coord),axis='columns')
            return self.df_comm[self.df_comm['match_found'] == True]['community'].values.tolist()
        except Exception as e:
            return []

if __name__ == '__main__':
    coord = [-87.75528165409671, 41.97509574219451]
    find_location = FindLocationOfCoords(coord)
    zipcode = find_location.find_zipcode()
    community_area = find_location.find_community_area()
    print("success")
