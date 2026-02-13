class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        within_x_bounds = (self.pos_x <= x_2) & (self.pos_x >= x_1)
        within_y_bounds = (self.pos_y <= y_2) & (self.pos_y >= y_1)

        return within_x_bounds & within_y_bounds


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        # define the bounds of the affected area
        x1, x2 = x - self.__fire_range, x + self.__fire_range
        y1, y2 = y - self.__fire_range, y + self.__fire_range

        units_affected = [unit for unit in units if unit.in_area(x1, y1, x2, y2)]

        return units_affected
