import re


f = open("assets1/potential-contacts.txt", "r").read()
numbers = re.findall(r'(\d\d\d-\d\d\d-\d\d\d\d)', f)
number_content = ''
for num in sorted(numbers):
    number_content += str(num)
    number_content += f'\n'

with open('phone_numbers.txt', 'w+') as file:
    file.write(number_content)

# //////////////////////////////////////////////////

email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', f)
email_content = ''
for ele in sorted(email):
    email_content += str(ele)
    email_content += f'\n'

with open('emails.txt', 'w+') as file:
    file.write(email_content)


# ///////////////////////////////


content = ''
for i in range(len(numbers)):
    content += str(email[i])
    content += f'\n'
    content += str(numbers[i])
    content += f'\n'

with open('potential-contacts.txt', 'w+') as file:
    file.write(content)
