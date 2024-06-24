import pandas as pd
from datetime import timedelta,datetime,date

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()




@app.get("/")
def read_root():
    return {"status yfinance": "OK"}


@app.get("/symbol/dates",description='Devuelve info')
async def get_dates(symbol:str,ini_date:str,fin_date:str,interval:str):

    interval_ok= ['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo']

    if interval not in interval_ok:
        raise 'Error interval'
    
    ini_year, ini_month, ini_day = ini_date.split('-')
    fin_year, fin_month, fin_day = fin_date.split('-')

    if int(ini_month) not in range(1,13) or int(fin_month) not in range(1,13):
        raise HTTPException(status_code=400,detail='Error in month, format will be "yyyy-mm-dd"')
    if int(ini_day) not in range(1,32) or int(fin_day) not in range(1,32):
        raise HTTPException(status_code=400,detail='Error in day, format will be "yyyy-mm-dd"')


    try:
        
        i_date = int(datetime.strptime(ini_date,'%Y-%m-%d').timestamp())
        f_date = int(datetime.strptime(fin_date,'%Y-%m-%d').timestamp())
        
        url=f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={i_date}&period2={f_date}&interval={interval}&events=history&includeAdjustedClose=true'
        print(url)
        return pd.read_csv(url).to_dict(orient='records')
    
    except Exception as e:
        return {'Error':str(e)}
