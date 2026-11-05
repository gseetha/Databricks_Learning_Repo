from pathlib import Path
import pandas as pd
test_file =r"C:\Users\555782\OneDrive - TMNA\Desktop\py_de_ai_project\landing\cust.csv"
file_path=Path(test_file)
df=pd.read_csv(file_path)
row_count = len(df)
#print (row_count)
column_profile=pd.DataFrame({"column_name":df.columns,"datatype":df.dtypes,"null_count":df.isnull().sum().values,"actual_count":row_count,"unique_count":df.nunique().values})
#print(column_profile)

data_type=df.dtypes.astype(str).to_dict()
duplicates =df.duplicated().sum()
print(duplicates)



