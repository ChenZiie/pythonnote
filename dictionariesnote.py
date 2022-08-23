d = {"A":1,"B":2,"C":3}
empty = {}      ## empty dictionary
print(d["A"])       ## d[1] won't work
print(d.values())
print(d.keys())
d["C"]=4        ### change the value of the keys
print(d.items())    #return a tulpe

x = (("A",1),("B",2))
print(dict(x))

d["D"]=5    #add D into d

del d["A"]   #remove A

d.pop("B")  #remove and return the value of "B"

print(d.get("C"))   # get the value of "C" same as d["C"]

d2={"F":5,"G":7}
d.update(d2)          # did not change d2, and add d2 to d

"E" in d            # will return true or false

("C",4) in d.items()        # will return true or false

for i, v in d.items():
    print(i,v)            # i is key and v is value

c={'a':[1]}
c['a'].append(2)            # one key 2 value, the value have to has [ ] around
for i, v in c.items():
    print(i,v)

f = {1:1,2:3}
for i, v in f.items():
    print(i,v)