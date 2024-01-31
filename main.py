import pandas as pd

class stats:
    def __init__(self,name):
        self.name=name
        self.Min=None
        self.Max=None
        self.Mean=None
        self.SD=None
    def Print(self):
        print(f"{self.name}: {self.Min},{self.Max},{self.Mean},{self.SD}")

data =  pd.read_csv('iris.data', sep=",")
print(data)
SepalL=stats('Sepal Length')
SepalL.Min=min(data.iloc[:,0])
SepalL.Max=max(data.iloc[:,0])
SepalL.Mean = data.iloc[:,0].mean()
SepalL.SD = data.iloc[:,0].std()
SepalL.Print()

SepalW=stats('Sepal Width')
SepalW.Min=min(data.iloc[:,1])
SepalW.Max=max(data.iloc[:,1])
SepalW.Mean = data.iloc[:,1].mean()
SepalW.SD = data.iloc[:,1].std()
SepalW.Print()

PetalL=stats('Petal Length')
PetalL.Min=min(data.iloc[:,2])
PetalL.Max=max(data.iloc[:,2])
PetalL.Mean = data.iloc[:,2].mean()
PetalL.SD = data.iloc[:,2].std()
PetalL.Print()

PetalW=stats('Petal Width')
PetalW.Min=min(data.iloc[:,3])
PetalW.Max=max(data.iloc[:,3])
PetalW.Mean = data.iloc[:,3].mean()
PetalW.SD = data.iloc[:,3].std()
PetalW.Print()