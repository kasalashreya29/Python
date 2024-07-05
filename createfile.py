fp1=open("csal.text","r")
fp2=open("csea12.text","w")
if fp1:
    print("file opened successfully")
for i in fp1:
    fp2.write(i)
print("file is copied successfully")
fp2.seek(0,0)
cont=fp2.read()
