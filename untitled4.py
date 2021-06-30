import tkinter as tk
import tkinter.font as tkFont
import threading
import time
import signal
import RPi.GPIO as GPIO
from pirc522 import RFID
from sys import getsizeof
import sys
Card_Detect_Sensor1 = 7
Error_Detector_Sensor = 11
yazAdedi = 0
isSuccess = 0
nazarFlag = 0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Card_Detect_Sensor1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(Error_Detector_Sensor, GPIO.IN, pull_up_down = GPIO.PUD_UP)
rdr = RFID()
util = rdr.util()
# Set util debug to true - it will print what's going on
util.debug = True
liste = [None]*66
start = 1
flag = 0
x = 0x00
y = 0x00
z = 0x00
q = 0x00
class BackgroundTasks(threading.Thread):
    def run(self,*args,**kwargs):
        global yazAdedi
        global flag
        global isSuccess
        print("Yazma islemi ", yazAdedi, " adet icin basliyor:")
         
        while yazAdedi > 0:
           # print("Kalan: ", yazAdedi)
            while GPIO.input(Card_Detect_Sensor1) == 1:
                print("Kart Tespit Edildi!")
                a = Hata_kontrol()
                a.start()
                flag = 1
                isSuccess = NFC_write_command()
                
                print("durum:", isSuccess)
                if isSuccess :
                    
                    yazAdedi= yazAdedi - 1
                    print("BackBasari", yazAdedi)
                    time.sleep(0.1)
                    while GPIO.input(Card_Detect_Sensor1) == 1:
                        pass
                        flag=0    
 
            
class Hata_kontrol(threading.Thread):
    def run(self,*args,**kwargs):
        hata_sayac = 0
        global flag
        global nazarFlag
        global isSuccess
        while True:
            while GPIO.input(Error_Detector_Sensor) == 1:
                if flag==1 or nazarFlag:
                    if isSuccess:
                     
                        print("yihhuuuu")
                        isSuccess = 0
                        nazarFlag =0
                        flag = 0
                         
                        
                        break
                    else:
                        print("abboooww")
                        nazarFlag =1
                        flag = 0
                        time.sleep(0.7)
                        break 
                 
                 
                 
                 
             
            time.sleep(0.5)
           




