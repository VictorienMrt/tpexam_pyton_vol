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
            if self.code == airport_code[0]:
                next(airport_code)
                return airport
        return None

flight_map = FlightMap()
flight_map.import_airports(csv_file='aeroports.csv')
flight_map.import_flights(csv_file='flights.csv')
print(flight_map.airports)