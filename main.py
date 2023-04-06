import settings
import pandas as pd
import matplotlib.pyplot as plt
import load, h_tolist, h_prepro, h_split, h_modelfit


def main():
    '''
    컨트롤러 실행 한다
    실행 유무
    ETL
    '''
    
    df= load.read()
    x,y=h_tolist.h_tolist(df)
    data_x,data_y=h_prepro.h_prepro(x,y)
    train_x, train_y, test_x, test_y=h_split.h_split(data_x,data_y)
    pred_y=h_modelfit.h_modelfit(train_x,train_y,test_x)



    plt.figure()
    plt.plot(test_y, color='red', label='real target y')
    plt.plot(pred_y, color='blue', label='predict y')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    print('start_main')
    main()
    print('end_main')
e