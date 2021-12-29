# importing googlemaps module
import googlemaps
  
# Requires API key
gmaps = googlemaps.Client(key='Your_API_key')
  
# Requires cities name
dist = gmaps.distance_matrix('Hyderabad','Vizag')['rows'][0]['elements'][0]
  
# Printing the result
print(dist)
