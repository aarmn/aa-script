
# AA-Script

<div align="center"><img src="https://raw.githubusercontent.com/aarmn/aa-script/master/AA-Script512.png" alt="AA-Script-Logo" /></div>

[![made-with-bash](https://img.shields.io/badge/Made%20with-Bash-1f425f.svg)](https://www.gnu.org/software/bash/)

## What?

A Tiny Script by "AARMN The Limitless" to ease bash with some funcs and aliases.

## How To Install?

### Fast way:

 **1. By wget**
 
    python3 -c "$(wget https://raw.githubusercontent.com/aarmn/aa-script/master/aa.py -O -)"

 **2. By cURL**

    python3 -c "$(curl -fsSL https://raw.githubusercontent.com/aarmn/aa-script/master/aa.py)" 

### Slow way:

 **1. Clone it All!**

    git clone https://github.com/aarmn/aa-script.git
    cd aa-script
    python3 aa.py

## Philosophy

1. Just usefull ones based on my opinion, not a bruteforce for all possible switches to alias, so it won't satisfy everyone but only some, but atleast help those effectivly! (Others can edit! it's MIT and the code is as simple as a code can get)

2. "Complex" and "Repetitve" ones only, life is short, we should optimize it, obey this can make it easier to learn and easier to code


3. One file, No dependency (a bigger version with lack of this but more features will come in sometime)

4. Robust, Try to decrese chance of overlap with installed packages commands, while there is no guarantee over this (Report in case you saw any major program is conflicting with our commands)

5. Keep names short and meaningful

  

## For Who?

1. "Linux Experts" whom are sick and tired of retyping switches and multiple commands in a row and also feel lazy to make their version of this

2. anyone who use Bash, Git and Linux alot

3. anyone who wants to get into reading bashscript, this code is FOR SURE NOT best exercise for these langs (reading some python lines made me feel a weird cringe actually and I'm sure my BashScript gonna have worth story if i dive deeper in that technology) but a cool one to check, with a "Real Production" approach 

  

## License

MIT Public License

  

## Contribute

**How? :**

- With Your Coding Power

- With Your Money (ETH:0xef9e0697af2b4b9b85eda19159ce98150cb05ff7)

- With Your Ideas for new commands (btw before this, read philosophy section carefully)

- With Finding Overlaps with other packages and programs cli commands (if its a major one, i try to change it asap, or put a notice here)

- With Reporting A Escapee Bug

- With A Thanks

- Make A Site, Wikia, Fandom, Ad, Story in Instagram, or any other way to inform other people to use it, I like these mortal, ifuns

  

**Ways to give me code :**

- Pull request (https://gitlab.com/aarmn/aa-script)

- Email me your code or idea aarmn80@gmail.com (Not Recommended)

- send it to me in Telegram @limitless_aarmn

  

## Guide

Because we have a few commands there is no need for a readthedocs

A: What you need to type before

B: What you type with AA

  
**mkcdir**

A:

    mkdir example
    cd example

B:

    mkcdir example

**rmx**

A:

    rm -rf example

B:

    rmx example # With No Parameter Delete everything in Dir

**rmhere**

A:

    cd ..
    rm -r example

B:

    rmhere

**fexe**

A:

    chmod +x example
    ./example

B:

    fexe example

**giton**

A:

    git init .
    touch README.md
    touch LICENSE
    touch .gitignore
    git add *
    git add .gitignore
    git commit -m "Your Initial Commit Message Example"

B:

    giton "Your Initial Commit Message Example" #By Default Set to "Initial Commit"
    
**gitup**

A:

    git add .
    git commit -m "example" 

B:

    gitup "example" #Default to ask user for commit message like "git commit"

**lsx**

A:

    ls -ltrhAis --author --color=auto --hyperlink=always

B:

    lsx

**gitconfg**

A:

    git config --global user.name "example name"
    git config --global user.email "example email"

B:

    gitconfg "example name" "example email"

  

**gitconf**

A:

    git config user.name "example name"
    git config user.email "example email"

B:

    gitconf "example name" "example email"

  

**KILLME**

A:

    sudo rm -rf /

B:

    KILLME



**runc**

A:

   	gcc example.c -o example.o
   	link example.o example
    chmod +x example
    ./example

B:

    runc example.c (even with example it would work and as default it work run main.c)



**runcpp**

A:

   	g++ -Wno-error -fconcepts-ts example.cpp -o example.o
   	link example.o example
    chmod +x example
    ./example

B:

    runcpp example.cpp (even with example it would work and as default it work run main.cpp)



**boilc**

A:

    mkdir example
    cd example
    # make a main.c file with a basic hello world program in example folder (with printf)

B:

    boilc example



**boilcpp**

A:

    mkdir example
    cd example
    # make a main.cpp file with a basic hello world program in example folder (with cout)

B:

    boilcpp example



**myip**

A:

    ip address # or `ifconfig` and looking up and down for public ip and yet not being 100% sure, or googling for ip, or running `curl ifconfig.co` and similar stuff, which is what we do.

B:

    myip

 

## Soon

- add to all users mode

- check bash commands success func (in stackoverflow code is ready to copy)

- ask to install bashit and oh-my-bash as a suggest

- color problem in some terminals and commands

- system unused packages cleaner

- root installation and sudo dep situations

- port for all *nix systems

- online update

- better update system and ver check (say same version)

- manual installation mode

- auto reset all terms with source .bashrc

- add badage
