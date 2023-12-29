#!/usr/bin/env python3
import os
import shutil
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
            
def DetectShell():
	Shell = os.popen('echo $SHELL').read()
	if('zsh' in Shell):
		return '.zshrc'
	return '.bashrc'

def ResetShell():
	if(DetectShell() == '.bashrc'):
		print("\n So Run: source ~/.bashrc \n")
		sleep(4)
	elif(DetectShell() == '.zshrc'):
		print("\n So Run: source ~/.zshrc \n")
		sleep(4)
AsciiArt=r'''
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
|_______/    |_______|    |__|      \______/  |__|      
                                                        

'''

Script=r'''
#####AA Zone#####
#11

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
alias lsx="ls -ltrhAi --author --color=auto --hyperlink=always -s"
alias KILLME="sudo rm -rf /"
alias LAGME=":(){ :|: & };:"

###funcs###

mkcdir ()
{
    mkdir -p -- "$1" &&
    cd -P -- "$1"
}

rmx ()
{

	RED="\e[1;31m"
	YELLOW="\e[1;33m"
	NOCOLOR="\e[0m"
	Forced="1"
	FolderCon="1"

    for var in "$@"
    do
        if [ "$var" = "-f" ] || [ "$var" = "--force" ]
        then
            Forced="0"
        fi
    done

	echo -e "${YELLOW}"
	pwd
	echo -e "${NOCOLOR}"
	echo -e "${RED}"

    lsx -lAd "${@}" | head -n 10
    ret=$?
    varnumline=$(($(ls -lAd "${@}" | wc -l)-10))
    if (( varnumline > 0 ))
    then
        echo -e "and $varnumline more"
    fi
	echo -e "${NOCOLOR}"

	if [ "$ret" -eq "0" ]
	then
		if [ "$Forced" -eq "0" ]
		then
			answertodel="y"
            echo 
		else
            printf "Are you Sure (Type y for continue): "
			read answertodel
		fi
	else
		answertodel="Danger"
	fi
	if [ "$answertodel" = "y" ] || [ "$answertodel" = "Y" ]
	then
        echo "${@:-$(ls -A)}" | xargs -l rm -rf
	else
        echo -e "${RED}Operation cancelled${NOCOLOR}"
		return 1
        fi
	return 0
}

rmhere ()
{
    RED="\e[1;31m"
	YELLOW="\e[1;33m"
	NOCOLOR="\e[0m"
    DELHEREPATH=$PWD
    echo -e "${YELLOW}"
    echo "Files which gonna be deleted:"
    echo -e "${NOCOLOR}"
    echo -e "${RED}"
    lsx
    echo -e "${NOCOLOR}"
    rmx
	if [ "$?" -eq "0" ]
	then
	    cd ..
        rmdir $DELHEREPATH
	fi
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
    git add . 
	if [[ "$1" = "" ]]
	then
	    git commit
	else
        git commit -m $1
	fi
}

gitconfg(){
    git config --global user.name "$1"
    git config --global user.email "$2"
}

gitconf(){
    git config user.name "$1"
    git config user.email "$2"
}

boilcpp(){
	z=$1
	if [[ "$z" = "" ]]
    then
        z="main"
	fi
	if [[ -d "$z" ]]
	then
		echo "a dir with this name exist! try another name or delete it by \"rm -rf $z\" "
		return -1
	fi
    mkdir "$z"
	cd "$z"
    ############################################### DEFAULT CODE
	echo "#include <iostream>"               >> main.cpp 
	echo ""                                  >> main.cpp
	echo "// using namespace std;"           >> main.cpp
	echo ""                                  >> main.cpp
	echo "int main(int argc, char *argv[]){" >> main.cpp
	echo "    std::cout << \"AA is OOF\\n\";"   >> main.cpp
	echo "    return 0;"                     >> main.cpp
	echo "}"                                 >> main.cpp
	###############################################	
}

boilc(){
	z=$1
	if [[ "$z" = "" ]]
    then
        z="main"
	fi
	if [[ -d "$z" ]]
	then
		echo "a dir with this name exist! try another name or delete it by \"rm -rf $z\" "
		return -1
	fi
    mkdir "$z"
	cd "$z"
    ############################################### DEFAULT CODE
	echo "#include <stdio.h>"               >> main.c
	echo ""                                  >> main.c
	echo "int main(int argc, char *argv[]){" >> main.c
	echo "    printf(\"AA is OOF\\n\");"        >> main.c
	echo "    return 0;"                     >> main.c
	echo "}"                                 >> main.c
    ############################################### 
}

runc(){
	z=$1
	if [[ "${z##*.}" = "c" ]]
	then
		z="${z%.*}" 
	fi
	if [[ "$z" = "" ]]
    then
        z="main"
	fi
	rm "$z.o" "$z" > /dev/null 2>&1
   	gcc -std=c2x "$z.c" -o "$z.o" #C flags / Bleeding edge features
   	link "$z.o" "$z"
    chmod +x "$z"
    echo ; echo
    echo "##################### Program Start #####################"
    echo
    ./"$z"
}

runcpp(){
	z=$1
	if [[ "${z##*.}" = "cpp" ]]
	then
		z="${z%.*}" 
	fi
	if [[ "$z" = "" ]]
    then
        z="main"
	fi
	rm "$z.o" "$z" > /dev/null 2>&1
   	g++ -Wno-error -std=c++2a -fconcepts "$z.cpp" -o "$z.o" #C++ flags / Bleeding edge features / take a look at https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html
   	link "$z.o" "$z"
    chmod +x "$z"
    echo ; echo
    echo "##################### Program Start #####################"
    echo
    ./"$z"
}

#FUTURE : Online Update

#####AA Zone#####
'''

