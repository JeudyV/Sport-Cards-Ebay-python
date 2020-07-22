import pandas as pd
from sqlalchemy import create_engine
import ebaysdk
from ebaysdk import finding
from ebaysdk.finding import Connection as finding
import os

user = os.getenv("DBUSER", 'root')
passw = os.getenv("DBPASS", '1234')
host = os.getenv("DBHOST", 'localhost')
port = os.getenv("DBPORT", 3306)
database = os.getenv("DBDATABASE", 'test_ebay_db_db_name') 
appid = os.getenv("APPID", 'HaokunLi-KACards-PRD-f2eb84a53-383636d9') 

mydb = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database, echo=False)

def search_for_articles(year, company, see, player, db_name):
    api = finding(appid=appid)

    api.execute ('findItemsAdvanced', {
        'keywords': f'{year}, {company}, {see}, {player}',
    }
    )

    dictstr = api.response.dict()
    print("1")
    df = pd.DataFrame(dictstr["searchResult"]["item"]).astype(str)
    print("2")
    df.to_sql(name=db_name, con=mydb, index=False, if_exists='replace')
    print("3")


search_for_articles("2020", "Panini", "Prizm", "Kobe Bryant", "db_name")