class Siege:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, food_price):
        cost = (distance / self.efficiency) * food_price

        return cost

    def get_cargo_volume(self):
        pass


class BatteringRam(Siege):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        super().__init__(max_speed, efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area
        self.depth = 2  # metres

    def get_trip_cost(self, distance, food_price):
        trip_cost = super().get_trip_cost(distance, food_price)

        cost_of_food = self.load_weight * 0.01

        return trip_cost + cost_of_food

    def get_cargo_volume(self):
        return self.bed_area * self.depth


class Catapult(Siege):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().__init__(max_speed, efficiency)
        self.__cargo_volume = cargo_volume

    def get_cargo_volume(self):
        return self.__cargo_volume
