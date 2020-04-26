# # # Part 1
# # Extending List

# class ContactList(list):
#     def search(self, name):
#         '''Return all contacts that contain the search value in their name
#         Search is case insensitive
#         '''
#         matching_contacts = []
#         for contact in self:
#             if name.lower() in contact.name.lower():
#                 matching_contacts.append(contact)
#         return matching_contacts
#
# class Contact:
#     all_contacts = ContactList()
#
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
#         self.all_contacts.append(self)
#
# c1 = Contact('John Mayor','jmayor@abc.com')
# c2 = Contact('Admen hilary','admen@abc.com')
# c3 = Contact('John leonidus','jleonidus@abc.com')
#
# # searching
# [print(c.name) for c in Contact.all_contacts.search('John')]
#

## ---------------------------------------------------------------------------------------------##
# # # Part 2 
# # Extending Dictionary

class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest

# Alternate way to declare a dictionary

d1 = LongNameDict()
d1['hello'] = 1
d1['world'] = 2
d1['!'] = 5

d2 = LongNameDict([ ('this is long',1) ,
                    ('this is longer',2) ,
                    ('this is longest',3)])

print(d1.longest_key())
print(d2.longest_key())
