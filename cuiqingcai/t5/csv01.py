import  csv

with open('data.csv','w') as csvfile:
    #writer = csv.writer(csvfile,delimiter=' ')
    #writer.writerow(['id','name','age'])
    #writer.writerow(['10002','Mike','20'])
    #writer.writerow(['10003','Bob','22'])
    #writer.writerow(['10004','Jordan','21'])
    ##writer.writerow([['10005','A',22],['10006','A',22],['10007','A',22]])
    fieldnames = ['id','name','age']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'10002','name':'Mike','age':'20'})
    writer.writerow({'id':'10003','name':'Bob','age':'22'})
    writer.writerow({'id':'10004','name':'Jordan','age':'21'})

with open('data.csv','a',encoding='utf-8') as csvfile:
    fieldnames = ['id','name','age']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writerow({'id':'10005','name':'王伟','age':'21'})




with open('data.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)