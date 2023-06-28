import pandas as pd

def get_final_df(xlsFile):
    xls = pd.ExcelFile(xlsFile)
    df1 = pd.read_excel(xls, 'agenda')
    df2 = pd.read_excel(xls, 'roleplayers')
    rolePlayers=dict()

    for index, row in df2.iterrows():
        rolePlayers[row[0]]=row[1]

    for i in range(0, len(df1)):
        key=df1.loc[i,'role players']
        if key in rolePlayers.keys():
            print(key)
            df1.loc[i,'role players']=rolePlayers[key]
    return df1

df=get_final_df('Automate-everything-with-python/CAMTMagenda.xlsx')
print(df)
