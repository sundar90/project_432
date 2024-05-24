import geopandas as gpd
from shapely.geometry import Polygon
import pandas as pd
import json
import ast

def find_overlappping_area(coord1,coord2):
    polygon1 = gpd.GeoSeries([Polygon(coord1)])
    polygon2 = gpd.GeoSeries([Polygon(coord2)])
    intersection = polygon1.intersection(polygon2)
    return intersection.area.iloc[0]

def find_zipcode_for_comm_area(coord):
    df_zip = pd.read_csv('./lookup_tables/zipcode_coordinates.csv')
    area_lst = []
    zipcode = df_zip['zip'].tolist()
    for index,row in df_zip[['coordinates']].iterrows():
        zip_coord = ast.literal_eval(row['coordinates'])
        area_lst.append(find_overlappping_area(zip_coord,coord))
    max_area_ind = area_lst.index(max(area_lst))
    return zipcode[max_area_ind]


def map_zipcode_to_community_area(df_comm):
    df_comm['zip_code'] = df_comm[['coordinates']].apply(lambda x: find_zipcode_for_comm_area(x['coordinates']),axis='columns')
    return df_comm[['zip_code','area_numbe','community']]

if __name__ == '__main__':
    df_comm = pd.read_csv('./lookup_tables/community_coordinates.csv')
    df_comm['coordinates'] = df_comm['coordinates'].apply(ast.literal_eval)
    df_zip = pd.read_csv('./lookup_tables/zipcode_coordinates.csv')
    df_zip['coordinates'] = df_zip['coordinates'].apply(ast.literal_eval)
    df = map_zipcode_to_community_area(df_comm)
    df.to_csv('./output/zipcode_communityarea_mapping.csv',index=False)
    print("success")

