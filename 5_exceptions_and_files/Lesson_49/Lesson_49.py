####################################
# 49.1 Запись в файл
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()
file = open("newfile.txt", "r")
print(file.read())
file.close()
####################################
####################################
# 49.2 Запись в файл
file = open("newfile.txt", "w")
file.write("Some new text")
file.close()
file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()
####################################
####################################
# 49.3 Запись в файл
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()
####################################
