import sys,re
fp=open(sys.argv[1],'r')
cnt=0
aligned=0
for recs in fp:
	pattern=re.search('^@',recs)
	if not pattern:
		recs=recs.strip('\n')
		data_recs=recs.split('\t')
		#print data_recs[11]
		#NM:i:4
		NM_tag=re.search('NM.+\:(\d+)',data_recs[11])
			
		if NM_tag:
			cnt+=int(NM_tag.group(1))
			aligned+=50
			#print(NM_tag.group(1))
fp.close()

print(float(float(cnt)/float(aligned)))
