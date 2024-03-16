# 1
landline = re.compile('\d{7}')

print(landline.match('0481234'))


# 2

mob = re.compile('\+?\d{12}')

print(mob.match('+380991231234'))

print(mob.match('380991231234'))


# 3
email = re.compile('\w{3,20}@\w{2,10}\.\w{2,10}')

print(email.match('asdf2@something.com'))


# 4

pib = re.compile('[a-zA-Z]{2,20} [a-zA-Z]{2,20} [a-zA-Z]{2,20}')

print(pib.match('Bruhman Bruh Man'))