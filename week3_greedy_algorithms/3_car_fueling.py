# python3
import sys


def compute_min_refills(destination, tank, n, stops):

    num_refills, curr_position, curr_refill = 0, 0, 0
    while curr_position + tank <= destination:
        if curr_refill >= n or stops[curr_refill] - curr_position >= tank:
            return -1
        while curr_refill < n - 1 and stops[curr_refill + 1] - curr_position <= tank:
            curr_refill += 1
        num_refills += 1
        curr_position = stops[curr_refill]
        curr_refill += 1

    return num_refills


def car_fueling(dist, miles, n, gas_stations):
    num_refill, curr_refill, limit = 0, 0, miles
    while limit < dist:
        # While the destination cannot be reached with current fuel
        if curr_refill >= n or gas_stations[curr_refill] > limit:
            # Cannot reach the destination nor the next gas station
            return -1

        # Find the furthest gas station we can reach
        while curr_refill < n - 1 and gas_stations[curr_refill + 1] <= limit:
            curr_refill += 1

        num_refill += 1  # Stop to tank
        limit = gas_stations[curr_refill] + miles  # Fill up the tank
        curr_refill += 1

    return num_refill

if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    # input = '950 400 4 200 375 550 750' #pass
    # input = '10 3 4 1 2 5 9'
    # input = '200 250 2 100 150' #pass
    # input = '500 200 4 100 200 300 400'
    # input = '700 200 4 100 200 300 400'
    # d, m, n, *stops = map(int, input.split())
    print(compute_min_refills(d, m, n, stops))
    # print(car_fueling(d, m, n, stops))
