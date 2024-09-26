#filename = "exemplo_files.py"

# with open(filename) as f:
#     content = f.readlines()

# print(content)    

# infile = open(filename, 'r')
# data = infile.read()
# infile.close()

# print(data)
# print("\n")

# f = open("test.txt", "w")

# f.write("Hello World, \n")
# f.write("This data will be written to the file.\n")

# f.close()

f = open("test.txt", "a")

f.write("Don't delete existing data.\n")
f.write("Add this to the existing file.")

f.close()