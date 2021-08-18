import shutil
import re
from typing import Counter

# numbers = re.findall('[0-9]+', str)
# with open('potential-contacts.txt', 'w+') as file:
#     # file.write(numbers)
#     x = file.read()s
# print(x)
# shutil.copy('potential-contacts.txt', 'potential-contacts.txt.bak')


f = open("assets1/potential-contacts.txt", "r").read()
numbers = re.findall(r'(\d\d\d-\d\d\d-\d\d\d\d)', f)
print(numbers)
match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', f)
print(match)
