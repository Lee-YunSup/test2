import settings
import pandas as pd

def read()->pd.DataFrame:
    '''
    settings 의 path를 통해 데이터를 읽어 옴
    '''

    df= pd.read_csv(settings.path)
    df=df.sort_values(by='Date')

    return df

# test confilt