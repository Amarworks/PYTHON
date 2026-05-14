name= "Jamie"
Bran= print("Hello," + name)
Jamie= ('''He said,
        I want to eat an apple''')  # Multiline string using triple quotes
print (Jamie)

print(name[0])
# print(name[5]) #Throws an error because index 5 does not exist

print(name[0:5]) #OR print(name[:5])
print(len(Jamie))

print(name[-3:-1]) #5-3=2 to 5-1=4 output-mi

print("Lets use Loop\n") 
for character in Jamie:
    print(character)

a="john"
print(a.upper())  # Converts to uppercase -> JOHN
print(a.lower())  # Converts to lowercase -> john
print(a.replace("john","Amar")) #a.split(" ") is used for spliting
print(a.capitalize())

b="WelcomeToTheConsole0"
print(b.isalnum()) #Alphanumeric{A-Z,a-z,0-9}
print(b.isalpha()) # {A-Z & a-z}
print(b.swapcase())
print(b.title()) # First letter of every word becomes capital

print(b.find("To")) # Finds index position of substring
print(b.startswith("Welcome"))   
print(b.endswith("0"))