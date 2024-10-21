import pandas as pd

def createDataFrame():
    df = pd.DataFrame(columns=['LC1', 'LC2', 'LC3', "time"])
    return df

def appendDataFrame(df, LC_1, LC_2, LC_3, time):
    df = pd.concat([df, pd.DataFrame([[LC_1, LC_2, LC_3, time]], columns=['LC1', 'LC2', 'LC3', "time"])], ignore_index=True, axis=0)
    return df

def saveDataFrame(df, name='test.xlsx'):
    df.to_excel(name)

##df = createDataFrame()
##df = appendDataFrame(df, 5, 6, 8, 7)
##saveDataFrame(df)