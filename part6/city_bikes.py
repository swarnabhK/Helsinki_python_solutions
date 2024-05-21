# First, write a function named get_station_data(filename: str). This function should read the names and locations of all the stations in the file, and return them in a dictionary with the following format:



# tee ratkaisu tänne
# Write your solution here

import math

def create_list(fn):
  res = []
  with open(fn,"r") as file:
    for line in file:
      line = line.strip()
      line = line.split(";")
      if line[0] == 'Longitude':
        continue
      res.append(line)
  return res

def get_station_data(fn):
  stations = create_list(fn)
  res = {}
  for s in stations:
    res[s[3]] = (float(s[0]),float(s[1]))
  return res

def distance(stations, s1, s2):
  lo1,lo2 = stations[s1][0], stations[s2][0]
  la1,la2 = stations[s1][1], stations[s2][1]

  x_km = (lo1 - lo2) * 55.26
  y_km = (la1 - la2) * 111.2
  d = math.sqrt(x_km**2 + y_km**2)
  return d

def greatest_distance(stations):
  sts = list(stations.keys())
  g,g1,g2 = -float("inf"),"",""
  for i in range(len(sts)):
    for j in range(i+1,len(sts)):
      d = distance(stations,sts[i],sts[j])
      if d>g:
        g,g1,g2 = d,sts[i],sts[j]
  return g1,g2,g


print(create_list("stations1.csv"))
stations = get_station_data('stations1.csv')
d = distance(stations, "Designmuseo", "Hietalahdentori")
print(d)
d = distance(stations, "Viiskulma", "Kaivopuisto")
print(d)


stations = get_station_data('stations1.csv')
station1, station2, greatest = greatest_distance(stations)
print(station1, station2, greatest)