import sys

reload(sys)
sys.setdefaultencoding('cp949')

keySet1 = sys.argv[1]
keySet2 = sys.argv[2]

f1 = open(keySet1, 'r')
f2 = open(keySet2, 'r')
outputfile = open('out','w')

for n in f1:
	f2 = open(keySet2, 'r')
	for m in f2:
		binded = n+m
		binded = binded.replace('\n','')
		print (binded)
		outputfile.write(binded + '\n')
f1.close
f2.close
outputfile.close
