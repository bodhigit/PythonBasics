# import the modules
from pymysql import*
import xlwt
import pandas.io.sql as sql

# connect the mysql with the python
con=connect(user="root",password="",host="localhost",database="db_201027235702")

# read the data
df=sql.read_sql('select student_other_details.mothername,student_details.* from student_other_details join student_details on student_other_details.userid=student_details.userid',con)

# print the data
#print(df)

# export the data into the excel sheet
df.to_excel('student_all_details.xls')