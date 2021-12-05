###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    trips = []
    avail_cows = cows.copy()
    
    while len(avail_cows):
        curr_trip = []
        lim = limit
        
        avail_trip_cows = avail_cows.copy()
        
        while lim and len(avail_trip_cows):
            heaviest_cow = max(avail_trip_cows, key = avail_trip_cows.get)
            if lim - avail_trip_cows[heaviest_cow] < 0:
                del avail_trip_cows[heaviest_cow]
                continue
            
            curr_trip.append(heaviest_cow)
            lim -= avail_trip_cows[heaviest_cow]
            del avail_cows[heaviest_cow]
            del avail_trip_cows[heaviest_cow]
        
        trips.append(curr_trip)
    
    return trips
        


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    for part in get_partitions(cows.keys()):

        for trip in part:

            trip_dict = {}
            for cow in trip:
                trip_dict[cow] = cows[cow]
                
            if sum(trip_dict.values()) > limit:
                break
        
        else:
            return part     

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    
    for func in [greedy_cow_transport, brute_force_cow_transport]:
        print(func.__name__)
        print(func(cows))
        start = time.time()
        gct = func(cows)
        end = time.time()
        print(f'Number of trips: {len(gct)}')
        print(f'Time: {end - start}s\n')

    



cows = load_cows("ps1_cow_data.txt")

compare_cow_transport_algorithms()

