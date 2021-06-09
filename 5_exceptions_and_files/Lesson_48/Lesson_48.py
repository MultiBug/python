####################################
# 48.1 Чтение данных из файлов
file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()
####################################
####################################
# 48.2 Чтение данных из файлов
file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()
####################################
####################################
# 48.3 Чтение данных из файлов
file = open("filename.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()
#>>>
#Re-reading
#Finished
#>>>
####################################
####################################
# 48.4 Чтение данных из файлов
file = open("filename.txt", "r")
print(file.readlines())
file.close()
#>>>
#['Line 1 text \n', 'Line 2 text \n', 'Line 3 text']
#>>>
file = open("filename.txt", "r")
for line in file:
    print(line)
file.close()
#>>>
#Line 1 text
#Line 2 text
#Line 3 text
#>>>
####################################
