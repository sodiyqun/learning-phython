# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 14:53:52 2021

@author: sodiyqun
"""

from uuid import uuid4

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __odamlar_soni = 0
    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        Shaxs.__odamlar_soni += 1
        
    @classmethod
    def get_num_odam(cls):
        return cls.__odamlar_soni

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil


class Talaba(Shaxs):
    """Talaba klassi"""
    __talabalar_soni = 0
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.bosqich = 1
        self.__idraqam = uuid4()
        Talaba.__talabalar_soni += 1
        
    @classmethod
    def get_num_talaba(cls):
        return Talaba.__talabalar_soni

    def get_id(self):
        """Talabaning ID raqami"""
        return self.__idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

talaba1 = Talaba("Alijon", "Valiyev", "ff004400", 2000, 430987)
talaba2 = Talaba("Hasan", "Alimov", "ff004400", 2000, 430987)
talaba3 = Talaba("Akrom", "Boriyev", "ff004400", 2000, 430987)
talaba4 = Talaba("Malik", "Husanov", "ff004400", 2000, 430987)
shaxs1 = Shaxs("Anvar", "Tursunov", "ff004400", 2000)
shaxs2 = Shaxs("Farruh", "Yoqubov", "ff004400", 2000)
shaxs3 = Shaxs("Umar", "Kamolov", "ff004400", 2000)
