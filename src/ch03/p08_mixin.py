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

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


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


# Check mixin
e1 = EmailableContact('John Smith', 'john@man.com')
e2 = EmailableContact('Jane Doe', 'jane@doe.com')
print([contact.name for contact in Contact.all_contacts])
e1.send_mail('Hello. this is a test mail')
