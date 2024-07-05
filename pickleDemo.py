import pickle
fp=open("pickle file.txt","wb")
Student=["hari","ram","ravi"]
pickle.dump(Student,fp)
fp.close()