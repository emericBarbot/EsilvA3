import pandas as pd


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
#print(df.Superficie[1:])

#%% Ex12
#print(df[df['Population']>700000].index)

#%% Ex13
#print(df[df.Superficie])
#print(df.sort_values(by='Superficie',ascending=False).index)

TabNote=pd.read_csv("TabNote.csv")
Matiere=pd.read_csv("Matiere.csv")
Etudiant=pd.read_csv("Etudiant.csv")
#print(type(TabNote))
#%% Ex4
#print(TabNote.info())
#print(TabNote.describe())
#print(TabNote.isna().sum().sum())
TabNote=TabNote.fillna(0)
TabNote=TabNote[TabNote["Note"]!=0]
TabNote=TabNote[["NumE","Note"]]
print(TabNote)