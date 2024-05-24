### About the code

The code  will read two API's which has boundary information of zipcode and community area and performs the following actions
1. Preprocesses information and creates lookup tables under lookup_tables folder
2. creates map between zipcode and community area
3. API call which will accept  a pair of coordinates and return the  zipcode and community area it belongs to

### How to use

1. Run the read_data_from_api.py script only if you need to regenerate the csv files in the lookup table. otherwise no need to run it
2. Run the create_zipcode_commarea_mapping.py script to generate the zip code and community area mapping table in csv format under the output table
3. Run the find_region_give_zipcode.py. it will host the api in the port 8080
   4. you can access the api using requests like the one in the example below

````
url = "http://localhost:8000/find_community_area"

url = "http://localhost:8000/find_zipcode"

input = [-87.75528165409671, 41.97509574219451]

response = requests.post(url,json=input)

output = response.json()
````