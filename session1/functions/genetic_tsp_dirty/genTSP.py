import math
from random import randint, choice, random, sample
from statistics import variance


class TspData:

    def __init__(self, plane_width, num_of_cities):
        self.cities_coords = [(randint(-plane_width//2, plane_width//2),
                        randint(-plane_width//2, plane_width//2)) for _ in range(num_of_cities)]
        self.cities_indices = list(range(num_of_cities))
        self.num_of_cities = num_of_cities

class GeneticTSPSolver:

    def __init__(self, tsp_data, random_mutation_factor = 2, population_size = 50,
                 mutation_chance = 0.01, max_mutation_chance = 0.15, max_generation_count=500000):
        self.tsp_data = tsp_data
        self.staring_population_size = population_size
        self.population = []
        self.random_mutation_factor = random_mutation_factor
        self.mutation_chance = mutation_chance
        self.max_mutation_chance = max_mutation_chance
        self.generation_counter = 0
        self.best_travel_itinerary = None
        self.best_travel_dist = math.inf
        self.max_generation_count = max_generation_count
        self.average_fitnesses = []

    def create_random_network_and_create_staring_population(self):
        for k in range(self.staring_population_size):
            # creates k randomly ordered samples from the cities and appends them to the population
            self.population.append(sample(self.tsp_data.cities_indices, len(self.tsp_data.cities_indices)))

    def string_them_up(self, travel_itinerary):
        # takes a travel itinerary (= a list of cities to be visited in order)
        # and creates a list of edges representing the path between the cities
        city_coords = []
        for i in range(len(travel_itinerary) - 1):
            src = travel_itinerary[i]
            dest = travel_itinerary[i + 1]
            city_coords.append((self.tsp_data.cities_coords[src], self.tsp_data.cities_coords[dest]))
        city_coords.append((self.tsp_data.cities_coords[travel_itinerary[-1]], self.tsp_data.cities_coords[travel_itinerary[0]]))
        return city_coords

    def calculate_distance_for_member(self, member):
        return sum([math.dist(*x) for x in member])

    def calculate_epoch(self):

        # calculate the fitness of all population members
        population_with_fitness = [(x, self.calculate_distance_for_member(self.string_them_up(x))) for x in self.population]
        population_with_fitness = sorted(population_with_fitness,key=lambda x: x[1])

        if population_with_fitness[0][1] < self.best_travel_dist:
            self.best_travel_dist = population_with_fitness[0][1]
            self.best_travel_itinerary = population_with_fitness[0][0]

        # extract the fittest 50% and append the worst and some random members
        fittest_50_percent = population_with_fitness[:len(population_with_fitness)//2]

        if self.generation_counter > 10000 and len(set([x[1] for x in fittest_50_percent])) == 1:
            # oh no! We have converged!
            return "Error! Converged!", 0

        fittest_50_percent.append(choice(population_with_fitness[len(population_with_fitness)//2:]))
        fittest_50_percent.append(choice(population_with_fitness[len(population_with_fitness)//2:]))
        fittest_50_percent.append(choice(population_with_fitness[len(population_with_fitness)//2:]))
        fittest_50_percent.append(population_with_fitness[-1])


        self.generation_counter += 1
        avg_population_fitness = sum([x[1] for x in population_with_fitness])/len(population_with_fitness)
        self.average_fitnesses.append(avg_population_fitness)

        #increase mutation_chance if it looks like we've hit a local minimum
        if len(self.average_fitnesses)> 1000:
            if self.mutation_chance < self.max_mutation_chance:
                last_1000_gens = self.average_fitnesses[-1000:]
                last_100_gens = self.average_fitnesses[-100:]
                variance_last_1000 = variance(last_1000_gens)
                variance_last_100 = variance(last_100_gens)
                if abs(variance_last_1000-variance_last_100) / ((variance_last_1000 + variance_last_100) / 2) < 0.05:
                    self.mutation_chance += 0.001


        # lets mate!
        children = []
        while len(children) < self.staring_population_size:
            parent_1 = choice(fittest_50_percent)[0]
            parent_2 = choice(fittest_50_percent)[0]
            if parent_1 == parent_2:
                # we don't want that
                continue

            # lets do some order crossover to create the new kid:
            size = len(parent_1)
            child = [None] * size
            start, end = sorted(sample(range(size), 2))
            child[start:end + 1] = parent_1[start:end + 1]
            p2_index = 0
            for i in range(size):
                if child[i] is None:
                    while parent_2[p2_index] in child:
                        p2_index += 1
                    child[i] = parent_2[p2_index]

            # mutations!
            for _ in range(self.random_mutation_factor):
                if random() < self.mutation_chance:
                    idx = range(len(child))
                    i1, i2 = sample(idx, 2)
                    child[i1], child[i2] = child[i2], child[i1]
            children.append(child)

        return children, avg_population_fitness

    def run(self, pipe):
        self.create_random_network_and_create_staring_population()
        while self.generation_counter < self.max_generation_count:
            self.population, avg_dist = self.calculate_epoch()
            if self.population == "Error! Converged!":
                print("Converged! :( ?")
                return "END"
            if self.generation_counter % 100 == 0:
                pipe.put((self.tsp_data.cities_coords, self.string_them_up(self.best_travel_itinerary)))
                print("Generation:", self.generation_counter, avg_dist, self.random_mutation_factor)
