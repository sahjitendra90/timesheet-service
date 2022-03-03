from fastapi import FastAPI, File, UploadFile
# from pymongo import MongoClient
# from student import sheet
import pandas as pd
from pandas.tests.indexing.multiindex.test_indexing_slow import df

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(excel_file: UploadFile = File(...)):

    contents = excel_file.file.read()
    df = pd.read_excel(contents)
    print(df)
    return {"filename": excel_file.filename}

wb = df.open_workbook('excel_file')
sh = wb.sheet_by_index(2)
for i in range(138):
    cell_value_class = sh.cell(i,2).value
    cell_value_id = sh.cell(i,0).value


#
# dict1 = {"number of storage arrays": 45, "number of ports":2390}
#
# df = pd.DataFrame(data=dict1, index=[0])
#
# df = (df.T)
#
# print (df)
#
# df.to_excel('dict1.xlsx')

 # data = pd.df()
 # rows =data.iloc[0:6]


# xl_file = pd.ExcelFile((df)
# dfs = {sheet_name: xl_file.parse(sheet_name) for sheet_name in xl_file.sheet_names}


# client = MongoClient()

#     db = client["timesheet"]
#     msg_collection = db["data"]
#
#     # Create a message dict
#     message = {
#         filename:df
#     }
#     result = msg_collection.insert_one(message)
#     print(result.inserted_id)


    # client = MongoClient("localhost", 27017, maxPoolSize=50)
    # mydb=client["mydb"]
    # data=excel_file
    # mydb.insert_one(data)








