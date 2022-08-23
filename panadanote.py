import pandas as pd
import numpy as np

countries = ['USA', 'Nigeria', 'France', 'Ghana']
data = [100, 200, 300, 400]
a = pd.Series(data,countries)
print(a)

dic = {'a':50, 'b':60, 'c':70, 'd':80, 'USA':50}
b = pd.Series(dic)              #key is index
print(b)

print(a['USA'])             #use the index call the value

print(a - b)        #if has same index in both series, then will do the operation, other index will become NaN. And int become float
print(a + b)
print(a * b)

df1 = {'Name': pd.Series(['Jon','Aaron','Todd'], index=['a','b','c']),
       'Age': pd.Series(['39','34','32','33'], index=['a','b','c','d']),
       'Nationality': pd.Series(["USA", 'China','US'],index=['a','b','c'])}
df1 = pd.DataFrame(df1)


print(df1.columns,df1.index)     #show the structure, how we define the dataframe


dic = {'Name': ['Jon','Aaron','Todd'],
       'Age':[39,34,32],
       'Nationality': ["USA", 'China','US']}
df2 = pd.DataFrame(dic,index=['a','b','c'])
#index as row, key of dictionary as colomn
#df1 can be NaN value, df2 must be all cell has value
print(df1, '\n')
print(df2, '\n')
print(df2['Name'], '\n')
print(df2[['Name','Age']], '\n')

df2['weight'] = pd.Series([0,1,2],['a','b','c'])  #add a column to the frame
df2['weightage'] = df2['weight'] + df2['Age']           #add a column base on other column
print(df2)

#########################################################################drop data
print(df2.drop('weightage',axis=1))        #drop column, axis=1 means column, axis=0 means row,
print(df2, ' 1111')                                    # it will return the result but print(df2) will not drop the column
print(df2.drop('weightage',axis=1,inplace=True))   #add inplace=True, the actull df2 will drop the column, it will not return
print(df2)
###########################################################################loc and iloc, index select data
print(df2.loc['a'])                      #return row a
print(df2.loc['a','Name'])               #return row a column Name
print(df2.loc[['a','b'],['Name','Age']])  #return row a,b and column Name and Age
print(df2.iloc[0])                       #return the 0th row, (result same as above line44)
print(df2.iloc[[0,2]])                   #return the 0th and 2nd row
#############################################################################condition select data
print(df2[df2['Age']>33])                       #return the person with age>33
print(df2[(df2['Age']>33) & (df2['weight']>0)]) #return the person with age>33 and weight>0
#####################################################################reset index(primery key)
print(df1.reset_index())       #reset_index change the index the number(by defult), and add a column call index with the origial index
print(df1)                     #without inplace=true not actully change
df1.reset_index(inplace=True)
print(df1)
print(df1.loc[0])
# df1['ID'] = ['a','b','c','d']                        #不知道为什么，没反应
# df1.set_index('ID')
# print(df1.loc[0])

########################################################多索引 看收藏网页

#######################################################################################清洗数据
print(df1)
print(df1.dropna())                       #by defult drop the row with NaN, axis=0 drop column, axis=1 drop row
#not actully drop the data, unless inplace=True
print(df1.fillna('ahaha'))                #fill all the NaN with ahaha, not actully fill the data,unless inplace=True

#######################################################################################分组
d = {'company':['G','G','O','O','T','T'],
     'person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
     'sales':[200,120,340,124,243,350]}
df3 = pd.DataFrame(d)
print(df3)
print(df3.groupby('company').mean())             #kinda like SQL
print(df3.groupby('company').describe())         #show the stistai data(max,min,25%qutel,50%,75%,mean,std,count)
print(df3.groupby('company').describe().transpose())    #transpose of above
print(df3.groupby('company').describe().transpose()['G'])  #only show company G

##########################################################################concat
a = df2
print(pd.concat([df2,a]))                 #concat 2 dataframe, by defult add row
print(pd.concat([df1,a],axis=1))          #axis= 1, add column

#################################################################merge
#where inner is intersection, outer is union
print(pd.merge(df1,df2,how='inner',on='Name'))          #same as join in SQL with key on=(key)
print(pd.merge(df1,df2,how='inner',on=['Name','Nationality']))   #join base on 2 keys
print(df1.join(df3,how='outer'))                 #kinda like no key merge operation

######################################################################unique value
df4 = pd.DataFrame({'c1':[2,3,2,1], 'c2':[4,5,6,7],'c3':[8,9,10,11]})
print(df4['c1'].unique())              #remove duplicate, find the element in c1
print(df4['c1'].nunique())             #count # of element
print(df4['c1'].value_counts())        #return each elememt and it's count
#######################################################################apply(function)
print(df4['c1'].apply(lambda x:x*x))          #apply the function to each element in c1
######################################################################sort
print(df4.sort_values('c1'))                 #sort the dataframe according c1
#######################################################################check isnull
print(df1.isnull())                          #return a dataframe with boolean value
#######################################################################数据透视表
df5 = pd.DataFrame({
       'A':['D','D','D','C','C','C'],
       'B':['RED','RED','BLACK','BLACK','BLUE','BLUE'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]
})
print(df5)
print(pd.pivot_table(df5,values='D',index=['A','B'],columns=['C']))
#Value:需要汇总的数据     index：row按照他们分类      colums：columns按照他们分类
#############################################################################  csv file
df5.to_csv("to_csv",index=False)        #write it to "to_csv", index=false means not save the index column [0,1,2,3,4,5]
df6 = pd.read_csv('to_csv')         #read 'to_csv' file
print(df6)
# df6.to_excel('to_excel.xlsx',sheet_name='Sheet1')         #should work but it don't, write it to excel file

######################################################################
#######################################################################
######################################################################