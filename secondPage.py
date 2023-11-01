from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from rock import Rock
from paper import Paper
from scissor import Scissor
import random



class SecondPage:
    def __init__(self,root):
        
        self.root=root
        self._secondpage()
    def _secondpage(self):
        self.root.geometry("600x500+100+100")
        self.root.title("Rock Paper Scissor")
        self.root['background']='white'

        # bg Image label
        # img=Image.open("new/bg2.jpg")
        # img=img.resize((600,500))
        # self.photoimg=ImageTk.PhotoImage(img)
        
        # bg_img=Label(self.root,image=self.photoimg)
        # bg_img.place(x=0,y=0,width=600,height=500)

        #text = Text(bg_img,width=50, height=20)  
        #text.insert(INSERT, "Name.....")
        #text.pack() 

        # it's time to play a game
        title_lbl23=Label(self.root,text="it's time to play a game?",font=("times new roman",13,"bold"),bg="white",fg='darkblue')
        title_lbl23.place(x=0,y=10,width=200 ,height=20)
    
        # label of Information
        title_lbl23=Label(self.root,text="you need to select only one among these three below",font=("times new roman",13,"bold"),bg="white",fg='darkblue')
        title_lbl23.place(x=0,y=30,width=400 ,height=20)


        # label of you
        title_lbl=Label(self.root,text="YOU",font=("times new roman",20,"bold"),bg="white",fg='red')
        title_lbl.place(x=50,y=70,width=150 ,height=35)

        

        # it's your turn
        title_lbl23=Label(self.root,text="it's your turn to choose........",font=("times new roman",13,"bold"),bg="white",fg='darkblue')
        title_lbl23.place(x=0,y=110,width=210 ,height=20)

        # label of you
        #title_lbl2=Label(self.root,text="now It's your turn",font=("times new roman",13,"bold"),fg='red')
        #title_lbl2.place(x=50,y=100,width=150 ,height=20)


        # label of computer
        title_lbl3=Label(self.root,text="COMPUTER",font=("times new roman",20,"bold"),bg="white",fg='#856ff8')
        title_lbl3.place(x=370,y=70,width=170 ,height=35)

        # label of computer
        #title_lbl4=Label(self.root,text="it's computer turn",font=("times new roman",13,"bold"),fg='#856ff8')
        #title_lbl4.place(x=400,y=100,width=150 ,height=20)


        # rock button with image
        strt_btn=Image.open("new/rock.jpg")
        strt_btn=strt_btn.resize((90,50))
        self.photoimg1=ImageTk.PhotoImage(strt_btn)

        b1=Button(self.root,command=self.rock1,image=self.photoimg1,cursor="hand2")
        b1.place(x=110,y=150,width=90,height=50)

        b1_1=Button(self.root,command=self.rock1,text="ROCK",cursor="hand2",font=("times new roman",10),bg="white",fg="green")
        b1_1.place(x=110,y=200,width=90,height=20)



        # paper button with image
        strt_btn2=Image.open("new/paper.jpg")
        strt_btn2=strt_btn2.resize((90,50))
        self.photoimg2=ImageTk.PhotoImage(strt_btn2)

        b11=Button(self.root,command=self.paper1,image=self.photoimg2,cursor="hand2")
        b11.place(x=40,y=230,width=90,height=50)

        b1_11=Button(self.root,command=self.paper1,text="PAPER",cursor="hand2",font=("times new roman",10),bg="white",fg="green")
        b1_11.place(x=40,y=280,width=90,height=20)


        # scissor button with image
        strt_btn3=Image.open("new/scissor.jpg")
        strt_btn3=strt_btn3.resize((90,50))
        self.photoimg3=ImageTk.PhotoImage(strt_btn3)

        b12=Button(self.root,command=self.scissor1,image=self.photoimg3,cursor="hand2")
        b12.place(x=110,y=310,width=90,height=50)

        b1_12=Button(self.root,command=self.scissor1,text="SCISSOR",cursor="hand2",font=("times new roman",10),bg="white",fg="green")
        b1_12.place(x=110,y=360,width=90,height=20)



        # versus image
        versus_img=Image.open("new/vs.png")
        versus_img=versus_img.resize((120,120))
        self.photoimg5=ImageTk.PhotoImage(versus_img)
        
        versus_img1=Label(self.root,image=self.photoimg5)
        versus_img1.place(x=220,y=200,width=120,height=120)



        # computer rock paper scissor images
        computer_img=Image.open("new/com.jpg")
        computer_img=computer_img.resize((170,200))
        self.photoimg6=ImageTk.PhotoImage(computer_img)
        
        computer_img1=Label(self.root,image=self.photoimg6,bg="white")
        computer_img1.place(x=370,y=150,width=170,height=200)

        # # # play again button
        # b1_1=Button(self.root,command=self.close_current,text="Play Again",cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="darkblue")
        # b1_1.place(x=80,y=420,width=150,height=40)

        # # quit button
        b1_1=Button(self.root,command=self.close_all,text="Quit",cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="red")
        b1_1.place(x=200,y=420,width=130,height=40)

    # close the whole program and quit all the  windows
    def close_all(self):
        self.root.destroy()
        exit()
        #self.root.quit()

    #============================= rock page calling function =============================================
    def rock1(self):
        self.new_window=Toplevel(self.root)
        self.app=Rock(self.new_window)



    #============================= paper page calling function =============================================
    def paper1(self):
        self.new_window=Toplevel(self.root)
        self.app=Paper(self.new_window)

    
    #============================= scissor page calling function =============================================
    def scissor1(self):
        self.new_window=Toplevel(self.root)
        self.app=Scissor(self.new_window)




if __name__ == "__main__":
    root=Tk()
    obj1=SecondPage(root)
    #obj1._secondpage()
    root.mainloop()
    
