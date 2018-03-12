import requests
import re
import xlwt

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage():
    try:
        infoList = []
        for i in range(1, 6):
            url = 'http://furhr.com/?page={}'.format(i)
            html = getHTMLText(url)
            pageList = re.findall(r'<tr><td>(.*?)</td><td>\d+</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>',html)
            for i in range(len(pageList)):
                pagelist = pageList[i]
                infoList.append(pagelist)
        #print(infoList)
        #excel_write()
        return infoList
    except:
        print("error")

#写入文件
def txt_write(items):
    for item in items:
        with open('yinhang.txt','a',encoding='utf-8') as f:
            f.write(item[0]+'\t'+item[1]+'\t'+item[2]+'\t'+item[3]+'\n')
            f.close()

#写入Excel
def excel_write(items):
    #创建表格
    newTable = 'test123.xls'  #表格名称
    wb = xlwt.Workbook(encoding = 'utf-8') #创建文件，设置编码
    ws = wb.add_sheet('test1') #创建表
    headDate = ['序号','公司名称','电话','地址']
    for colnum in range(0,4):
        ws.write(0,colnum,headDate[colnum],xlwt.easyxf('font:bold on')) #0行，列，内容
    wb.save(newTable) #保存
    print('创建成功')

    #写入数据
    index = 1
    for item in items:
        for i in range(0,4):
            print(item[i])
            ws.write(index,i,item[i])#行，列，数据
        index += 1
    wb.save(newTable)
    print("ok")

if __name__ == "__main__":
    parsePage()
    items = parsePage()
    #print(parsePage())
    #print(items)
    excel_write(items)
    txt_write(items)

