f1=open("firstfile.txt","r")
for x in f1:
    print(x)
print("........................................................")

f1.seek(0,0)
ff=f1.readlines()
with open("oddlines.txt","w") as file2:
    for x in range(0,len(ff)):
        if(x%2==0):
           file2.write(ff[x])
           print(ff[x])
        