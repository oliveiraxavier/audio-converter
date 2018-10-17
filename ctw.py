#!/usr/bin/python
#sudo  ln -s  /home/marcos/scripts/ctw.py /usr/bin/caudio
#Executar como caudio 
#

art  = """\   _____              .___                                  
  /     \ _____     __| _/______  ____   _________    ______
 /  \ /  \\__  \   / __ |\_  __ \/  _ \ / ___\__  \  /  ___/
/    Y    \/ __ \_/ /_/ | |  | \(  <_> ) /_/  > __ \_\___ \ 
\____|__  (____  /\____ | |__|   \____/\___  (____  /____  >
        \/     \/      \/             /_____/     \/     \/
        """
print(art)        
import os
import argparse
import glob
parser = argparse.ArgumentParser()
parser.add_argument('--i', help='i help')
parser.add_argument('--o', help='o help')
parser.add_argument('--t', help='t help')
parser.add_argument('--f', help='f help')
args = parser.parse_args()
fileDir = args.i
saveDir = args.o
typeIn  =args.f
typeOut = args.t
allfiles = glob.glob(fileDir+"/*."+typeIn)
for f in allfiles:
	originalName = os.path.basename(f)
	newFile = os.path.splitext(originalName)[0]
	os.system("mkdir -p "+saveDir)
	os.system("sox "+f+" "+saveDir+"/"+newFile+"."+typeOut)
print("Verifique os arquivos em "+saveDir)