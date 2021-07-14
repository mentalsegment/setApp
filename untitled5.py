import tkinter as tk
import tkinter.font as tkFont

class App:
    def GButton_351_command(self):
        file1 = open('x1.txt', 'r' ,encoding="utf8")
        Lines = file1.readlines()
 
        count = 0
# Strips the newline character
        for line in Lines:
            count += 1
            self.GListBox_288.insert(0, line)
            print("Line{}: {}".format(count, line.strip()))
    
    def __init__(self, root):
        #setting title
        

    
root.title("Tolkido")
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
        GListBox_288["justify"] = "center"
        GListBox_288.place(x=190,y=0,width=450,height=500)

        GButton_351=tk.Button(root)
        GButton_351["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_351["font"] = ft
        GButton_351["fg"] = "#000000"
        GButton_351["justify"] = "center"
        GButton_351["text"] = "Button"
        GButton_351.place(x=350,y=600,width=70,height=25)
        GButton_351["command"] = self.GButton_351_command

        GButton_806=tk.Button(root)
        GButton_806["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_806["font"] = ft
        GButton_806["fg"] = "#000000"
        GButton_806["justify"] = "center"
        GButton_806["text"] = "Yaz"
        GButton_806.place(x=560,y=600,width=70,height=25)
        GButton_806["command"] = self.GButton_806_command

        GCheckBox_693=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_693["font"] = ft
        GCheckBox_693["fg"] = "#333333"
        GCheckBox_693["justify"] = "center"
        GCheckBox_693["text"] = "X1 - Öğrenme Kartları"
        GCheckBox_693.place(x=10,y=90,width=159,height=30)
        GCheckBox_693["offvalue"] = "0"
        GCheckBox_693["onvalue"] = "1"
        GCheckBox_693["command"] = self.GCheckBox_693_command

        GCheckBox_153=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_153["font"] = ft
        GCheckBox_153["fg"] = "#333333"
        GCheckBox_153["justify"] = "center"
        GCheckBox_153["text"] = "X2 - Soru Kartı"
        GCheckBox_153.place(x=10,y=130,width=121,height=30)
        GCheckBox_153["offvalue"] = "0"
        GCheckBox_153["onvalue"] = "1"
        GCheckBox_153["command"] = self.GCheckBox_153_command

        GCheckBox_941=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_941["font"] = ft
        GCheckBox_941["fg"] = "#333333"
        GCheckBox_941["justify"] = "center"
        GCheckBox_941["text"] = "X3 - Boş Kart/Etiket"
        GCheckBox_941.place(x=20,y=170,width=128,height=30)
        GCheckBox_941["offvalue"] = "0"
        GCheckBox_941["onvalue"] = "1"
        GCheckBox_941["command"] = self.GCheckBox_941_command

        GCheckBox_836=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_836["font"] = ft
        GCheckBox_836["fg"] = "#333333"
        GCheckBox_836["justify"] = "center"
        GCheckBox_836["text"] = "X5 - Memory Game"
        GCheckBox_836.place(x=20,y=210,width=128,height=30)
        GCheckBox_836["offvalue"] = "0"
        GCheckBox_836["onvalue"] = "1"
        GCheckBox_836["command"] = self.GCheckBox_836_command

        GCheckBox_847=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_847["font"] = ft
        GCheckBox_847["fg"] = "#333333"
        GCheckBox_847["justify"] = "center"
        GCheckBox_847["text"] = "X6 - Kutuda Ne Var?"
        GCheckBox_847.place(x=20,y=250,width=132,height=30)
        GCheckBox_847["offvalue"] = "0"
        GCheckBox_847["onvalue"] = "1"
        GCheckBox_847["command"] = self.GCheckBox_847_command

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
        GCheckBox_455["command"] = self.GCheckBox_455_command

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
        GCheckBox_247["command"] = self.GCheckBox_247_command

        GCheckBox_42=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_42["font"] = ft
        GCheckBox_42["fg"] = "#333333"
        GCheckBox_42["justify"] = "center"
        GCheckBox_42["text"] = "Etiket Modu"
        GCheckBox_42.place(x=0,y=450,width=130,height=30)
        GCheckBox_42["offvalue"] = "0"
        GCheckBox_42["onvalue"] = "1"
        GCheckBox_42["command"] = self.GCheckBox_42_command

        GMessage_347=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_347["font"] = ft
        GMessage_347["fg"] = "#333333"
        GMessage_347["justify"] = "center"
        GMessage_347["text"] = "Sistem Hazır"
        GMessage_347.place(x=10,y=520,width=140,height=91)

        GButton_749=tk.Button(root)
        GButton_749["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_749["font"] = ft
        GButton_749["fg"] = "#000000"
        GButton_749["justify"] = "center"
        GButton_749["text"] = "-"
        GButton_749.place(x=190,y=620,width=70,height=25)
        GButton_749["command"] = self.GButton_749_command

        GButton_148=tk.Button(root)
        GButton_148["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_148["font"] = ft
        GButton_148["fg"] = "#000000"
        GButton_148["justify"] = "center"
        GButton_148["text"] = "+"
        GButton_148.place(x=190,y=590,width=70,height=25)
        GButton_148["command"] = self.GButton_148_command

        GLabel_87=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_87["font"] = ft
        GLabel_87["fg"] = "#333333"
        GLabel_87["justify"] = "center"
        GLabel_87["text"] = "Motor Hızı"
        GLabel_87.place(x=190,y=560,width=70,height=25)        

    def GButton_806_command(self):
        print("command")


    def GCheckBox_693_command(self):
        print("command")


    def GCheckBox_153_command(self):
        print("command")


    def GCheckBox_941_command(self):
        print("command")


    def GCheckBox_836_command(self):
        print("command")


    def GCheckBox_847_command(self):
        print("command")


    def GCheckBox_455_command(self):
        print("command")


    def GCheckBox_247_command(self):
        print("command")


    def GCheckBox_42_command(self):
        print("command")


    def GButton_749_command(self):
        print("command")


    def GButton_148_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
