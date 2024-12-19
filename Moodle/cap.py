print("Enter multiple lines of text. Press 'Enter' on an empty line to stop.")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
for line in lines:
    print(line.upper())
