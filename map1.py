import folium

map=folium.Map(location=[38.58,-99.09],zoom_start=2, tiles ='openstreetmap',max_zoom=18,zoom_control='True')

#folium.TileLayer('openstreetmap'.add_to(map))
#folium.TileLayer('mapquestopen'.add_to(map))
#folium.TileLayer('MapQuest Open Aerial'.add_to(map))
#folium.TileLayer('Mapbox Bright'.add_to(map))
#folium.TileLayer('stamenterrain'.add_to(map))
#folium.TileLayer('stamentoner'.add_to(map))
#folium.TileLayer('cartodbpositron'.add_to(map))
#fg=folium.FeatureGroup(name="My Map")

def lat(l):
    if -90 <= l <=90:
        print("The value has been entered")
        return l
    else:
        print(input("Incorrect values. Please enter values betwee -90 to 90: "))

def lon(lo):
    if -180 <= lo <=180:
        print("The value has been entered")
        return lo
    else:
        print(input("Incorrect values. Please enter values betwee -180 to 180: "))

lat_input = input("Enter the Latitude value between -90 to 90 of your desired location: ")
output1 = lat(float(lat_input))
lon_input = input("Enter the longitude value between -180 to 180 of your desired location: ")
output2 = lon(float(lon_input))
coordinates = output1,output2
name = input("Please enter your name: ")
yn = input("Hello! %(name)s The latitude you entered is %(first)s and longitude is %(second)s. Enter Y if yes and N if no: " %{"name":name,"first":output1,"second":output2})

fgp = folium.FeatureGroup(name="Pointers") #This is like different views you can have on a map, like layers.
if yn == 'Y':
     fgp.add_child(folium.CircleMarker(location=[output1,output2],radius = 6, popup=str(coordinates)+"m",
     fill_color='green',color='grey',fill_opacity=0.7))
else:
     print("Exit and try again")

fgpl = folium.FeatureGroup(name="Population")
fgpl.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005']<10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
#.GeoJson is a method to create layers in the map. There is point layer, line layer
#and we can also make a polygon layer. GeoJson is a special case of Json.
#lambda functions are functions that are written in single line of code

map.add_child(fgp)
map.add_child(fgpl)
map.add_child(folium.LayerControl())
map.save("Map1.html")
