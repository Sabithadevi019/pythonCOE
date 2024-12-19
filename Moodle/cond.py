def preLet(input_string, letter):
    index = input_string.find(letter)
    if index != -1:
        return input_string[:index].lower() + input_string[index:].upper()
    else:
        return input_string
print(preLet("CAtCHa", "a"))
print(preLet("Preteen", "e"))
print(preLet("You've got this", "m"))
print(preLet("Keep trying", "k"))
