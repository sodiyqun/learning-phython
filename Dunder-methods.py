# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 04:18:49 2021

@author: sodiyqun
"""

class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    def __repr__(self):
        return f"{self.ism} {self.familiya}"
    
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

    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
    
    def __repr__(self):
        return f"{self.ism} {self.familiya}"
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    
    def set_bosqich(self, qiymat):
        if qiymat >=0:
            self.bosqich += qiymat
        else:
            print("Xato")

    def __lt__(self, y):
        return self.bosqich < y.bosqich
    
    def __le__(self, y):
        return self.bosqich <= y.bosqich
    
    def __eq__(self, y):
        return self.bosqich == y.bosqich
    
    
class Fan:
    """Fan nomli klass"""
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
        
    def __getitem__(self, x):
        return self.talabalar[x]
    
    def __setitem__(self, index, value):
        # self.talabalar[index] = value
        if isinstance(value, Talaba):
            self.talabalar[index] = value
        else:
            return "xato"
        
    def __len__(self):
        return len(self.talabalar)
    
    def __add__(self, x):
        if isinstance(x, Talaba):
            self.add_student(x)
            
    def __sub__(self, x):
        # self.talabalar.remove(x)
        if x in self.talabalar:
            self.talabalar.remove(x)

    def add_student(self, talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_name(self):
        """Fan nomi"""
        return self.nomi

    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return [talaba.get_fullname() for talaba in self.talabalar]

    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni



matem = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon", "Valiyev", "ff004400", 2000, 430987)
talaba2 = Talaba("Hasan", "Alimov", "ff004400", 2000, 430987)
talaba2.set_bosqich(2)
talaba3 = Talaba("Akrom", "Boriyev", "ff004400", 2000, 430987)
talaba3.set_bosqich(3)
talaba4 = Talaba("Malik", "Husanov", "ff004400", 2000, 430987)
shaxs1 = Shaxs("Anvar", "Tursunov", "ff004400", 2000)
shaxs2 = Shaxs("Farruh", "Yoqubov", "ff004400", 2000)
shaxs3 = Shaxs("Umar", "Kamolov", "ff004400", 2000)

talaba5 = Talaba("Boho", "Majidov", "ff004400", 2000, 430987)

matem.add_student(talaba1)
matem.add_student(talaba2)
matem.add_student(talaba3)
matem.add_student(talaba4)
