#!/usr/bin/python
#sudo  ln -s  /home/marcos/scripts/ctw.py /usr/bin/caudio
#Executar como caudio 
#

art  = """
MMMMMMMM               MMMMMMMM                                                                                           
M:::::::M             M:::::::M                                                                                           
M::::::::M           M::::::::M                                                                                           
M:::::::::M         M:::::::::M                                                                                           
M::::::::::M       M::::::::::M  aaaaaaaaaaaaa  rrrrr   rrrrrrrrr       cccccccccccccccc   ooooooooooo       ssssssssss   
M:::::::::::M     M:::::::::::M  a::::::::::::a r::::rrr:::::::::r    cc:::::::::::::::c oo:::::::::::oo   ss::::::::::s  
M:::::::M::::M   M::::M:::::::M  aaaaaaaaa:::::ar:::::::::::::::::r  c:::::::::::::::::co:::::::::::::::oss:::::::::::::s 
M::::::M M::::M M::::M M::::::M           a::::arr::::::rrrrr::::::rc:::::::cccccc:::::co:::::ooooo:::::os::::::ssss:::::s
M::::::M  M::::M::::M  M::::::M    aaaaaaa:::::a r:::::r     r:::::rc::::::c     ccccccco::::o     o::::o s:::::s  ssssss 
M::::::M   M:::::::M   M::::::M  aa::::::::::::a r:::::r     rrrrrrrc:::::c             o::::o     o::::o   s::::::s      
M::::::M    M:::::M    M::::::M a::::aaaa::::::a r:::::r            c:::::c             o::::o     o::::o      s::::::s   
M::::::M     MMMMM     M::::::Ma::::a    a:::::a r:::::r            c::::::c     ccccccco::::o     o::::ossssss   s:::::s 
M::::::M               M::::::Ma::::a    a:::::a r:::::r            c:::::::cccccc:::::co:::::ooooo:::::os:::::ssss::::::s
M::::::M               M::::::Ma:::::aaaa::::::a r:::::r             c:::::::::::::::::co:::::::::::::::os::::::::::::::s 
M::::::M               M::::::M a::::::::::aa:::ar:::::r              cc:::::::::::::::c oo:::::::::::oo  s:::::::::::ss  
MMMMMMMM               MMMMMMMM  aaaaaaaaaa  aaaarrrrrrr                cccccccccccccccc   ooooooooooo     sssssssssss
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
