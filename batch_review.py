#!/usr/local/bin/pythonw
batch_file = open('/Users/VillordoMendoza/Documents/PruebasPython/batch.txt')
ciops_file = open('/Users/VillordoMendoza/Documents/PruebasPython/ciops.txt')

batch = {}
ciops = {}
finalbatch = {}
finalciops = {}
lista = list()
batch_line = batch_file.readlines()
ciops_line = ciops_file.readlines()

resultado = 0

# READ BATCH FILE
for i in batch_line:
    lista = i.split(' ')
    num = int(lista[1])
    if lista[0] not in batch:
        batch[lista[0]] = [num]
    else:
        batch[lista[0]].append(num)
# READ CIOPS FILE
for f in ciops_line:
    lista = f.split(' ')
    num = int(lista[1])
    if lista[0] not in ciops:
        ciops[lista[0]] = [num]
    else:
        ciops[lista[0]].append(num)
        
for g,h in batch.iteritems():
    resultado = sum(h) 
    finalbatch[g] = [resultado]

for r,w in ciops.iteritems():
    resultado = sum(w)
    finalciops[r] = [resultado]
    
print 'BATCH ','       CIOPS'
for key in finalbatch:
    if key in finalciops:
        print str(key)+' '+str(finalbatch[key]),str(key)+' '+str(finalciops[key])
    else:    
        print str(key)+' '+str(finalbatch[key])
         
batch_file.close()
ciops_file.close()
