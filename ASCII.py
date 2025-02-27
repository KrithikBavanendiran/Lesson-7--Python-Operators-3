
def character_to_ascii(character):
    return ord(character)

character = input("Enter a character: ")
ascii_value = character_to_ascii(character)
print("The ASCII value of ",character, "is",ascii_value)
