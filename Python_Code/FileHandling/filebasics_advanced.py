

print("------------R+ mode ------------")

# read the file in "r+" mode
# read + write 
with open(file="demo_r.txt",mode="r+") as fd:
    print(fd.tell()) # file pointer
    print(fd.read())
    print(fd.tell()) # file pointer 114 , after the operation read


print("------------W+ mode ------------")
# read file in "w+" mode
# write + read
with open(file="demo_r.txt",mode="r+") as fd:
    print(fd.tell()) # file pointer
    print(fd.read())
    print(fd.tell()) # file pointer 114 , after the operation read

"""
    tell  - will tell the position
    seek - will change the position
"""