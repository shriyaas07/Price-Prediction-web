import airportsdata

# Load IATA airports data
airports = airportsdata.load("IATA")

# Extract all unique cities
unique_cities = sorted({info['city'] for info in airports.values() if info.get('city')})

# Save to a text file
with open("city_list.txt", "w", encoding="utf-8") as f:
    for city in unique_cities:
        f.write(city + "\n")

print("City_list.txt created successfully with", len(unique_cities), "cities.")
