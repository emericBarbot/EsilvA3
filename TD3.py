import pandas as pd
"""

s=pd.Series([100,200,'chat','lapin'],index=['a','b','c','d'])
print(s)
print(s.keys())

print(s.index)
print(s[0])
s['a']


s.index=['a1','b1','c1','d1']
print(s)

s2=s
print(s2)
s3=s.append(s2)
print(s3)

dico={
      'chaton':[1,2,3],
      'chien':[4,5,6],
      'lapin':[7,8,9]
}
df=pd.DataFrame(dico,index=['nb','prix','nb2'])
print(df)
print(df.loc[1])
"""

#1
Pop=pd.Series([2187526,863310,516092,479553,340017],
              index=["Paris","Marseille","Lyon","Toulouse","Nice"])

Superficie=pd.Series([105.4,240.6,47.87,118.3,71.92],
                     index=["Paris","Marseille","Lyon","Toulouse","Nice"])

#print(Pop["Lyon"],Superficie["Lyon"])

df = pd.DataFrame({
    'Population': Pop,
    'Superficie': Superficie
})
#print(df.head(1))
#print(df.tail(3))
#5
#print(df.info)
#print(df.shape)
#print(df.describe())
#print(df["Paris"])
#print(df["Marseille"])
#print(df)
#print(df.iloc[1:3])
print(df.Superficie[1:])