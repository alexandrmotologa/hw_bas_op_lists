guests_1 = ["Bethaney Bain", "Kacey Johns", "Manpreet Saunders"]
guests_2 = ["Elwood Curtis", "Diya Griffin", "Kacey Johns"]
guests_3 = ["Tobey Weiss", "Kadie Barnes", "Diya Griffin"]

tangled_list_guests = guests_1 + guests_2 + guests_3
list_of_guests = []

for order_list_guests in tangled_list_guests:
    if order_list_guests not in list_of_guests:
        list_of_guests.append(order_list_guests)
list_of_guests.sort()
order_guests = list_of_guests
print(order_guests)

# cea mai simpla metoda, insa nu include for,
# nu indeplineste conditia in cazul dat :DD

# list_of_guests = list(set(tangled_list_guests))
# list_of_guests.sort()
# order_guests = list_of_guests
# print(order_guests)
