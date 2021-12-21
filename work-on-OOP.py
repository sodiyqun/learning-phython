# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 01:16:51 2021

@author: sodiyqun
"""

class Avto():
    def __init__(self, kompaniya, model, rang, korobka, narh):
        self.make = kompaniya
        self.model = model
        self.color = rang
        self.type = korobka
        self.price = narh
        self.km = 0
        
    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_rang(self):
        return self.color

    def get_type(self):
        return self.type
    
    def get_info(self):
        return f"{self.color.capitalize()} {self.model.capitalize()}, kompaniya: {self.make}, korobka: {self.type.capitalize()}, probeg: {self.km} km, narhi: {self.price}"

    def update_km(self, n):
        self.km += n


class Avtosalon():
    def __init__(self, nomi, manzil):
        self.loc = manzil
        self.name = nomi
        self.cars = []
        
    def add_car(self, car):
        self.cars.append(car)
        
    def get_cars(self):
        return [car.get_info() for car in self.cars]


salon = Avtosalon("GM", "tosh")
car1 = Avto("GM", "spark", "Oq", "avtomat", 6000)
car2 = Avto("KIA", "lam", "qizil", "avtomat", 13000)
car3 = Avto("Tesla", "Model S", "qora", "ruchnoy", 40000)
salon.add_car(car1)
salon.add_car(car2)
salon.add_car(car3)
print(salon.get_cars())