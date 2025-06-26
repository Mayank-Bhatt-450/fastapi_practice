import fastapi,requests
import pydantic
import typing 
from fastapi.middleware.cors import CORSMiddleware


class CitiesResponse(pydantic.BaseModel):
    cities:typing.List[str] = pydantic.Field('Delhi',description='city name')
app = fastapi.FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/cities/{city_prefix}',response_model=CitiesResponse)
def get_cities(city_prefix:str)->list:
    try:
        response= requests.get('https://samples.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10&appid=b6907d289e10d714a6e88b30761fae22')
        response= response.json()
        cities_metadata_list=response.get('list',[])
        response=[]
        if cities_metadata_list and city_prefix:
            for city in  cities_metadata_list:
                if (city.get('name','')[:len(city_prefix)]).lower() ==city_prefix.lower():
                    response.append(city['name'])

        return {"cities":sorted(response)}
    except Exception as ex:
        print(ex)