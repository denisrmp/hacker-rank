patterns = ["++--***..."[:x] for x in xrange(1, 11)]
blueprint = list(raw_input())
pads = 0
building = ""
numbers = '123456789'
letters = 'abcdefghij'

def print_output(building):
    length = len(building[0])
    for i in reversed(xrange(length)):
        temp = ''
        for column in building:
            temp += column[i]
        print(temp)

for element in blueprint: 
    if element in numbers:
        pads = int(element)
    else:
        i = letters.find(element)
        building += ' ' * pads + patterns[i] + ' ' * (22 - pads - i)
        pads = 0

print("\n".join([building[x::23] for x in xrange(22,-1,-1)]))
