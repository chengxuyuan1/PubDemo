from  urllib  import  request
from  bs4 import BeautifulSoup
import  ssl

nameList=[]
scoreList=[]
coutryList=[]

url='https://movie.douban.com/chart'
def getData(url):
    context = ssl._create_unverified_context()
    res=request.urlopen(url,context=context).read().decode()
    #print(res)
    return  res


def parseData(html):
    print('')
    soup = BeautifulSoup(html,'html.parser')
    movieList=soup.find_all('div',attrs={'class':'pl2'})
    #print(movieList)
    for movie in movieList:
        movieName=movie.find('a').getText().strip('\n').strip('\t').strip('\r')
        movieScore=movie.find('span',attrs={'class':'rating_nums'}).getText()
        movieContry=movie.find('p',attrs={'class':'pl'}).getText().rstrip().split('/')[0].rstrip().split('(')[1]
        nameList.append(movieName)
        scoreList.append(movieScore)
        coutryList.append(movieContry)
        #print(movieContry)
    return nameList,scoreList,coutryList

    #return [],[],[]

def saveData(nameList,scoreList,countryList):
    #print(nameList)
    resFile=open('result.txt','w',encoding='utf-8')
    for i in range(len(nameList)):
        lineText='名字:'+nameList[i]+'\t得分:'+scoreList[i]+'\t国家：'+coutryList[i]
        resFile.write(lineText+'\n')
    resFile.close()


myHtml=getData(url)

ameList , scoreList , coutryList = parseData(myHtml)
saveData(nameList,scoreList,coutryList)