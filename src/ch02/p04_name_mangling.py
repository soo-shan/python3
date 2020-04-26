class SecretString:
    """ A not at all secure way to store a string
    """

    def __init__(self, plain_text, pass_phrase):
        self.__plain_text = plain_text
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        """ Only show the text if pass phrase is correct
        """
        if self.__pass_phrase == pass_phrase:
            print(self.__plain_text)
            return 0
        else:
            print('Incorrect Pass Phrase !!!!')
            return 1


secret_string = SecretString('hakuna matata', 'cool')
attempts = 0
agent_name = input('Enter Code Name: ')
print(f'Welcome Agent {agent_name}')
while True:
    print(f'{agent_name}, you have {3 - attempts} attempts left')
    password = input('Enter the pass phrase to decrypt the message: ')
    print(f'Decrypt with pass phrase: {password}')
    if not secret_string.decrypt(password):
        break

    attempts += 1
    if attempts >= 3:
        print('Allowed Attempts exceeded')
        print('Exiting the program \n')
        break
print('Original Message without Decrypt')
# Name mangling
# property prefixed by _<classname>
print(secret_string._SecretString__plain_text)