print(back+cyan+AsciiArt)
print("A Tiny Script By AARMN The Limitless To Ease Bash With Some Funcs And Aliases\n")

if (platform.system()!="Linux"):
	print("Installer Work Only On Gnu\Linux OS , If You Have Bash Installed In Your OS,  Copy Script Var From Source to Your .bashrc File In Home Folder Of Your OS")
	exit()
if(DetectShell() == '.bashrc'):
	bash=str(subprocess.check_output(["bash","--version"])).find("GNU bash")
	if (bash==-1):
		print("There Is No Bash In Your System PATH , Try to Install Or Reinstall It")
		exit()
else:
	zsh=str(subprocess.check_output(["zsh","--version"])).find("zsh")
	if (zsh==-1):
		print("your default shell is zsh but There Is No zsh In Your System PATH , Try to Install Or Reinstall It")
		exit()
Home=os.path.expanduser("~")

try:
	Shell=open(os.path.join(Home,DetectShell()),"r")
except IOError:
	if(DetectShell() == '.bashrc'):
		ans3=yesno(angryinput("You Don't Have A .bashrc, Can I Create One? (Yes/No)",func=yesno))
	elif(DetectShell() == '.zshrc'):
		ans3=yesno(angryinput("You Don't Have A .zshrc, Can I Create One? (Yes/No)",func=yesno))
	if not (ans3):
            exit()
	Shell=open(os.path.join(Home,DetectShell()),"w+")
	Shell.close()

Shell=open(os.path.join(Home,DetectShell()),"r")
ans=None
BashrcString=Shell.read()
Shell.close()
StartScript=BashrcString.find('#####AA Zone#####\n')
EndScript=BashrcString.find('#####AA Zone#####\n',StartScript+1)
WithoutScript=BashrcString[0:StartScript]+BashrcString[EndScript+17:-1]
InstalledScript=BashrcString[StartScript:EndScript+17]
TagCount=0

def InstallScript():
	try:
		Shell=open(os.path.join(Home,DetectShell()),"a")
	except IOError:
		print("I Think Shell Is Write Protect, Fix It And Run Code Again")
		exit()
	Shell.write(Script)
	Shell.close()

