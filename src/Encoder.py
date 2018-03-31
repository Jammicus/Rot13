import sys
encodedText = ""

for input in sys.argv[1:]:
    for character in str(input):
        encodedValue = (ord(character.lower()))
        if (not chr(encodedValue).isalpha()):
            print(character,end='', flush=True)
        elif encodedValue <= 110:
            print((chr(encodedValue+13)),end='', flush=True)
        else:
             print((chr(encodedValue-13)),end='', flush=True)

print(encodedText)