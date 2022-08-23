import matplotlib.pyplot as plt
import numpy as np
import numpy as rand

y=np.arange(0,10,2)
plt.plot(y)     #the index is the x coordinates and the vlue will be the y coordinates
plt.show()         #will show the plot same as print
#plt.savefig("example1.png")     #save
z=np.arange(0,15,3)
plt.plot(z)           #plot z at the same png

plt.title("A title")
plt.xlabel("X lable")
plt.ylabel("Y lable")       #lable the x,,y and title

line1,=plt.plot(data[0],'rs-')#给曲线设置标识。并把曲线赋给一个变量，方便下面添加图例时候应用
line2,=plt.plot(data[1],'-')#同上
line3,=plt.plot(data[2],'b.-')#同上
ll=plt.legend([line1,line2,line3],["Weekend", "Weekday","Festival"],loc='upper left')#添加图例


plt.clf()               #clean the figure

x=np.array([1,0,-1,0])
y=np.array([0,1,0,-1])
plt.plot(x,y)           #x as x , y as y

plt.plot(x,y,'g--')     #will use dashed green lines, "g--" is the style
plt.plot(x,y,'r+')         # red +

x = np.arange(0., 5., 0.2)
plt.plot(x, x, "r--")
plt.plot(x, x ** 2, "bs")      #blue square
plt.plot(x, x ** 3, "g^")       #green triangle

#other, "o" is point, "k" is black



x = np.arange(-np.pi, np.pi, step = 0.02)      #plot the sin and cos, step smaller will be better(more like the sin,cos)
si = np.sin(x)
co = np.cos(x)
plt.plot(x, si)
plt.plot(x, co)
plt.show()

plt.clf()
a=np.arange(50)
b=rand.randint(0,50,50)
plt.scatter(a,b)                #scatter plot

cat = np.array(["a", "b", "c", "d", "e"])
values = rand.randint(0, 10, 5)
plt.bar(cat, values)                        #bar chart


x = np.random.randint(0, 50, 50)
plt.hist(x)                         #bins automatically determined
plt.hist(x, bins=5)                  # with 5 equal sized bins
plt.hist(x, bins=[0, 10, 15, 25, 30, 40, 44, 50])    # with the bins specified in a list

s=rand.normal(size=1000)
plt.hist(s,bins=10)