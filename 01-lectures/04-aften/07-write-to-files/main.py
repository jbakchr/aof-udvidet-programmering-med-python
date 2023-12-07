txt = ""

for _ in range(0, 10):
    txt += "Thanks for letting me teach you Python\n"

# write to file
file = open("./thanks.txt", "w")
file.write(txt)
file.close()

# append to file
file = open("./thanks.txt", "a")
file.write("I hope I did okay ..")
file.close()
