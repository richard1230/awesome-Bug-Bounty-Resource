# 这个py的作用:
# 原来文本的每一行之间都插入了peter
file1 = open('Authentication_lab_passwords.txt', 'r')

Lines = file1.readlines()

for line in Lines:
    print("peter")
    print("{}".format(line.strip()))
