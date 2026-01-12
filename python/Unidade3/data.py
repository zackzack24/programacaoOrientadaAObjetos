from datetime import datetime

def formatarData(data = datetime.now(), formato = '%d/%m/%Y'):
    return datetime.strftime(data, formato)

def criarData(data, formato = '%Y-%m-%d'):
    return datetime.strptime(data,formato)

data1 = datetime(2024,2,17)  
data2 = '2023-02-17'        
print(data1)
print(data2)

data = datetime(2017,10,20)
data = datetime.now()
formatarData( formato='%m')

print(datetime.strptime('2023-10-07','%Y-%m-%d')) 