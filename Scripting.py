import pandas as pd


def textFileRead():
    # read text file into pandas DataFrame
    # df = pd.read_csv("data.txt")
    df1 = pd.read_table("data.txt")
    # display DataFrame
    print(df1)
    print(df1.size)
    print(df1.shape)
    df2 = df1.iloc[:, [1]]
    # print(df2)
    # Conditional slicing
    df3 = df1.loc[df1['DiseaseType'] == "a"]
    # print(df3)
    for rows in df3.iterrows():
        # take second tuple from the row
        z = rows[1]
        # take any column from value
        print(z[2])

    # take another datasheet
    dfGene = pd.read_table("GeneData.txt")
    # joining multiple dataframes with condition
    df_cd = pd.merge(df1, dfGene, how='inner', on='ID')

    print(df_cd)

    # data writing to file
    df_cd.to_csv(r'pandas.txt', index=None, sep=' ', mode='w')

