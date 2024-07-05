import shelve
sh=shelve.open("sheves")
sh['one']=1
sh['two']=2
sh['three']=3
sh.close()