#Program Name: print_me_first
#Program Description:
#   This is a program to return student info, the lab name, and the current time
#
#   This program will return the name of the student, the lab name, and the time
#@Author : Zhenyu Jiang
#@Date: 11/12/2022
#

def printinfo():
    from datetime import datetime
   
    name = "CNET-142 - Zhenyu Jiang"
    currentTime = datetime.now()
    time = currentTime.strftime("%b-%d-%Y %a (%I:%M:%S%p)")
    myword = name+'\n'+time
    return myword
