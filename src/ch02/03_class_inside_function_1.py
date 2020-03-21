class LowerCase:
    '''
    Format a string in lower case
    '''
    def format(self,string):
        return string.lower()

def format_string(string, formatter=None):
    '''Format the string using the formatter object, which is expected to have 
    a format method that accepts a string.
    '''

    class DefaultFormatter:
        ''' Default: Format a string in title case
        '''
        def format(self,string):
            return str(string).title()

    if not formatter:
        formatter = DefaultFormatter()
        return formatter.format(string)

    return formatter.format(string)


lowercase = LowerCase()
input1 = 'hello world, how are thou ?'
output1 = format_string(input1)
print('input string: ', input1)
print('output string: ', output1)
print('input string: ', output1)
print('output string: ', format_string(output1,formatter=lowercase))
# alternative way
# print('output string: ', format_string(output1,formatter=LowerCase()))
