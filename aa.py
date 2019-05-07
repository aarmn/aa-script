#!/usr/bin/env python3
import os
import platform
import subprocess
from time import sleep

cyan='\033[96m'
end='\033[0m'
back='\033[44m'

def yesno(txt):
	txt=txt.lower()
	if (txt=="y" or txt=="yes" or txt=="yep" or txt=="yeah"):
		return True
	if (txt=="n" or txt=="no" or txt=="nope" or txt=="not"):
		return False
	return None
    
def angryinput(text="",list=None,func=None):
	while (1):
		tt=input(text)
		if func!=None:
			if func(tt)==None:
				continue
			
		if list!=None:
			if not (tt in list):
				continue
		return tt
            
    
def ResetBash():
	print("\n So Run: source ~/.bashrc \n")
	sleep(0.5)
    
AsciiArt='''
     ___           ___      
    /   \         /   \     
   /  ^  \       /  ^  \    
  /  /_\  \     /  /_\  \   
 /  _____  \   /  _____  \  
/__/     \__\ /__/     \__\ 
                            
     _______. _______ .___________. __    __  .______   
    /       ||   ____||           ||  |  |  | |   _  \  
   |   (----`|  |__   `---|  |----`|  |  |  | |  |_)  | 
    \   \    |   __|      |  |     |  |  |  | |   ___/  
.----)   |   |  |____     |  |     |  `--'  | |  |      
|_______/    |_______|    |__|      \______/  | _|      
                                                        

'''

Script='''
#####AA Zone#####
#3

###codes,color and etc###
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'   
    alias dir='dir --color=auto'  
    alias vdir='vdir --color=auto'
    alias grep='grep --color=auto'  
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi
export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

###alias###
alias lsx="ls -ltrha"
alias KILLME="sudo rm -rf /"

###funcs###
mkcdir ()
{
        #Copied from stackoverflow
        mkdir -p -- "$1" &&
        cd -P -- "$1"
}

#Lags on rmdirx and rmhere 

rmx ()
{
        echo "${1:-$(ls -a)}" | xargs rm -rf
}

rmhere ()
{
        DELHEREPATH=$PWD
        rmdirx
        cd ..
        rmdir $DELHEREPATH
}

fexe (){
        chmod +x "$1"
        ./"$1"
}

giton(){
        git init .
        touch README.md
        touch LICENSE
        touch .gitignore
        git add *
        git add .gitignore
        git commit -m "${1:-"Initial Commit"}"
}

#-p for push 

gitup(){
        git add *
        git commit -m "$1"
}

gitconfg(){
        git config --global user.name "$1"
        git config --global user.email "$2"
}

gitconf(){
        git config user.name "$1"
        git config user.email "$2"
}

#####AA Zone#####
'''

#FUTURE : Online Update

print(back+cyan+AsciiArt)
print("A Tiny Script By AARMN The Limitless To Ease Bash With Some Funcs And Aliases\n")

if (platform.system()!="Linux"):
	print("Installer Work Only On Gnu\Linux OS , If You Have Bash Installed In Your OS,  Copy Script Var From Source to Your .bashrc File In Home Folder Of Your OS")
	exit()

bash=str(subprocess.check_output(["bash","--version"])).find("GNU bash")
if (bash==-1):
	print("There Is No Bash In Your System PATH , Try to Install Or Reinstall It")
	exit()

Home=os.path.expanduser("~")

try:
	Bashrc=open(os.path.join(Home,".bashrc"),"r")
except IOError:
	ans3=yesno(angryinput("You Don't Have A Bashrc, Can I Create One? (Yes/No)",func=yesno))
	if not (ans3):
            exit()
	Bashrc=open(os.path.join(Home,".bashrc"),"w+")
	Bashrc.close()

Bashrc=open(os.path.join(Home,".bashrc"),"r")
ans=None
BashrcString=Bashrc.read()
Bashrc.close()
StartScript=BashrcString.find('#####AA Zone#####\n')
EndScript=BashrcString.find('#####AA Zone#####\n',StartScript+1)
WithoutScript=BashrcString[0:StartScript]+BashrcString[EndScript+17:-1]
InstalledScript=BashrcString[StartScript:EndScript+17]
TagCount=0

def InstallScript():
	try:
		Bashrc=open(os.path.join(Home,".bashrc"),"a")
	except IOError:
		print("I Think Bashrc Is Write Protect, Fix It And Run Code Again")
		exit()
	Bashrc.write(Script)
	Bashrc.close()
