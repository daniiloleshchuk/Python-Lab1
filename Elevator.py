class Elevator:

    # static field
    staticVar = "This is static variable"

    # constructor
    def __init__(self, producer_name = "default producer name", carrying_capacity_in_kg = 800,
                 engine_power_consumption_in_watts = 999, height_in_sm = 260, width_in_sm = 180, length_in_sm = 180):

        self.producer_name = producer_name
        self.carrying_capacity_in_kg = carrying_capacity_in_kg
        self.engine_power_consumption_in_watts = engine_power_consumption_in_watts
        self.height_in_sm = height_in_sm
        self.width_in_sm = width_in_sm
        self.length_in_sm = length_in_sm

    # destructor
    def __del__(self):
        return

    def __str__(self):
        return "Producer name is: " + str(self.producer_name) + "\n" + \
            "Carrying capacity in kg is: " + str(self.carrying_capacity_in_kg) + "\n" + \
            "Engine power consumption in watts is: " + str(self.engine_power_consumption_in_watts) + "\n" + \
            "Height in sm is: " + str(self.height_in_sm) + "\n" + \
            "Width in sm is: " + str(self.width_in_sm) + "\n" + \
            "Length in sm is: " + str(self.length_in_sm) + "\n"

    @staticmethod
    def static_method():
        return Elevator.staticVar

    @staticmethod
    def main():
        print()
        elevator_1 = Elevator()
        elevator_2 = Elevator("prod name 2", 2, 3)
        elevator_3 = Elevator("prod name 3", 3, 4, 5, 6, 7)
        print(elevator_1.__str__())
        print(elevator_2.__str__())
        print(elevator_3.__str__())


if __name__ == '__main__':
    Elevator.main()
