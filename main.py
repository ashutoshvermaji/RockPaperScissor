from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import atexit
from PIL import Image,ImageTk
from secondPage import SecondPage



class Rock_Paper_scissor:
    def __init__(self,root):
        self.root=root
        self.root.geometry("600x500+100+100")
        self.root.title("Rock Paper Scissor")

        # bg Image
        img=Image.open("new/bg.png")
        img=img.resize((600,500))
        self.photoimg=ImageTk.PhotoImage(img)
        
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=600,height=500)

        # text label
        title_lbl=Label(bg_img,text="you can start playing by clicking on 'play' button",font=("times new roman",13),fg="darkblue")
        title_lbl.place(x=0,y=0,width=350 ,height=25)

        # Play button with image
        #strt_btn=Image.open(r"C:\Users\H.P\Desktop\rockPaperScissor\new\rockpaper.jpg")
        #strt_btn=strt_btn.resize((150,150))
        #self.photoimg1=ImageTk.PhotoImage(strt_btn)

        #b1=Button(bg_img,image=self.photoimg1,cursor="hand2")
        #b1.place(x=150,y=50,width=150,height=150)

         # # play again button
        b1_1=Button(self.root,command=self.second,text="Play",cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=20,y=420,width=130,height=40)

        # # quit button
        b1_1=Button(self.root,command=self.close_all,text="Quit",cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="red")
        b1_1.place(x=200,y=420,width=130,height=40)



    # close the whole program and quit all the  windows
    def close_all(self):
        #messagebox.askyesno("Application","Got it?")
        self.root.destroy()
        exit()
        #self.root.quit()

    # # close the whole program and quit all the  windows
    # def close_all(self):
    #     result=messagebox.askquestion("Quit all windows","do you want to exit")
    #     if result=="yes":
    #         self.root.destroy()
    #         exit()
    #     else:
    #         return None
    #     #self.root.quit()

#============================= second page calling function =============================================
    def second(self):
        self.new_window=Toplevel(self.root)
        self.app=SecondPage(self.new_window)

        

        
        
if __name__ == "__main__":
    root=Tk()
    obj1=Rock_Paper_scissor(root)
    root.mainloop()
