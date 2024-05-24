from fastapi import FastAPI,HTTPException
from find_region_given_zipcode import FindLocationOfCoords
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Coordinate(BaseModel):
    lat: float
    lng: float

class CoordinatesList(BaseModel):
    coordinates: List[Coordinate]

@app.post("/find_zipcode/")
def extract_zipcode(coord: List[float]):
    try:
        location_finder =  FindLocationOfCoords(coord)
        zipcodes = location_finder.find_zipcode()
        if not zipcodes:
            raise HTTPException(status_code=404, detail="Zipcode not found")
        return zipcodes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/find_community_area/")
def extract_community_area(coord: List[float]):
    try:
        location_finder =  FindLocationOfCoords(coord)
        zipcodes = location_finder.find_community_area()
        if not zipcodes:
            raise HTTPException(status_code=404, detail="Community area not found")
        return zipcodes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)