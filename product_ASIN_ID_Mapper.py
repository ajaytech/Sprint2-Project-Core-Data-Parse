import io
fNew = open('./product_LIST_MAIN.txt','w')
#writer = csv.writer(fNew)
output = []
ASIN = ""
allProd = dict()
with io.open("amazon-meta.txt","r",encoding="utf-8") as f:
    for row in f:
        if len(row) > 0:
            if not row.encode("utf-8").strip().find('Id:',0,3) == -1:
                idASIN = row[3:].strip()
            if not row.encode("utf-8").strip().find('ASIN:',0,5) == -1:
                ASIN = row[5:].strip()
                if not allProd.get(ASIN):
                    allProd[ASIN] = idASIN
                else:
                    if allProd[ASIN] == -1:
                        allProd[ASIN] = idASIN
            if not row.encode("utf-8").strip().find('similar:',0,11) == -1:
                rowSimillar = row[11:].strip().split("  ")
                if(len(rowSimillar) == 1  and int(rowSimillar[0])==0):
                    continue
                for i in range(len(rowSimillar)):
                    if not allProd.get(rowSimillar[i]):
                        allProd[rowSimillar[i]] = -1
                

idASIN = int(idASIN) +1
for key in allProd:
    if allProd[key] == -1:
             allProd[key] = idASIN
             idASIN = idASIN + 1    


for key in allProd:
    fNew.write(str(allProd[key])+"\t"+key+"\n")


f.close()
fNew.close()