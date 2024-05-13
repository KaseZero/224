import os
f = open("t234.txt",'w')
f.write(("老马滑铲"))
f.write(("老马火焰"))
f.flush()
f = open("t234.txt",'w')
f.close()
#...
os.remove("4234.txt")
f.close()

f = open("a.txt",'r')
print(f.tell())
print(f.read(3))
print(f.tell)


