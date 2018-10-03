import  pymysql
nameList=[]
scoreList=[]
coutryList=[]
def readTxt():
    txtFiel=open('result.txt','r',encoding='utf-8')
    line=txtFiel.readline()
    #print(line)
    while line:
        str=line.split()
        #print(str)
        name=str[0].split(':')[1]
        #print(name)
        score = str[1].split(':')[1]
        #print(score)
        country = str[2].split(':')[1]
        #print(country)
        nameList.append(name)
        scoreList.append(score)
        coutryList.append(country)
        line = txtFiel.readline()
    txtFiel.close()

readTxt()
print(nameList)
def openDB():
    conn=pymysql.connect(user='root',password='mysql',host='localhost',db='test')
    cursor=conn.cursor()
    sql='create table movie(movie_name char(20) NOT NULL,score char(10),country char(20))'
    cursor.execute(sql)
    sqlInsert='insert into movie(movie_name,score,country) values(%s,%s,%s)'
    for i in range(len(nameList)):
        value =(nameList[i],scoreList[i],coutryList[i])
        cursor.execute(sqlInsert%value)
    conn.commit()