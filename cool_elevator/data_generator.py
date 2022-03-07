from random import randint


class DataGenerator:

    def __init__(self, first_floor=5, last_floor=20, min_passengers=0, max_passengers=10):
        self.first_floor = first_floor
        self.last_floor = last_floor
        self.min_passengers = min_passengers
        self.max_passengers = max_passengers

    def get_floors(self):
        return randint(self.first_floor, self.last_floor)

    def get_passengers(self):
        return randint(self.min_passengers, self.max_passengers)

    def generation_all_data(self):
        people = {}
        floors = DataGenerator.get_floors(self)
        for i in range(floors):
            choice_floor = []
            for n in range(DataGenerator.get_passengers(self)):
                floor = randint(1, floors)
                if floor != i+1:
                    choice_floor.append(floor)
            people[i+1] = choice_floor
        return people
