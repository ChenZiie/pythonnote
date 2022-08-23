# dic = {'a':['187','001']}
import glob
import matplotlib as plt
# for i in dic['a']:
for filename in glob.glob('data/*.txt'):
    print(filename)