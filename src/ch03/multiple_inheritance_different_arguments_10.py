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

    def __init__(self, name="", email="", **kwargs):
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class MailSender:
    """
    This class doesn't do anything by itself but allows us to define a new class
    """

    def send_mail(self, message):
        print('Sending mail to ' + self.email)
        # add email logic here


class EmailableContact(Contact, MailSender):
    """
    This class inherits from both Contact and MailSender class
    """
    pass


class AddressHolder:
    def _init__(self, street="", city="", state="", code="", **kwargs):
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    def __init__(self, phone="", **kwargs):
        super().__init__(**kwargs)
        self.phone = phone


f1 = Friend('9898989')