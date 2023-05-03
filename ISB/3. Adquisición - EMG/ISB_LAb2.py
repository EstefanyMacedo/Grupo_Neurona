import serial
import os
import time

t_mode= ""
training_time = 8 # tiempo de record
mode = 2

def Set_Training_Mode():
    global training_time #current_time
    global t_mode
    flag = True
    while(flag):
        print("""Select a training mode
        0. Exit
        1. 5 sec
        2. 10 sec
        3. 15 sec
        4. 20 sec""")
        t_mode = input("Training mode: ")
        if t_mode== "0":   
            exit()
        elif t_mode == "1":
            training_time = 5
            flag = False
        elif t_mode == "2":
            training_time = 10
            flag = False
        elif t_mode == "3":
            training_time = 15
            flag = False
        elif t_mode == "4":
            training_time = 20
            flag = False
        else:
            print("----please insert a valid option----")


def CreateFile():
    global exm
    codPac= "0001"
    rep = 0
    file_direc = codPac
    if not (os.path.exists(file_direc)):
        os.mkdir(file_direc)
    while(True):
        direct = file_direc+"/"+file_direc+"_"+t_mode+"_"+str(rep)+".csv"
        if(os.path.exists(direct)):
            rep+=1
        else:
            exm = open(direct,"x")
            break


def Record_Data(serialport):
    #current_time = time.time()- time_inc (restando practicamente lo mismo)
    current_time=0
    while(training_time>=current_time):
        current_time = time.time()- time_inc
        raw_data = str(serialport.readline())
        exm.write(raw_data +"\n")
    if (current_time>=training_time):
        exm.close()
        serialport.close()
        exit()

        
if __name__ =="__main__":
    Serialport = serial.Serial(port="COM9", baudrate=9600, timeout=1 )
    print(f"Serial connected to {Serialport.name}")
    Set_Training_Mode()
    CreateFile()

    input("----------- Press enter to star recording--------")
    time_inc=time.time() 
    Record_Data(Serialport)
        