def NFC_write_command():
   
    sendArray = liste[:]
    rdr.wait_for_tag()
    print("geldi")
    # Request tag
    (error, data) = rdr.request()
    if not error:
        print("\nDetected")

        (error, uid) = rdr.anticoll()
        if not error:
            # Print UID
            print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
            util.set_tag(uid)
            util.auth(rdr.auth_b, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
            # Print contents of block 4 in format "S1B0: [contents in decimal]". RFID.card_auth() will be called now
           # util.read_out(4)
            #util.read_out(5)
            #util.deauth()
            
           
            
            sendArray[0] = x                  
            sendArray[1] = y
            sendArray[2] = z
            sendArray[3] = q
            print(x)
            print (sendArray)
            util.auth(rdr.auth_a, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
           # util.do_auth(util.block_addr(1, 1))
            util.rewrite(4, [sendArray[0], sendArray[1], sendArray[2], sendArray[3], sendArray[4], sendArray[5],
                          sendArray[6], sendArray[7], sendArray[8], sendArray[9], sendArray[10], sendArray[11],
                          sendArray[1], sendArray[13], sendArray[14], sendArray[15]])

            util.rewrite(5, [sendArray[16], sendArray[17], sendArray[18], sendArray[19], sendArray[20], sendArray[21],
                         sendArray[22], sendArray[23], sendArray[24], sendArray[25], sendArray[26], sendArray[27],
                          sendArray[28], sendArray[29], sendArray[30], sendArray[31]])
           
            controlRead = str(rdr.read(4))
            
            b = controlRead.split(",")
            readCheck = len(b)
            print("check" , readCheck)
            if readCheck == 17:
                print("lastCheck OK")
            else:
                print("HATA1")
                return 0
            #print("0:" ,b[0] , "1:", b[1] , "2:", int(b[2]), "3:", b[3] ,"4:", b[4])
            controlSayac = 2
            okSayac = 0
            while controlSayac < 10:
                if int(sendArray[controlSayac-1]) == int(b[controlSayac]):
                    okSayac +=1
                #print("sen array : " , sendArray[controlSayac-1],"b : ",b[controlSayac])
                
                    #print("hebele")
                
                controlSayac  +=1
            if okSayac ==8:
                print("yazma ok")
                return 1
            
            print(okSayac)

def yaz_command():
  
    global yazAdedi
    yazAdedi= int(GLineEdit_815.get())
    print(yazAdedi)
    for i in GListBox_288.curselection():
        
        can = GListBox_288.get(i)
        printSelected(can)
        t = BackgroundTasks()
        t.start()
       
    
def printSelected(selectedItem):
    secili = selectedItem
    print(secili)
    a = secili.split(",")
    byreArray = [None]*66
    sayac = 4
    for i  in range(1, len(a)):
        zz = a[i]
        b =int(zz)

        a_bytes_big = b.to_bytes(2, 'big')
        # print(a_bytes_big[0])
        #print(a_bytes_big[1])
        byreArray[sayac] = a_bytes_big[0]
        byreArray[sayac+1] = a_bytes_big[1]
   
        sayac = sayac + 2

    global liste
    liste = byreArray[:]
    #NFC_write_command()

def selectBox_x1_command():
    global x
    x = 0x01
    GListBox_288.delete(0,tk.END)
    
    file1 = open('x1.txt', 'r' ,encoding="utf8")
    Lines = file1.readlines()
 
    count = 0
# Strips the newline character
    for line in Lines:
        count += 1
        GListBox_288.insert(0, line)
        print("Line{}: {}".format(count, line.strip()))


def selectBox_x2_command():
    GListBox_288.delete(0,tk.END)
    
    global x
    x = 0x02
    
    file1 = open('x2.txt', 'r' ,encoding="utf8")
    Lines = file1.readlines()
 
    count = 0
# Strips the newline character
    for line in Lines:
        count += 1
        GListBox_288.insert(0, line)
        print("Line{}: {}".format(count, line.strip()))

def selectBox_x3_command():
    print("command")


def selectBox_x5_command():
    GListBox_288.delete(0,tk.END)
    
    file1 = open('x5.txt', 'r' ,encoding="utf8")
    Lines = file1.readlines()
 
    count = 0
# Strips the newline character
    for line in Lines:
        count += 1
        GListBox_288.insert(0, line)
        print("Line{}: {}".format(count, line.strip()))       


def selectBox_x6_command():
    GListBox_288.delete(0,tk.END)
    
    file1 = open('x6.txt', 'r' ,encoding="utf8")
    Lines = file1.readlines()
 
    count = 0
# Strips the newline character
    for line in Lines:
        count += 1
        GListBox_288.insert(0, line)
        print("Line{}: {}".format(count, line.strip()))       



def GCheckBox_455_command():
        print("command")


def kart_modu_command():
        print("command")


def GCheckBox_42_command():
        print("command")

def etiket_modu_command():
        print("command")
        
        
def hiz_dusur():
    pass
    


def GButton_148_command():
        print("command")
        
        
root = tk.Tk()
        #setting title
root.title("Tolkido 15 Temmuz Demokrasi Uygulaması")
        #setting window size
width=687
height=657
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
GListBox_288=tk.Listbox(root)
GListBox_288["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GListBox_288["font"] = ft
GListBox_288["fg"] = "#333333"
GListBox_288["justify"] = "left"
GListBox_288.place(x=190,y=0,width=450,height=500)        
        


GButton_351=tk.Button(root)
GButton_351["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_351["font"] = ft
GButton_351["fg"] = "#000000"
GButton_351["justify"] = "center"
GButton_351["text"] = "Button"
GButton_351.place(x=350,y=600,width=70,height=25)
GButton_351["command"] =   NFC_write_command 

GButton_806=tk.Button(root)
GButton_806["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_806["fg"] = "#000000"
GButton_806["justify"] = "center"
GButton_806["text"] = "Yaz"
GButton_806.place(x=560,y=600,width=70,height=25)
GButton_806["command"] =  yaz_command

selectBox_x1=tk.Checkbutton(root)
ft = tkFont.Font(family='Times',size=10)
selectBox_x1["font"] = ft
selectBox_x1["fg"] = "#333333"
selectBox_x1["justify"] = "center"
selectBox_x1["text"] = "X1 - Öğrenme Kartları"
selectBox_x1.place(x=10,y=90,width=159,height=30)
selectBox_x1["offvalue"] = "0"
selectBox_x1["onvalue"] = "1"
selectBox_x1["command"] =  selectBox_x1_command

GCheckBox_153=tk.Checkbutton(root)
ft = tkFont.Font(family='Times',size=10)
GCheckBox_153["font"] = ft
GCheckBox_153["fg"] = "#333333"
GCheckBox_153["justify"] = "center"
GCheckBox_153["text"] = "X2 - Soru Kartı"
GCheckBox_153.place(x=10,y=130,width=121,height=30)
GCheckBox_153["offvalue"] = "0"
GCheckBox_153["onvalue"] = "1"
GCheckBox_153["command"] =  selectBox_x2_command

GCheckBox_941=tk.Checkbutton(root)
ft = tkFont.Font(family='Times',size=10)
GCheckBox_941["font"] = ft
GCheckBox_941["fg"] = "#333333"
GCheckBox_941["justify"] = "center"
GCheckBox_941["text"] = "X3 - Boş Kart/Etiket"
GCheckBox_941.place(x=20,y=170,width=128,height=30)
GCheckBox_941["offvalue"] = "0"
GCheckBox_941["onvalue"] = "1"
GCheckBox_941["command"] = selectBox_x3_command

GCheckBox_836=tk.Checkbutton(root)
ft = tkFont.Font(family='Times',size=10)
GCheckBox_836["font"] = ft
GCheckBox_836["fg"] = "#333333"
GCheckBox_836["justify"] = "center"
GCheckBox_836["text"] = "X5 - Memory Game"
GCheckBox_836.place(x=20,y=210,width=128,height=30)
GCheckBox_836["offvalue"] = "0"
GCheckBox_836["onvalue"] = "1"
GCheckBox_836["command"] = selectBox_x5_command

GCheckBox_847=tk.Checkbutton(root)
ft = tkFont.Font(family='Times',size=10)
GCheckBox_847["font"] = ft
GCheckBox_847["fg"] = "#333333"
GCheckBox_847["justify"] = "center"
GCheckBox_847["text"] = "X6 - Kutuda Ne Var?"
GCheckBox_847.place(x=20,y=250,width=132,height=30)
GCheckBox_847["offvalue"] = "0"
GCheckBox_847["onvalue"] = "1"
GCheckBox_847["command"] = selectBox_x6_command

GLineEdit_815=tk.Entry(root)
GLineEdit_815["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_815["font"] = ft
GLineEdit_815["fg"] = "#333333"
GLineEdit_815["justify"] = "center"
GLineEdit_815["text"] = "Adet"
GLineEdit_815.place(x=560,y=550,width=70,height=25)

GCheckBox_455=tk.Checkbutton(root)
ft = tkFont.Font(family='Times',size=10)
GCheckBox_455["font"] = ft
GCheckBox_455["fg"] = "#333333"
GCheckBox_455["justify"] = "center"
GCheckBox_455["text"] = "X7 - Joker"
GCheckBox_455.place(x=10,y=290,width=99,height=30)
GCheckBox_455["offvalue"] = "0"
GCheckBox_455["onvalue"] = "1"
GCheckBox_455["command"] = GCheckBox_455_command

GLineEdit_520=tk.Entry(root)
GLineEdit_520["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_520["font"] = ft
GLineEdit_520["fg"] = "#333333"
GLineEdit_520["justify"] = "center"
GLineEdit_520["text"] = "Y"
GLineEdit_520.place(x=180,y=510,width=70,height=25)

GLineEdit_714=tk.Entry(root)
GLineEdit_714["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_714["font"] = ft
GLineEdit_714["fg"] = "#333333"
GLineEdit_714["justify"] = "center"
GLineEdit_714["text"] = "Z"
GLineEdit_714.place(x=260,y=510,width=70,height=25)

GLineEdit_174=tk.Entry(root)
GLineEdit_174["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_174["font"] = ft
GLineEdit_174["fg"] = "#333333"
GLineEdit_174["justify"] = "center"
GLineEdit_174["text"] = "Q"
GLineEdit_174.place(x=340,y=510,width=70,height=25)

GCheckBox_247=tk.Checkbutton(root)
ft = tkFont.Font(family='Times',size=10)
GCheckBox_247["font"] = ft
GCheckBox_247["fg"] = "#333333"
GCheckBox_247["justify"] = "center"
GCheckBox_247["text"] = "Kart Modu"
GCheckBox_247.place(x=20,y=420,width=86,height=30)
GCheckBox_247["offvalue"] = "0"
GCheckBox_247["onvalue"] = "1"
GCheckBox_247["command"] = kart_modu_command

GCheckBox_42=tk.Checkbutton(root)
ft = tkFont.Font(family='Times',size=10)
GCheckBox_42["font"] = ft
GCheckBox_42["fg"] = "#333333"
GCheckBox_42["justify"] = "center"
GCheckBox_42["text"] = "Etiket Modu"
GCheckBox_42.place(x=0,y=450,width=130,height=30)
GCheckBox_42["offvalue"] = "0"
GCheckBox_42["onvalue"] = "1"
GCheckBox_42["command"] = etiket_modu_command

GMessage_347=tk.Message(root)
ft = tkFont.Font(family='Times',size=10)
GMessage_347["font"] = ft
GMessage_347["fg"] = "#333333"
GMessage_347["justify"] = "center"
GMessage_347["text"] = "Sistem Hazır"
GMessage_347.place(x=10,y=520,width=140,height=91)

button_hiz_dusur=tk.Button(root)
button_hiz_dusur["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
button_hiz_dusur["font"] = ft
button_hiz_dusur["fg"] = "#000000"
button_hiz_dusur["justify"] = "center"
button_hiz_dusur["text"] = "-"
button_hiz_dusur.place(x=190,y=620,width=70,height=25)
button_hiz_dusur["command"] = hiz_dusur

GButton_148=tk.Button(root)
GButton_148["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_148["font"] = ft
GButton_148["fg"] = "#000000"
GButton_148["justify"] = "center"
GButton_148["text"] = "+"
GButton_148.place(x=190,y=590,width=70,height=25)
GButton_148["command"] = GButton_148_command

GLabel_87=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_87["font"] = ft
GLabel_87["fg"] = "#333333"
GLabel_87["justify"] = "center"
GLabel_87["text"] = "Motor Hızı"
GLabel_87.place(x=190,y=560,width=70,height=25)


        
        
root.mainloop()


