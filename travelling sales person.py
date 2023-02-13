import itertools
import math

def distance(city1, city2):
    # Euclidean distance between two cities
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def total_distance(cities):
    # Total distance of the current route
    return sum(distance(cities[i], cities[i-1]) for i in range(len(cities)))

def solve_tsp(cities):
    # Find the shortest route visiting all cities and returning to the starting city
    best_route = None
    best_distance = float("inf")
    for route in itertools.permutations(cities):
        route_distance = total_distance(route)
        if route_distance < best_distance:
            best_route = route
            best_distance = route_distance
    return best_route, best_distance

if __name__ == "__main__":
    cities = [(0, 0), (1, 1), (1, 0), (0, 1)]
    route, distance = solve_tsp(cities)
    print("Route:", route)
    print("Distance:", distance)
