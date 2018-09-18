# Given an unordered list of flights taken by someone, each represented as 
# (origin, destination) pairs, and a starting airport, compute the person's 
# itinerary. If no such itinerary exists, return null. If there are multiple 
# possible itineraries, return the lexicographically smallest one. All flights
# must be used in the itinerary.

def get_itinerary(start, flights, itinerary):
    itinerary.append(start)
    if not flights:
        return itinerary

    for i, (origin, destination) in enumerate(flights):
        if origin == start:
            without_cur = flights[:i] + flights[i+1:]
            return get_itinerary(destination, without_cur, itinerary)

    return None

if __name__ == '__main__':
    for start, flights in [
        ('YUL', [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]),
        ('COM', [('SFO', 'COM'), ('COM', 'YYZ')]),
        ('A', [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]),
        ('A', [('A', 'C'), ('A', 'B'), ('B', 'C'), ('C', 'A')]),
    ]:
        flights.sort()
        print('Itinerary of {} is {}'.format(flights, get_itinerary(start, flights, [])))
