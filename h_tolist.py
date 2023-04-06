import load


def h_tolist(df):
    df=df.sort_values(by='Date')
    dfx = df[['Price']]
    dfy = df[['Price']] 
    x =dfx.values.tolist()
    y= dfy.values.tolist()
    return x,y