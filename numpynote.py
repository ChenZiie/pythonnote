import numpy as np
a=np.array([1,4,5,8],int)    # array will contain same type element , this is int, for list
a=np.array([1,4,5,8],float)  #  this is floating number
a.shape    # for this one is (4,)

b=np.array((1,4,5,8))    # array will contain same type element, for tuple
b=np.array(range(10),int)    # array will contain same type element , this is int, for list

x=[1,"a",3.0]
a=np.array(x)    # will become a list of string

d=np.arange(2,4,0.5,dtype=float)  # it can increase by 0.5

q=np.ones(10)      # list of ten 1's
w=np.zeros(10)     # list of ten 0's

a1=q               # change q will change a1 as well, they are one object
c1=a1.copy()        # chaange a1 won't change c1


x=[[1,2,3],[4,5,6]]
x[0][2]                 # it will be 3
a=np.array(x)                # will present as 2x3 matrix
a[0,2]                # it will be 3 as well
a.shape                 # it will be (2,3)

a=np.array([[1,2,3],[4,5,6]],float)
a[1,:]               #row 1 of a and all column   array([4,5,6])
a[-1:,-2:]           # will be array([[5,6]])

b=np.arange(0,10)
b=b.reshape((5,2))   #will become 5x2 array
b=b.flatten()     # will become a line

a = np.array([1,2,3])
np.concatenate((a,[1,2]))   #array concatenate array not need to be same size
np.vstack([a,[4,5,6]])      #array concatenate array need to be same size become matrix

np.zeros((5,2))    #creat a 5x2 all 0
np.ones((3,4))      # creat a 3x4 all 1
np.empty((3,4))      # will creat a 3x4 matirx but the element is very tiny number

b=np.zeros_like(a)   # creat b(all 0) as the shape as a
b.fill(33)       # b become all 33

np.identity(4,dtype=float)    # creat a identity 4x4 matrix
np.eye(4,k=-1,dtype=int)    # place off diagonal


np.concatenate((a,b))    # if a is 3x3 and b is 3x3 then this is 6x3
a+b      #just add the element inside the matrix (need to be same size or (b 1xn and a mxn))
a*b
a/b
a+1 # add all element in a by 1
a**3  # all element **3 in a
np.sin(a)  # sin all
a.sum()  #sum all element in a

b[:, np.newaxis]            # what is this?
np.dot(a,b)                 #dot product of 2 vector or 2 matrix a and b
np.cross(a,b)               # cross product of a,b
a.transpose()               #transpose of matrix a
np.linalg.det(a)            # determinet of a
np.linalg.inv(a)            #inverse of a
np.linalg.eig(a)            #return eigenvalue and csoponding eigenvector
vals,vecs=np.linalg.eig(a)  #vals=eigenvalue, vecs=eigenvector
vecs[:,0]                   #first column of vecs


# a is nx3 arrary
for [x,y,z] in a:           # you can do this
    x+y+z


a>b                         #it also can use <,>,=,!= ,it will return array([result,result,result]), compair the crosponding element ia a and b
a>3                         # comparies each element in a with 3

# if f is arrary([True,Flase....
any(f)                      #if f have 1 True then true
all(f)                      #if f have all True then true
any(a>3)
all(a>3)
np.logical_not(f)           # not f
np.logical_and(c,d)         # and
np.logical_or(c<4,c>5)      # or

e[e>=6]                     #pick up the element of e is >=6, return as array
q= e>5
e[q]                        #same as above
e[q]=0                      #change the element whcih is >5 to 0

a.nonzero()                 #return the nonzero index as a array


####  array can + the same demantion array   shape(a,) is 1 demantio


a[1]=0                      #change a[1] to 0