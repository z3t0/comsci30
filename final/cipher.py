# Lets me make up objects
class Foo(object):
    pass

def get_input():
    path = None
    shift = None
    file = None

    while (path == None or file == None):
        try:
            path = raw_input("Where is your text file located: ")
            file = open(path)

        except IOError:
            file = None
            path = None
            print "Please enter a valid path"

    while (shift == None or type(shift) != int):

        try:
            shift = int(raw_input("How many characters to shift by?: "))

        except ValueError:
            print "Please enter an integer"

    data = Foo()
    data.path = path
    data.shift = shift
    data.lines = file.readlines()[0]

    file.close()

    return data

input = get_input()
encrypted = ""

for char in input.lines:
    n = ord(char)

    if n >= 65 and n <= 90: # Capital Letter
        if (n + input.shift) > 90:
            # Need to wraparound
            n = 65 + (n + input.shift - 90) - 1

        elif (n + input.shift) < 65:
            # Need to wraparound
            n = 90 + (n + input.shift - 65) + 1

        else:
            n += input.shift

    elif n >= 97 and n <= 122: # Lower case letter
        if (n + input.shift) > 122:
            # Need to wraparound
            n = 97 + (n + input.shift - 122) - 1

        elif(n + input.shift) < 97:
            # Need to wraparound
            n = 122 + (n + input.shift - 97) + 1

        else:
            n += input.shift

    encrypted += chr(n)

print ">>>"
print encrypted