def InstallExtra():
	print(letsinstall)
	if(DetectShell() == '.bashrc'):
		print(omb)
		print(iowt)
		OptionList = ['0','1']
	elif(DetectShell() == '.zshrc'):
		print(omz)
		print(iowt)
		OptionList = ['0','1']
	ExtraTools = int(angryinput(list=OptionList))
	if(DetectShell() == '.bashrc'):
		if(ExtraTools == 1):
			os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"')
	elif(DetectShell() == '.zshrc'):
		if(ExtraTools == 1):
			os.system('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')

def UninstallScript():
	try:
		Shell=open(os.path.join(Home,DetectShell()),"w")
	except IOError:
		print("I Think Shell Is Write Protect, Fix It And Run Code Again")
		exit()
	Shell.write(WithoutScript)
	Shell.close()
def FindVer(start,scriptstr):
	endline="\n"
	ListTmpVer=list()
	step=start+19
	while(scriptstr[step]!=endline):
		ListTmpVer.append(scriptstr[step])
		step+=1
	return int(''.join(ListTmpVer))

Shell=open(os.path.join(Home,DetectShell()),"r")
for line in Shell:
	if (line=="#####AA Zone#####\n"):
		TagCount+=1
Shell.close()

nonew="This Script Don't Have A New Version Of AA"
installthem="To Upgrade Bash to Next Level We Suggest You to Install More Fancy Stuff too \nDo You Want to Install:"
omb="1.Oh My Bash"
bashit="2.Bashit"
omz = "1.Oh My Zsh"
iowt="0.None Of Them, AA is Enough"
donesad="Done :("
donehappy="Done :)"
wisechoice="Wise Choice :)"
letsinstall="AA Is Not Installed Yet, Do You Want to Install? (Yes/No) : "
pbbutinstalled="AA Is Not Installed Successfully (Or You Want to Trick Us ... HAHAHAHA), Do You Want to Install Anyway? (Just Add Commands to End) (Yes/No) : "
cancelit3="3.Cancel"
cancelit2="2.Cancel"
uninstallit="1.Uninstall AA"
newincompatver="Your Version Is Newer And Backward Incompatible Or You Have A Corrupt Version of AA In Your Shell,In This Situation Try Delete It Manually And Have A New Installed"
upgradeit="2.Down/Up-grade AA"
otherver="If You Want to Upgrade Or Find It Useless, This Script Contain a diffrent ver"
olderver="But It's Older :("
newerver="Good News, It's New :)"
resetshell="To Effect Changes You Need To Run A New Bash Or Source Shell, Do You Want To Source Shell? (If You Are Already Running This In Bash Its Recommended) (Yes/No) : "

if (TagCount==0):
	ans=yesno(angryinput(letsinstall,func=yesno))
	if (ans):
		InstallScript()
		ansreset=yesno(angryinput(resetshell,func=yesno))
		if (ansreset):
			ResetShell()
		InstallExtra()
		print(donehappy)
elif (TagCount==1):
	ans=yesno(angryinput(pbbutinstalled,func=yesno))
	if (ans):
		InstallScript()
		ansreset=yesno(angryinput(resetshell,func=yesno))
		if (ansreset):
			ResetShell()
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
				ResetShell()
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
				ResetShell()
			print(donesad)
		if (ans2==2):
			UninstallScript()
			InstallScript()
			ansreset=yesno(angryinput(resetshell,func=yesno))
			if (ansreset):
				ResetShell()
			print(donehappy)
else:
	ans=yesno(angryinput(pbbutinstalled,func=yesno))
	if (ans):
		InstallScript()
		ansreset=yesno(angryinput(resetshell,func=yesno))
		if (ansreset):
			ResetShell()
		print(donehappy)

print(end + "\033[2J" + "\033[1;1H")
cols=shutil.get_terminal_size((80, 20)).columns
print()
print("This project is more about ease and fun, if you like this give us star on gitlab and github, check my other projects, report bugs, pull request new features and so on".center(cols))
print("Wish you bests! Have a good day :)".center(cols))
print()
print()
print()
