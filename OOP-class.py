# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 22:30:49 2021

@author: sodiyqun
"""

class User:
    def __init__(self, taxallus, ism, familiya, epochta, traqam):
        self.nickname = taxallus
        self.name = ism
        self.surname = familiya
        self.email = epochta
        self.phone = traqam
        
    def get_info(self):
        return f"Foydalanuvchi: {self.nickname}\nIsmi: {self.name} {self.surname}\
            \nElektron pochtasi: {self.email}\nTelefon raqami: {self.phone}"
            
    def get_name(self):
        return f"Ismi: {self.name}"
            
    def get_surname(self):
        return f"Familiyasi: {self.surname}"

    def get_contact(self):
        return f"Telefon raqami: {self.phone}nElektron pochtasi: {self.email}"
    
    
user1 = User("coder", "Ali", "Husanov", "ali@coder.co", 911655488)
print(user1.get_info())