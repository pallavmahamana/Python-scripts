PATHIN = "C:\\Users\\Pallav\\Desktop\\filein.csv"    # Input csv file
PATHOUT =  "C:\\Users\\Pallav\\Desktop\\fileout.vcf"      # Output vcf file

def issci(i):
	for j in range(0,len(i)):
		if i[j]=='+' or i[j]=='E' or i[j]=='e':
			return 1
	return 0


def parsename(bar):
	bar = bar.split(',')
	name = bar[0]
	return name

def parsenum(bar):
	bar = bar.split(',')
	for i in bar:
		if i!='':
			if not issci(i) :
				num = i
				return num
	return None		
				
	
def chckhasnum(bar):
	bar = bar.split(',')
	bar[0]=''
	for i in bar:
		if i!='':
			if not issci(i) :
				return 1
	return 0


fi = open(PATHIN)
fo = open(PATHOUT,'w') 
accepted = 0 
rejected = 0
print "\n"
for line in fi.readlines():
	line = line.replace('\n','')
	accepted+=1
	if chckhasnum(line):
		fo.write('BEGIN:VCARD\nVERSION:3.0\n')
		string = parsename(line)
		line = line[len(string):len(line)]
		fo.write("N:;"+string+";;;\n")
		fo.write("FN:"+string+"\n")
		while chckhasnum(line):
			num = parsenum(line)
			if num is not None:
				if len(num)!=1:
					line = line.replace(num,',')
					num = "TEL;TYPE=CELL:"+num+"\n"
					fo.write(num)
					num=None
				else:
					line = line.replace(num,',')
		fo.write("END:VCARD\n")
	else:
		rejected+=1
		foo = line.split(',')
		print foo[0]+" <<Rejected>>"
		
print "\n\n",accepted," out of ",(accepted+rejected)," contacts converted"
print round(float(accepted)/float(accepted+rejected)*100,2),"% Efficiency"
fo.close()
fi.close()

