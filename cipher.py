caesar_cipher = {
    "a" : "f",
    "b" : "g",
    "c" : "h",
    "d" : "i",
    "e" : "j",
    "f" : "k",
    "g" : "l", 
    "h" : "m", 
    "i" : "n", 
    "j" : "o", 
    "k" : "p", 
    "l" : "q", 
    "m" : "r", 
    "n" : "s", 
    "o" : "t", 
    "p" : "u", 
    "q" : "v", 
    "r" : "w", 
    "s" : "x", 
    "t" : "y", 
    "u" : "z", 
    "v":"a", 
    "w":"b", 
    "x":"c", 
    "y":"d", 
    "z":"e",
}
message = input("Please enter a sentence:")
message = message.lower()
characters = message.split()
output = ""
for character in message:
    output += caesar_cipher.get(character, character)
print(output)