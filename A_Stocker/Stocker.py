import threading
import tushare as ts
import pandas as pd
import datetime

STOCK = {'002594':[1,170.15],   ## 比亚迪 / 几手，成本价
         '601012':[6,107.55],    ## 隆基股份
         '600438':[9,42.96],    ## 通威股份
         #'002475':[3,59.51],    ## 立讯精密
         #'603308':[1,33.49],     ## 应流股份
         '002415': [3, 66.40]   ## 海康威视
         # '600559':[3,35.3],     ## 老白干
         # '601100':[1, 114.5],   ## 恒立液压
         # '603466':[6, 22.40]    ## 风语筑
}
TimerNum = 20.0 # s
Total = 0

def get_all_price():
    '''process all stock'''
    stockCode = list(STOCK.keys())
    df = ts.get_realtime_quotes(stockCode)

    lp = list(STOCK.values())

    stockNum = []
    stockCostPrice = []
    for i in range(len(lp)):
        stockNum.append(lp[i][0])
        stockCostPrice.append(lp[i][1])

    df['num'] = stockNum
    df['stockCostPrice'] = stockCostPrice
    # 处理
    # profit and lost ratio 盈亏率
    plRatio = round((df['price'].astype(float) / df['stockCostPrice'] - 1)*100,2)

    # profit and lost 盈亏
    df['plRatio'] = plRatio
    df['stockNum'] = stockNum
    pl = round(df['plRatio'].astype(float) * df['stockNum'] * df['stockCostPrice'].astype(float),2)
    df['pl'] = pl

    # 当日涨幅 Rise and fall
    currentRF = round((df['price'].astype(float) / df['pre_close'].astype(float) - 1)*100,2)
    df['currentRF'] = currentRF

    df1 = df[[ 'open', 'price', 'stockCostPrice', 'plRatio', 'num','pl', 'currentRF','name']]
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)
    pd.set_option('display.width', 180)  # 设置打印宽度(**重要**)
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 1000)
    sss = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f)")[:-4]

    print('\n')
    print("----------------" + sss +"------------------")

    print(df1)
    sum_int = round(df['pl'].sum(),2)

    print("total profit and lost is " + sum_int.astype(str))
    print('\n')

    # df.to_csv('stock_data.csv', encoding='utf_8_sig', index=None)
    global timer
    timer = threading.Timer(TimerNum, get_all_price, [])
    timer.start()


if __name__ == '__main__':
    get_all_price()
    timer = threading.Timer(TimerNum, get_all_price, [])
    timer.start()
