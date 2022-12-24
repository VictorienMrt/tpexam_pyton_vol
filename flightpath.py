from airport import Airport
from flight import Flight
from flightmap import FlightMap
from flightpathbroken import FlightPathBroken
from flightpathduplicate import FlightPathDuplicate

class FlightPath:
    def __init__(self, src_airport: Airport) -> None:

        self.airports2 = [src_airport]
        self.flights2 = []


    def add(self, dst_airport: Airport, via_flight: Flight) -> None:
        if via_flight == None or self.airports2[-1] == None:
            raise FlightPathBroken("Aucun trajet de vol trouvé")
        
        if via_flight.src_code != self.airports2[-1].code:
            raise FlightPathBroken(
                "Aucun vol pour cette aéroport de départ ")
            
        if via_flight.dst_code != dst_airport.code:
            raise FlightPathBroken(
                "Aucun vol pour cette destination")
            
        if via_flight in self.flights2:
            raise FlightPathDuplicate("Le vol est actuellement en provenance de l'aéroport")
        self.flights2.append(via_flight)
        self.airports2.append(dst_airport)


    def flights(self) -> list[Flight]:
        try:
            return self.flights2
        except:
            return ('Aucune liste de vols trouvée')


    def airports(self) -> list[Airport]:
        try:
            return self.airports2
        except:
            return ('Aucune liste d\'aéroports trouvée')


    def steps(self) -> float:
        try:
            return len(self.flights2)
        except:
            return ('Aucune étape de vol trouvée')


    def duration(self) -> float:
        try:
            return sum(flight.duration for flight in self.flights2)
        except:
            return ('Aucune durée de parcours trouvée')
