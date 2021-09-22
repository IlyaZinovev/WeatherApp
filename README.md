# Weather App
## About
Web service made with Flask which takes weather data and aggregate it
## How to install
1. add environment variable `Weather_API_Key` with API key from http://weatherapi.com
2. `pip install -r requirements.txt`
## How to run
1. `flask run`
2. `GET \weather?city=<city>&days=<n>` where `<city>` is the name of city and `<n>` is the number of days for aggregating
## Response
As a result you you get a `.json` which contains information about temperature, humidity and pressure for the last `<n>` days
### Example
```
{
 "city": "Saint-Petersburg",
 "from": "2021-09-10",
 "to": "2021-09-15",
 "temperature_c": {
   "average": 25.0,
   "median": 24.5,
   "min": 20.1,
   "max": 29.3
 },
 "humidity": {
   "average": 55.4,
   "median": 58.1,
   "min": 43.1,
   "max": 82.4
 },
 "pressure_mb": {
   "average": 1016.0,
   "median": 1016.5,
   "min": 1015.1,
   "max": 1017.3
 }
}
```
