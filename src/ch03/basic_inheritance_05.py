class Contact:
    all_contacts = [] # classs variable

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        print(f'If this were a real system we would send "{order}" order to "{self.name}" ')

c = Contact('Sushan','sushan@abc.com') 
s = Supplier('james','james@yahoo.com')
s.order('need space')