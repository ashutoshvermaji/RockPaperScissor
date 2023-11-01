import random
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import atexit
from PIL import Image,ImageTk



class Rock:
    def __init__(self,root):
        self.root=root
        self.user_input="rock"
        self.rock()
    def rock(self):
        self.root.geometry("600x500+100+100")
        self.root.title("Rock Paper Scissor")
        self.root['background']='white'

        


        # label of you
        title_lbl=Label(self.root,text="Your Input",font=("times new roman",16,"bold"),bg="white",fg='red')
        title_lbl.place(x=40,y=70,width=150 ,height=35)

        # label of computer
        title_lbl3=Label(self.root,text="Computer Input",font=("times new roman",16,"bold"),bg="white",fg='darkblue')
        title_lbl3.place(x=350,y=70,width=200 ,height=35)


        # rock button with image
        strt_btn=Image.open("new/rock.jpg")
        strt_btn=strt_btn.resize((150,90))
        self.photoimg=ImageTk.PhotoImage(strt_btn)

        b1=Label(self.root,image=self.photoimg,cursor="hand2")
        b1.place(x=40,y=150,width=150,height=90)

        b1_1=Button(self.root,text="ROCK",cursor="hand2",font=("times new roman",10),bg="white",fg="darkblue")
        b1_1.place(x=40,y=240,width=150,height=20)


        # versus image
        versus_img=Image.open("new/vs.png")
        versus_img=versus_img.resize((120,120))
        self.photoimg5=ImageTk.PhotoImage(versus_img)
        
        versus_img1=Label(self.root,image=self.photoimg5)
        versus_img1.place(x=220,y=150,width=120,height=120)


        self.com_input=self.loop()








        # it is for computer input option
        if self.com_input=="rock":
            strt_btn1=Image.open("new/rock.jpg")
            strt_btn1=strt_btn1.resize((150,90))
            self.photoimg1=ImageTk.PhotoImage(strt_btn1)

            b11=Label(self.root,image=self.photoimg1,cursor="hand2")
            b11.place(x=370,y=150,width=150,height=90)

            b1_11=Button(self.root,text="ROCK",cursor="hand2",font=("times new roman",10),bg="white",fg="darkblue")
            b1_11.place(x=370,y=240,width=150,height=20)
        elif self.com_input=="paper":
            strt_btn1=Image.open("new/paper.jpg")
            strt_btn1=strt_btn1.resize((150,90))
            self.photoimg1=ImageTk.PhotoImage(strt_btn1)

            b11=Label(self.root,image=self.photoimg1,cursor="hand2")
            b11.place(x=370,y=150,width=150,height=90)

            b1_11=Button(self.root,text="PAPER",cursor="hand2",font=("times new roman",10),bg="white",fg="darkblue")
            b1_11.place(x=370,y=240,width=150,height=20)
        elif self.com_input=="scissor":
            strt_btn1=Image.open("new/scissor.jpg")
            strt_btn1=strt_btn1.resize((150,90))
            self.photoimg1=ImageTk.PhotoImage(strt_btn1)

            b11=Label(self.root,image=self.photoimg1,cursor="hand2")
            b11.place(x=370,y=150,width=150,height=90)

            b1_11=Button(self.root,text="SCISSOR",cursor="hand2",font=("times new roman",10),bg="white",fg="darkblue")
            b1_11.place(x=370,y=240,width=150,height=20)








        


        # # you need to play it again to win?
        # title_lbl23=Label(self.root,text="you need to play it again to win?",font=("times new roman",13,"bold"),bg="white",fg='darkblue')
        # title_lbl23.place(x=10,y=390,width=570 ,height=20)


        # # play again button
        b1_1=Button(self.root,command=self.close_current,text="Play Again",cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=80,y=420,width=150,height=40)

        # # quit button
        b1_1=Button(self.root,command=self.close_all,text="Quit",cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="red")
        b1_1.place(x=350,y=420,width=130,height=40)

    # ==================================================destryod the program=====================================
    # close the current window using play again button
    def close_current(self):
        #self.root.quit()
        self.root.withdraw()
        #exit()
        #self.root.quit()
    
    # close the whole program and quit all the  windows
    def close_all(self):
        self.root.destroy()
        exit()
        #self.root.quit()

    







    def check_winner(self,computer_input):
        if self.user_input==computer_input:
            #print("it's Draw ")
            #print("Please choose again ")
            return "draw"
        else:
            if self.user_input=="rock" and computer_input=="scissor":
                return "you are winner"
            elif self.user_input=="rock" and computer_input=="paper":
                return "computer is winner"
            elif self.user_input=="paper" and computer_input=="rock":
                return "you are winner"
            elif self.user_input=="paper" and computer_input=="scissor":
                return "computer is winner"
            elif self.user_input=="scissor" and computer_input=="rock":
                return "computer is winner"
            elif self.user_input=="scissor" and computer_input=="paper":
                return "you are winner"
    

    def loop(self):
        try:
            choose1=['rock','paper','scissor']
            computer_input=random.choice(choose1)
            #computer_input="paper"
            chk=self.check_winner(computer_input)   # call the function and check winner
            if chk=="draw":
                # you and computer both have entered same input?
                title_lbl23=Label(self.root,text="you and computer both have selected the 'ROCK'?",font=("times new roman",13,"bold"),bg="white",fg='darkblue')
                title_lbl23.place(x=0,y=270,width=400 ,height=20)
                # "IT'S DRAW"
                title_lbl23=Label(self.root,text="IT'S DRAW",font=("times new roman",30,"bold"),bg="white",fg='red')
                title_lbl23.place(x=100,y=320,width=400 ,height=50)
                return computer_input
            
            elif chk=="computer is winner":
                # Paper(computer) wrapped rock(you)
                title_lbl23=Label(self.root,text="Paper   Wrapped  your  Rock?",font=("times new roman",13,"bold"),bg="white",fg='darkblue')
                title_lbl23.place(x=0,y=270,width=400 ,height=20)

                # you are the looser
                title_lbl23=Label(self.root,text="You are the Loser!",font=("times new roman",30,"bold"),bg="white",fg='red')
                title_lbl23.place(x=60,y=320,width=500 ,height=50)

                # congrats image
                strt_btn111=Image.open("new/looser2.jpeg")
                strt_btn111=strt_btn111.resize((100,80))
                self.photoimg111=ImageTk.PhotoImage(strt_btn111)

                b1111=Label(self.root,image=self.photoimg111,cursor="hand2")
                b1111.place(x=20,y=300,width=100,height=80)
                return computer_input

            elif chk=="you are winner":
                # rock(you) crushed scissor(computer)
                title_lbl23=Label(self.root,text="Rock   Crushed   the computer's Scissor",font=("times new roman",13,"bold"),bg="white",fg='darkblue')
                title_lbl23.place(x=0,y=270,width=400 ,height=20)

                # you are the winner
                title_lbl23=Label(self.root,text="Congratulation!! You are the Winner!",font=("times new roman",25,"bold"),bg="white",fg='red')
                title_lbl23.place(x=0,y=320,width=600 ,height=50)

                # congrats image
                strt_btn11=Image.open("new/cong12.jpg")
                strt_btn11=strt_btn11.resize((200,150))
                self.photoimg11=ImageTk.PhotoImage(strt_btn11)

                b111=Label(self.root,image=self.photoimg11,cursor="hand2")
                b111.place(x=170,y=10,width=200,height=150)


                return computer_input

        except Exception as e:
            pass
            # print("something wrong in it ")
            # print("please try again")
            # print(e)

    
    

              
        
if __name__ == "__main__":
    root=Tk()
    obj1=Rock(root)
    root.mainloop()








    

    