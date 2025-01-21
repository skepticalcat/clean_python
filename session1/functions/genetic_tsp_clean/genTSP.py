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

    def create_random_network(self):
        return sample(self.tsp_data.cities_indices, len(self.tsp_data.cities_indices))

    def create_staring_population(self):
        for k in range(self.staring_population_size):
            self.population.append(self.create_random_network())

    def create_edges_between_cities_of_travel_itinerary(self, travel_itinerary):
        edges = []
        for i in range(len(travel_itinerary) - 1):
            src = travel_itinerary[i]
            dest = travel_itinerary[i + 1]
            edges.append((self.tsp_data.cities_coords[src], self.tsp_data.cities_coords[dest]))
        edges.append((self.tsp_data.cities_coords[travel_itinerary[-1]], self.tsp_data.cities_coords[travel_itinerary[0]]))
        return edges

    @staticmethod
    def calculate_distance_for_travel_itinerary(itinerary):
        return sum([math.dist(*x) for x in itinerary])


    def augment_current_population_with_fitness(self):
        population_with_fitness = []
        for itinerary in self.population:
            edges = self.create_edges_between_cities_of_travel_itinerary(itinerary)
            fitness = self.calculate_distance_for_travel_itinerary(edges)
            population_with_fitness.append((itinerary, fitness))
        return population_with_fitness

    def update_best_travel_values(self, population_with_fitness_sorted):
        if population_with_fitness_sorted[0][1] < self.best_travel_dist:
            self.best_travel_dist = population_with_fitness_sorted[0][1]
            self.best_travel_itinerary = population_with_fitness_sorted[0][0]


    def get_other_non_fit_parents_for_genetic_variation(self, population_with_fitness):

        additional_less_fit_parents = []
        additional_less_fit_parents.append(choice(population_with_fitness[len(population_with_fitness)//2:]))
        additional_less_fit_parents.append(choice(population_with_fitness[len(population_with_fitness)//2:]))
        additional_less_fit_parents.append(choice(population_with_fitness[len(population_with_fitness)//2:]))
        additional_less_fit_parents.append(population_with_fitness[-1])

        return additional_less_fit_parents

    def select_new_parent_population(self, population_with_fitness):

        fittest_50_percent = population_with_fitness[:len(population_with_fitness)//2]

        if self.generation_counter > 10000 and len(set([x[1] for x in fittest_50_percent])) == 1:
            raise ValueError("The fittest 50% of the population consists of the same member, we have converged!")

        fittest_50_percent.extend(self.get_other_non_fit_parents_for_genetic_variation(population_with_fitness))

        return fittest_50_percent

    def increase_mutation_chance_if_needed(self):
        if self.mutation_chance < self.max_mutation_chance:
            if len(self.average_fitnesses) > 1000:
                last_1000_gens = self.average_fitnesses[-1000:]
                last_100_gens = self.average_fitnesses[-100:]
                variance_last_1000 = variance(last_1000_gens)
                variance_last_100 = variance(last_100_gens)
                if abs(variance_last_1000-variance_last_100) / ((variance_last_1000 + variance_last_100) / 2) < 0.05:
                    return self.mutation_chance + 0.001
        return self.mutation_chance

    @staticmethod
    def choose_two_different_parents(parents):
        while True:
            parent_1 = choice(parents)[0]
            parent_2 = choice(parents)[0]
            if parent_1 != parent_2:
                return parent_1, parent_2

    @staticmethod
    def create_child_using_order_crossover(parent_1, parent_2):
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
        return child

    def mutate_child(self, child):
        for _ in range(self.random_mutation_factor):
            if random() < self.mutation_chance:
                idx = range(len(child))
                i1, i2 = sample(idx, 2)
                child[i1], child[i2] = child[i2], child[i1]
        return child


    def create_children(self, parents):
        children = []
        while len(children) < self.staring_population_size:
            parent_1, parent_2 = self.choose_two_different_parents(parents)
            child = self.create_child_using_order_crossover(parent_1, parent_2)
            mutated_child = self.mutate_child(child)
            children.append(mutated_child)
        return children

    def calculate_generation(self):

        self.generation_counter += 1

        population_with_fitness = self.augment_current_population_with_fitness()
        population_with_fitness_sorted = sorted(population_with_fitness, key=lambda x: x[1])

        parents = self.select_new_parent_population(population_with_fitness_sorted)
        self.mutation_chance = self.increase_mutation_chance_if_needed()
        children = self.create_children(parents)

        avg_population_fitness = sum([x[1] for x in population_with_fitness])/len(population_with_fitness)
        self.average_fitnesses.append(avg_population_fitness)
        self.update_best_travel_values(population_with_fitness_sorted)

        return children, avg_population_fitness

    def run(self, pipe):
        self.create_staring_population()
        while self.generation_counter < self.max_generation_count:
            try:
                self.population, avg_dist = self.calculate_generation()
            except ValueError as e:
                if "converged" in str(e):
                    print(e)
                    break
            if self.generation_counter % 100 == 0:
                pipe.put((self.tsp_data.cities_coords, self.create_edges_between_cities_of_travel_itinerary(self.best_travel_itinerary)))
                print("Generation:", self.generation_counter, avg_dist)
