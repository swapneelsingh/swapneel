
flight_data = [
    {"Flight ID": "AI161E90", "From": "BLR", "To": "BOM", "Price": 5600},
    {"Flight ID": "BR161F91", "From": "BOM", "To": "BBI", "Price": 6750},
    {"Flight ID": "AI161F99", "From": "BBI", "To": "BLR", "Price": 8210},
    {"Flight ID": "VS171E20", "From": "JLR", "To": "BBI", "Price": 5500},
    {"Flight ID": "AS171G30", "From": "HYD", "To": "JLR", "Price": 4400},
    {"Flight ID": "AI131F49", "From": "HYD", "To": "BOM", "Price": 3499}
]

def search_flights_for_city(city):
    matching_flights = [flight for flight in flight_data if flight["From"] == city or flight["To"] == city]
    if matching_flights:
        print("Flights to/from", city)
        print_flight_table(matching_flights)
    else:
        print("No flights found for", city)

def search_flights_from_city(city):
    matching_flights = [flight for flight in flight_data if flight["From"] == city]
    if matching_flights:
        print("Flights from", city)
        print_flight_table(matching_flights)
    else:
        print("No flights found departing from", city)

def search_flights_between_cities(city1, city2):
    matching_flights = [flight for flight in flight_data if flight["From"] == city1 and flight["To"] == city2]
    if matching_flights:
        print("Flights from", city1, "to", city2)
        print_flight_table(matching_flights)
    else:
        print("No direct flights found from", city1, "to", city2)

# Function to print flight data in a tabular format
def print_flight_table(flights):
    print("{:<12} {:<5} {:<5} {:<6}".format("Flight ID", "From", "To", "Price"))
    for flight in flights:
        print("{:<12} {:<5} {:<5} {:<6}".format(flight["Flight ID"], flight["From"], flight["To"], flight["Price"]))

# Main program
while True:
    print("\nFlight Search Options:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        city = input("Enter the city name: ")
        search_flights_for_city(city)
    elif choice == "2":
        city = input("Enter the city name: ")
        search_flights_from_city(city)
    elif choice == "3":
        city1 = input("Enter the departure city: ")
        city2 = input("Enter the destination city: ")
        search_flights_between_cities(city1, city2)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")

print("Thank you for using the Flight Search program!")
