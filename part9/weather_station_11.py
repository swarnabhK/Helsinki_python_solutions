class WeatherStation:
    def __init__(self, station_name) -> None:
        self.__station_name = station_name
        self.__observations = []

    def add_observation(self,observation):
        self.__observations.append(observation)

    def latest_observation(self):
        if(len(self.__observations)>0):
            return self.__observations[-1]
        return ""
    
    def number_of_observations(self):
        return len(self.__observations)
    
    def __str__(self) -> str:
        return f"{self.__station_name}, {self.number_of_observations()} observations"
    

station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())

station.add_observation("Thunderstorm")
print(station.latest_observation())

print(station.number_of_observations())
print(station)
