import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

city_coordinates = []

def distance(cities, cityorder):

    totaldistance = 0
    num_cities = len(cities)
    for i in range(num_cities):
        x1, y1 = cities[cityorder[i]]
        x2, y2 = cities[cityorder[(i + 1) % num_cities]]  # Wrap around to the first city.
        totaldistance += np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return totaldistance

def read(filename):
    global city_coordinates
    with open(filename, 'r') as file: 
        # Read the first line to get the number of cities
        num_cities = int(file.readline())

        # Read the subsequent lines containing x and y coordinates
        for _ in range(num_cities):
            line = file.readline().strip()  # Read a line and remove leading/trailing whitespace
            x, y = map(float, line.split())  # Split the line into x and y coordinates
            city_coordinates.append((x, y))
        return city_coordinates

        
def tsp(cities):
    
    def simulated_annealing(cities, initial_order, temperature, cooling_rate):
        current_order = initial_order
        current_cost = distance(cities,current_order)

        best_order = current_order
        best_cost = current_cost
        
        while temperature > 1e-10:
            new_order = np.copy(current_order)
            i, j = np.random.choice(len(cities), 2, replace=False)
            new_order[i], new_order[j] = new_order[j], new_order[i]

            new_cost = distance(cities,new_order)

            if new_cost < current_cost or np.random.rand() < np.exp((current_cost - new_cost) / temperature):
                current_order = new_order
                current_cost = new_cost

                if current_cost < best_cost:
                    best_order = current_order
                    best_cost = current_cost
            temperature *= 1 - cooling_rate
        return best_order

    x_cities = np.array([coord[0] for coord in cities])
    y_cities = np.array([coord[1] for coord in cities])

    initial_order = np.arange(len(cities))
    np.random.shuffle(initial_order)

    best_order = simulated_annealing(cities, initial_order, temperature=10000, cooling_rate=0.00013)
    best_x = x_cities[best_order]
    best_y = y_cities[best_order]
    initial_cost = distance(cities,initial_order)
    total_cost = distance(cities, best_order)
    best_x = np.append(best_x, best_x[0])
    best_y = np.append(best_y, best_y[0])

    plt.figure()
    plt.plot(best_x, best_y, marker='o', linestyle='-')
    plt.title('TSP Path')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.savefig('test.png')
    
    percentage_improvement = ((initial_cost - total_cost) / initial_cost) * 100

    print(total_cost)
    return best_order
