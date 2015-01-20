# Adds 0 to all the numbers 

FILEIN = "C:\\Users\\Pallav\\Desktop\\file.vcf"
FILEOUT = "C:\\Users\\Pallav\\Desktop\\fileout.vcf"

fi = open(FILEIN)
fo = open(FILEOUT,'w')
A=0
B=0
C=0
D=0



for line in fi.readlines():
	flag=0
	if line.find("L:9")!=-1:
		fo.write(line.replace("L:9","L:09"))
		A+=1
		flag=1
	
	if line.find("L:8")!=-1:
		fo.write(line.replace("L:8","L:08"))
		B+=1
		flag=1
	
	if line.find("L:7")!=-1:
		fo.write(line.replace("L:7","L:07"))
		C+=1
		flag=1
	
	if line.find("L:5")!=-1:
		fo.write(line.replace("L:5","L:05"))
		D+=1
		flag=1
	
	if flag!=1:
		fo.write(line)

fi.close()
fo.close()
		
print "Total 09 replacements is",A
print "Total 08 replacements is",B
print "Total 07 replacements is",C
print "Total 05 replacements is",D		