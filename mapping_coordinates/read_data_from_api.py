import pandas as pd
import requests
import json

def read_data(url):
    df = pd.DataFrame()
    response = requests.get(url)
    if response.status_code == 200:
        df = pd.DataFrame(response.json())
    return df

def create_community_data(url):
    df = read_data(url)
    cols = ['community','area_numbe','coordinates']
    df['coordinates'] = df['the_geom'].apply(lambda x: x['coordinates'][0][0])
    df['coordinates'] = df['coordinates'].apply(lambda x: f"{x}")
    df[cols].to_csv('./lookup_tables/community_coordinates.csv',index=False)
    return

def create_zipcode_data(url):
    df = read_data(url)
    cols = ['zip','coordinates']
    df['coordinates'] = df['the_geom'].apply(lambda x: x['coordinates'][0][0])
    df['coordinates'] = df['coordinates'].apply(lambda x: f"{x}")
    df[cols].to_csv('./lookup_tables/zipcode_coordinates.csv',index=False)
    return



if __name__ == '__main__':
    comm_url = 'https://data.cityofchicago.org/resource/igwz-8jzy.json'
    zip_url = 'https://data.cityofchicago.org/resource/unjd-c2ca.json'
    create_community_data(comm_url)
    create_zipcode_data(zip_url)









