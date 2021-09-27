import csv
import pymongo
import os

def mongoClient(doc):
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = db_client["TradingData"]
    mycol = mydb[doc]
    if doc in mydb.list_collection_names():
        mycol.drop()
    return mycol

def csv2mongo(path):
    db = mongoClient(path)
    title_list  = ['成交日期','商品代號','到期月份(週別)','成交時間','成交價格','成交數量(B+S)','近月價格','遠月價格','開盤集合競價']
    for filename in os.listdir(path+'/'):
        print("Reading",path,filename,'...')
        with open(path+'/'+filename, newline='') as csvfile:
            rows = csv.reader(csvfile)
            all_data = []
            data = {}
            for idx,row in enumerate(rows):
                data = dict(zip(title_list,[ele.replace('-','').strip() for ele in row]))
                if(data.get('成交日期')):
                    data['成交數量(B+S)'] += row
                # if idx!=len(rows)-1 and rows[idx+1][3] != row and rows[idx+1][]:
                #     all_data.append(data)
                #     data.clear()
            db.insert_many(all_data[1:])


mycol = mongoClient('DailyFuturesCSV')
for x in mycol.find():
    print(x)

# if __name__ == '__main__':
    # csv2mongo('DailyFuturesCSV') 
    # csv2mongo('DailyOptionsCSV')


# load()

