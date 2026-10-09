temp=int(input("Enter today's temperature:"))
if temp<20:
    outfit="jacket"
    print( "It is cold today")
    print( "Wear a ",outfit)
else:
    outfit="t-shirt"
    print( "It is warm today")
    print( "Wear a ",outfit)

is_raining=input("Is it raining today? yes/no")

if is_raining=="yes":
     print("bring your umbrella")
else:
    print("you can skip bringing your umbrella")

wind_speed=int(input("Enter today's wind speed:"))
if wind_speed>30:
    print( "It is windy today")
   
else:
    
    print( "It is a calm day today")

has_puddles=input("Are there puddles on the ground today? (yes/no)")

if has_puddles=="yes":
  shoes="boots"
  print("The ground is wet")
  print("Wear",shoes)
else:
    print("The ground is dry")
    print("Wear",shoes)

print("")
print("Weather check complete")

print("======== WEATHER OUTFIT PICKER =========")
print("Temperature:",temp)
print("Outfit chosen:",outfit)
print("Raining:",is_raining)
print("Wind:",wind_speed)
print("Shoes chosen:",shoes)
print("========================================")