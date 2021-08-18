import shutil
import re

content = ''
with open('potential-contacts.txt', 'w+') as file:
    file.write(content)
shutil.copy('potential-contacts.txt', 'potential-contacts.txt.bak')
