# importing googlemaps module
import googlemaps

# Requires API key
gmaps = googlemaps.Client(key='API KEY')

#PASTE YOUR API KYE IN PLACE OF 'API KEY'

l1=['Thirupathi','Sri Kalahasthi','Vizag','Araku','Harsley Hills','Gandikota','Lambasingi','Manthralayam','Papikondalu','Vijayawada','Lepakshi','Amaravathi','Talakunta Falls(Thirupathi)','Rajamundry','Bellam Caves (Kurnool)','Kadapa','SriSailam','Nallamala hills','Ahobilam']
l3=[]

for i in l:
    for j in l:
        if(i!=j):
            dist = gmaps.distance_matrix(i,j)['rows'][0]['elements'][0]
            l3.append((i,j,(dist['distance'])['text']))
        

print(l3)




#to remove duplicates

l4=[]
for i in range(len(l3)):
    for j in range(i+1,len(l3)):
        if(l3[i][2]==l3[j][2]):
            l4.append(l3[j])
for i in l4:
    if(i in l3):
        l3.remove(i)
print(l3)
