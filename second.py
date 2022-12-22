import csv

class Airport:
    def __init__(self, name: str, code: str, lat: float, long: float):
        self.name = name
        self.code = code
        self.lat = lat
        self.long = long

class Flight:
    def __init__(self, src_code: str, dst_code: str, duration: float):
        self.src_code = src_code
        self.dst_code = dst_code
        self.duration = duration

class FlightMap:
    def __init__(self):
        self.airports = []
        self.flights = []
        
    def import_airports(self, csv_file: str)-> None:
        with open(csv_file, "r") as f:
            reader = csv.reader(f)
            next(reader)
            self.airports = [Airport(name, code, float(lat.replace('"', '')), float(long.replace('"', ''))) 
                            for name, code, lat, long in reader]
    
    def import_flights(self, csv_file: str)-> None:
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            self.flights = [Flight(src_code, dst_code, float(duration.replace('"', ''))) 
                           for src_code, dst_code, duration in reader]
            
    def airports(self) -> list[Airport]:
        return self.airports
    
    def flights(self) -> list[Flight]:
        return self.flights
    
   
    def airport_find(self, airport_code: str) -> Airport:
        for airport in self.airports:
            if airport.code == airport_code:
                return airport
        return None
    
    def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> bool:
        flights = [f for f in self.flights if f.src_code == src_airport_code and f.dst_code == dst_airport_code]
        return bool(flights)
    
    def flights_where(self, airport_code: str) -> list[Flight]:
        flights = [f for f in self.flights if f.src_code == airport_code or f.dst_code == airport_code]
        return flights

    def airports_from(self, airport_code: str) -> list[Airport]:
        flights = self.flights_where(airport_code)
        airports = [self.airport_find(f.dst_code) for f in flights]
        return airports

flight_map = FlightMap()
flight_map.import_airports(csv_file='aeroports.csv')
flight_map.import_flights(csv_file='flights.csv')
airport = flight_map.airport_find
flights = flight_map.flights_where
airports = flight_map.airports_from
# print(flight_map.airports)
print(airport)
print(flights)
print(airports)