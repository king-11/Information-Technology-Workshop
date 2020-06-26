import os

print(os.getcwd())

os.mkdir("newdir")
print(os.listdir())


os.chdir("./newdir")
os.popen("touch myfile.txt")
print(os.popen("ls").readlines())
os.chdir("..")

os.popen("rm -r ./newdir")
