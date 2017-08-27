# pythonex
#For practice my python skill

#https://github.com/giolao2018/pythonex.git
def rental_car_cost(days):
    co = days * 40
    if days >= 7:
        co = co - 50
    elif days >= 3:
        co = co - 20
    return co

def hotel_cost(days):
    return days * 140


def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475


def trip_cost(  city, days ,spending_monney):
 total=  rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_monney
 return total
print(trip_cost("Los Angeles",5, 600))
