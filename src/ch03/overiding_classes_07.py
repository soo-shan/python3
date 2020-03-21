class ContactList(list):
    def search(self, name):
        """Return all contacts that contain the search value in their name
        """
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class Friend(Contact):
    def __init__(self, name, email, phone):
        self.phone = phone
        super().__init__(name, email)


c1 = Contact('Sam','sam@gmail.com')
f1 = Friend('fri','fri@fri.con',102020)
print([i.name for i in Contact.all_contacts])