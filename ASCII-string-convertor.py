#ASCII-string-convertor
print("Enter a String: ", end="")
text = input()
textlength = len(text)
for char in text:
    ascii = ord(char)
    print(char, "\t", ascii)