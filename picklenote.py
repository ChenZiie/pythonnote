import pickle

with open(nameoffile,'wb+') as f:
    pickle.dump(object,f)

with open(nameoffile,'rb') as f:
    something = pickle.load(f)