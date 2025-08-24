#Prompting user for a file name and reading its contents
file = input("Enter name of the file you wish to open: ")
try:
    with open(file, "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("File name you entered does not exist.")

modifed_names = contents.upper()

with open("names_upper.txt", "w") as new_file:
    new_file.write(modifed_names)
    print("Modified names have been written to new file, names_upper.txt")
#open the new file and read its contents
input("Press Enter to read the new file, names_upper.txt: ")
with open("names_upper.txt", "r") as new_file:
    new_contents = new_file.read()
    print(new_contents)