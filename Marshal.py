import marshal
src='''
a=10
b=20
print("Multiplication=",a*b)
'''
code=compile(src,"src","exec")
fp=open("Marshal.txt","wb")
marshal.dump(code,fp)
fp.close()