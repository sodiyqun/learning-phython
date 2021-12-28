# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 18:11:31 2021

@author: sodiyqun
"""

import json

# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# data_json = json.dumps(data, indent=4)
# # print(data_json)


# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# talaba = json.loads(talaba_json)
# print(f"{talaba['ism']} {talaba['familiya']}")


# with open("JSON/data.json", "w") as f:
#     json.dump(data, f)
    
# with open("JSON/talaba.json", "w") as f:
#     json.dump(talaba, f)
    
    
# with open("JSON/students.json", "r") as f:
#     students = json.load(f)

# for s in students['student']:
#     print(f"{s['name']} {s['lastname']}, {s['year']}-kurs, {s['faculty']} talabasi")
    

with open("JSON/wikipython-api-result.json", "r") as f:
    py = json.load(f)

print(py['query']['pages']['13801']['title'])
print(py['query']['pages']['13801']['extract'])
