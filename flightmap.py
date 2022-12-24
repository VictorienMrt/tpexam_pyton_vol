import csv
from airport import Airport
from flight import Flight
from flightpathbroken import FlightPathBroken


class FlightMap:
    def __init__(self):
        self.airports_list = []
        self.flights_list = []
        
        
    def import_airports(self, csv_file: str) -> None:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file, quotechar='"', skipinitialspace=True)
            for row in reader:
                name, code, lat, longitude = row
                self.airports_list.append(
                    Airport(name, code, float(lat), float(longitude)))
    
    
    def import_flights(self, csv_file: str)-> None:
        try:
            with open(csv_file, 'r') as f:
                reader = csv.reader(f)
                next(reader)
                self.flights_list = [Flight(src_code, dst_code, float(duration.replace('"', ''))) 
                                        for src_code, dst_code, duration in reader]
        except:
            return ('Aucun fichier de vols trouvé')
            
            
    def airports(self) -> list[Airport]:
        try:
            return self.airports_list
        except:
            return ('Aucune liste d\'aéroports trouvée')
    
    
    def flights(self) -> list[Flight]:
        try:
            return self.flights_list
        except:
            return ('Aucune liste de vols trouvée')
    
   
    def airport_find(self, airport_code: str) -> Airport:
            for airport in self.airports_list:
                if airport.code == airport_code:
                    return airport
            return None
        
        
    def airport_find_error(self, airport_code: str) -> Airport:
        
            for airport in self.airports_list:
                if airport.code == airport_code:
                    return airport   
            raise FlightPathBroken("L'aéroport n'a pas été trouvé")


    def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> bool:
        for flight in self.flights_list:
            if flight.src_code == src_airport_code and flight.dst_code == dst_airport_code:
                return flight
        return None


    def flights_where(self, airport_code: str) -> list[Flight]:
        try:
            flights = []
            for flight in self.flights_list:
                if flight.src_code == airport_code or flight.dst_code == airport_code:
                    flights.append(flight)
            return flights
        except:
            return ('Aucun trajet trouvé pour ce vol')


    def airports_from(self, airport_code: str) -> list[Airport]:
        try:
            airports = []
            for flight in self.flights_where(airport_code):
                if flight.src_code == airport_code:
                    airport = self.airport_find(flight.dst_code)
                    if airport:
                        airports.append(airport)
            return airports
        except:
            return ('Aucun vol en provenance trouvé')
        