def UninstallScript():
	try:
		Bashrc=open(os.path.join(Home,".bashrc"),"w")
	except IOError:
		print("I Think Bashrc Is Write Protect, Fix It And Run Code Again")
		exit()
	Bashrc.write(WithoutScript)
	Bashrc.close()
def FindVer(start,scriptstr):
	endline="\n"
	ListTmpVer=list()
	step=start+19
	while(scriptstr[step]!=endline):
		ListTmpVer.append(scriptstr[step])
		step+=1
	return int(''.join(ListTmpVer))
    
Bashrc=open(os.path.join(Home,".bashrc"),"r")
for line in Bashrc:
	if (line=="#####AA Zone#####\n"):
		TagCount+=1
Bashrc.close()

nonew="This Script Don't Have A New Version Of AA"
installthem="To Upgrade Bash to Next Level We Suggest You to Install More Fancy Stuff too \nDo You Want to Install:"
bashit="1.Bashit"
omb="2.Oh My Bash"
iowt="3.None Of Them, AA is Enough"
donesad="Done :("
donehappy="Done :)"
wisechoice="Wise Choice :)"
letsinstall="AA Is Not Installed Yet, Do You Want to Install? (Yes/No) : "
pbbutinstalled="AA Is Not Installed Successfully (Or You Want to Trick Us ... HAHAHAHA), Do You Want to Install Anyway? (Just Add Commands to End) (Yes/No) : "
cancelit3="3.Cancel"
cancelit2="2.Cancel"
uninstallit="1.Uninstall AA"
newincompatver="Your Version Is Newer And Backward Incompatible Or You Have A Corrupt Version of AA In Your Bashrc,In This Situation Try Delete It Manually And Have A New Installed"
upgradeit="2.Down/Up-grade AA"
otherver="If You Want to Upgrade Or Find It Useless, This Script Contain a diffrent ver"
olderver="But It's Older :("
newerver="Good News, It's New :)"
resetshell="To Effect Changes You Need To Run A New Bash Or Source Bashrc, Do You Want To Source Bashrc? (If You Are Already Running This In Bash Its Recommended) (Yes/No) : "

if (TagCount==0):
	ans=yesno(angryinput(letsinstall,func=yesno))
	if (ans):
		InstallScript()
		ansreset=yesno(angryinput(resetshell,func=yesno))
		if (ansreset):
			ResetBash()
		print(donehappy)
elif (TagCount==1):
	ans=yesno(angryinput(pbbutinstalled,func=yesno))
	if (ans):
		InstallScript()
		ansreset=yesno(angryinput(resetshell,func=yesno))
		if (ansreset):
			ResetBash()
		print(donehappy)
elif (TagCount==2):
	if (('\n'+InstalledScript+'\n')==Script):
		print(nonew)
		print(uninstallit)
		print(cancelit2)
		ans2=0
		ans2=int(angryinput(list=["1","2"]))
		if (ans2==1):
			UninstallScript()
			ansreset=yesno(angryinput(resetshell,func=yesno))
			if (ansreset):
				ResetBash()
			print(donesad)
		else:
			print(wisechoice)
	else:
		print(otherver)
		try: 
			if (FindVer(0,InstalledScript)<FindVer(1,Script)):
				print(newerver)
			else :
				print(olderver)
		except:
                    print(newincompatver)
		print("We Have 3 Options: ")
		print(uninstallit)
		print(upgradeit)
		print(cancelit3)
		ans2=0
		ans2=int(angryinput(list=["1","2","3"]))
		if (ans2==1):
			UninstallScript()
			ansreset=yesno(angryinput(resetshell,func=yesno))
			if (ansreset):
				ResetBash()
			print(donesad)
		if (ans2==2):
			UninstallScript()
			InstallScript()
			ansreset=yesno(angryinput(resetshell,func=yesno))
			if (ansreset):
				ResetBash()
			print(donehappy)
else:
	ans=yesno(angryinput(pbbutinstalled,func=yesno))
	if (ans):
		InstallScript()
		ansreset=yesno(angryinput(resetshell,func=yesno))
		if (ansreset):
			ResetBash()
		print(donehappy)

print("\nThis project is in early stages and its more about ease and fun, if you like this give us star on gitlab and github, check other project, report bugs, pull request new features and so on, Wish you best, Bye Bye :)\n")
print(end)
print('\n')
