from datetime import datetime


class Vehicle:
    def __init__(self, vehicle_id, make, model, year, daily_rate, mileage, fuel_type):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.is_available = True
        self.mileage = mileage
        self.fuel_type = fuel_type

    def rent(self):
        if self.is_available:
            self.is_available = False
            return f"{self.vehicle_id} rented successfully!"
        return "Vehicle is not available."

    def return_vehicle(self):
        self.is_available = True
        return f"{self.vehicle_id} returned successfully."

    def calculate_rental_cost(self, days):
        return round(self.daily_rate * days, 2)

    def get_vehicle_info(self):
        return f"{self.make} {self.model} ({self.year}) - ${self.daily_rate}/day"


class Car(Vehicle):
    def __init__(self, vehicle_id, make, model, year, daily_rate, seating_capacity, transmission_type, has_gps):
        super().__init__(vehicle_id, make, model, year, daily_rate, mileage=0, fuel_type="Petrol")
        self.seating_capacity = seating_capacity
        self.transmission_type = transmission_type
        self.has_gps = has_gps

    def calculate_rental_cost(self, days):
        return round(self.daily_rate * days, 2)

    def get_fuel_efficiency(self):
        return {
            "city_mpg": 25 if self.transmission_type == "Automatic" else 30,
            "highway_mpg": 35 if self.transmission_type == "Automatic" else 40
        }


class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, make, model, year, daily_rate, engine_cc, bike_type):
        super().__init__(vehicle_id, make, model, year, daily_rate, mileage=0, fuel_type="Petrol")
        self.engine_cc = engine_cc
        self.bike_type = bike_type

    def calculate_rental_cost(self, days):
        rate = self.daily_rate
        if days < 7:
            rate *= 0.8  # 20% discount for short rentals
        return round(rate * days, 2)

    def get_fuel_efficiency(self):
        return 45 + (1000 - self.engine_cc) * 0.01  # simple formula for variation


class Truck(Vehicle):
    def __init__(self, vehicle_id, make, model, year, daily_rate, cargo_capacity, license_required, max_weight):
        super().__init__(vehicle_id, make, model, year, daily_rate, mileage=0, fuel_type="Diesel")
        self.cargo_capacity = cargo_capacity
        self.license_required = license_required
        self.max_weight = max_weight

    def calculate_rental_cost(self, days):
        return round(self.daily_rate * days * 1.5, 2)  # 50% surcharge

    def get_fuel_efficiency(self):
        return {
            "empty_mpg": 15,
            "loaded_mpg": 10
        }
