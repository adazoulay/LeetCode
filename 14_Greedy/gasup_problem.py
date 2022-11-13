import collections

MPG = 20
def find_ample_city(gallons, distances):
    remaining_gallons = 0
    CityAndRemainingGas = collections.namedtuple('CityAndRemainingGas',('city','remaining_gallons'))
    city_remaining_gallons_pair = CityAndRemainingGas(0,0)
    num_cities = len(gallons)
    for i in range(1, num_cities):
        remaining_gallons += gallons[i-1] - distances[i - 1] // MPG
        if remaining_gallons < city_remaining_gallons_pair.remaining_gallons:
            city_remaining_gallons_pair = CityAndRemainingGas(i, remaining_gallons)
    return city_remaining_gallons_pair.city


