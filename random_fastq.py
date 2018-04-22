import random,sys,re
seq=''
random_base_insert=['A','T','G','C']
fp=open(sys.argv[1],'r')
for recs in fp:
    recs=recs.strip('\n')
    pattern=re.search('^>',recs)
    if pattern:
        next
    else:
        seq+=recs
fp.close()
quality=''
for i in range(0,50):
    quality+='1'
header='@HWWI:1:FCX:1:15:6329:1045 1:N:0:2'
for x in range(100000):
    read=''
    val=random.randint(0,len(seq)-50)
    val2=random.randint(0,50)    
    for y in range(0,50):
        if int(x)<=1000:
            
            #val2=random.randint(0,50)
            if int(y)==int(val2):
                read+=random_base_insert[random.randint(0,3)]
                
           
            else:
                read+=seq[val+y]
        else:
            read+=seq[val+y] 
    print(header+'\n'+read+'\n+\n'+quality)
