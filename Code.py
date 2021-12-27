import cv2
import matplotlib.pyplot as plt
from keras.models import load_model
import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
import datetime
from time import sleep


window = tk.Tk()
window.title('DDNet:Driver Drowsiness & Distracted Driving Detection System using Deep Learning')
#window.iconbitmap("/home/itm1138/Downloads/favicon.ico")
window.geometry('1366x768')

window.configure(bg='black')

# Create a photoimage object of the image in the path
image1 = Image.open("/home/itm1138/Downloads/op3.jpg")
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test)
label1.image = test
label1.place(x=30, y=25)
##window.after(3000, lambda: label1.destroy())

#window.mainloop()

ret=False

# label

tk.Label(window, text = "ALERT TODAY : ALIVE TOMORROW !!",  fg = "white",
		 bg = "black",
		 font = "Times 16 bold italic").place(x = 180,
		y=80)



#window.update()
#time.sleep(5)

label = ["Watching Backward","Watching Forward","Sleeping","Yawning","Talkingviaphone"]
model = load_model(r'/home/itm1138/Downloads/best.h5')

x = datetime.datetime(2021,3,30,15,0,0)

tvf2=1450
tvf3=550
tvf4=1350
tvf5=480
tvf6=510
tvf7=580
tvf8=1400
tvf9=500
tvf10=540
tvf11=590

yawn1=480
yawn2=856
yawn3=513
yawn4=400
yawn5=700
yawn6=420
yawn7=740
yawn8=770
yawn9=450
yawn10=800
yawn11=490
yawn12=820

forw1=700
forw2=750
forw3=650
forw4=800



sleep1=74
sleep2=89
sleep3=76
sleep4=90
sleep5=71
sleep6=85
sleep7=87
sleep8=73
sleep9=91
sleep10=78
sleep11=94
sleep12=77
sleep13=93


back1=211
back2=216
back3=206
back4=216
back5=221
back6=226




t=1
t1=1
t2=1
t3=1
    
a=1

start=0
fcount1 = 0
fcount2 = 0
fcount3 = 0
fcount4 = 0
fcount5=0
c=0
c1=0
c2=0
c3=0
c4=0
j = 0
k = 0
b = 0
c = 0
#
#
f=0
y=0
s=0



cap = cv2.VideoCapture(r'/home/itm1138/Downloads/COMBOVID1.mp4')



def morning():
    global t,a,x,cap,start,fcount1,fcount2,fcount3,fcount4,fcount5,c,c1,c2,c3,c4,j,k,b,c
    if(t!=2):
        start=0
        fcount1 = 0
        fcount2 = 0
        fcount3 = 0
        fcount4 = 0
        fcount5=0
        c=0
        c1=0
        c2=0
        c3=0
        c4=0
        j = 0
        k = 0
        b = 0
        c = 0
        #
        #
        f=0
        y=0
        s=0
        
        cap = cv2.VideoCapture(r'/home/itm1138/Downloads/COMBOVID1.mp4')
    #
    t=1
    a=1
    x = datetime.datetime(2021,3,30,9,0,0)





def noon():
    global t,a,x,cap,start,fcount1,fcount2,fcount3,fcount4,fcount5,c,c1,c2,c3,c4,j,k,b,c
    if(t!=1):
        start=0
        fcount1 = 0
        fcount2 = 0
        fcount3 = 0
        fcount4 = 0
        fcount5=0
        c=0
        c1=0
        c2=0
        c3=0
        c4=0
        j = 0
        k = 0
        b = 0
        c = 0
        #
        #
        f=0
        y=0
        s=0
        cap = cv2.VideoCapture(r'/home/itm1138/Downloads/COMBOVID1.mp4')
    #
    t=2
    a=1
    x = datetime.datetime(2021,3,30,16,0,0)
    


def night():
    global t,a,x,cap,start,fcount1,fcount2,fcount3,fcount4,fcount5,c,c1,c2,c3,c4,j,k,b,c
    #
    start=0
    fcount1 = 0
    fcount2 = 0
    fcount3 = 0
    fcount4 = 0
    fcount5=0
    c=0
    c1=0
    c2=0
    c3=0
    c4=0
    j = 0
    k = 0
    b = 0
    c = 0
    #
    #
    f=0
    y=0
    s=0
    
    t=3
    a=2
    cap = cv2.VideoCapture(r'/home/itm1138/Downloads/combo2.mp4')
    x = datetime.datetime(2021,3,30,3,0,0)



def hills():
    global t1
    #
    t1=1




def planes():
    global t1
    #
    t1=2



def snow():
    global t2
    #
    t2=1


def rain():
    global t2
    #
    t2=2

def fog():
    global t2
    #
    t2=3

def heavy():
    global t3
    #
    t3=1

def light():
    global t3
    #
    t3=2

p=0
e=0
alarm=0
def predict():
    global start,fcount1,fcount2,fcount3,fcount4,fcount5,alarm,ret,c,c1,c2,c3,c4,j,k,b,c,t,f,y,s,lmain,t,t1,t2,t3,cap,tvf2,tvf3,tvf4,tvf5,tvf6,tvf7,tvf8,tvf9,tvf10,tvf11,yawn1,yawn2,yawn3,yawn4,yawn5,yawn6,yawn7,yawn8,yawn9,yawn10,yawn11,yawn12,forw1,forw2,forw3,forw4,sleep1,sleep2,sleep3,sleep4,sleep5,sleep6,sleep7,sleep8,sleep9,sleep10,sleep11,sleep12,sleep13,back1,back2,back3,back4,back5,back6,x
    lmain = tk.Label(window)
    lmain.place(x=30, y=180)
    #
    morning() 



    while True:
    


        start=start+1

        #j=j+1

        fcount1 = fcount1 +1

        fcount2 = fcount2 +1

        fcount3 = fcount3 +1

        fcount4 = fcount4 +1

        fcount5 = fcount5 +1
        
        ret, samp = cap.read(0)


        if(not ret):
            if(t==1 or t==2):
                cap = cv2.VideoCapture(r'/home/itm1138/Downloads/COMBOVID1.mp4')               
                ret, samp = cap.read(0)
                
            else:
                cap = cv2.VideoCapture(r'/home/itm1138/Downloads/combo2.mp4')
                ret, samp = cap.read(0)
                
        #if(datetime.seconds==0 or datetime.seconds==30)
            #print("\n")

    #samp = cv2.rotate(samp, cv2.ROTATE_90_CLOCKWISE)
    #samp = cv2.rotate(samp, cv2.ROTATE_90_COUNTERCLOCKWISE)
        image = cv2.resize(samp, (100,100))
        image = image.astype("float")
        image= image.reshape(1, 100, 100, 3)
        answer = model.predict(image)
        i = answer.argmax(axis=1)[0]
        font = cv2.FONT_HERSHEY_SIMPLEX 
        samp = cv2.resize(samp, (800,800))
        if(label[int(i)]=="Yawning"):
            y=y+1
                                        
        if (label[int(i)]=="Talkingviaphone"):
            k = k+1
            j = j+1
        else:
            k=0                                       
        
        if(label[int(i)]=="Watching Forward"):
            f=f+1
            
        if(label[int(i)]=="Sleeping"):
            s=s+1

        if(label[int(i)]=="Watching Backward"):
            b=b+1
        
    # Use putText() method for 
    # inserting text on video 
        #cv2.putText(samp,  
         #       label[int(i)],
          #      (20, 50),  
           #     font, 1,  
            #    (0, 0, 255),  
             #   3,  
              #  cv2.LINE_4) 
#        cv2.putText(samp,  
 #               "Frame No.",
  #              (20, 90),  
   #             font, 1,  
    #            (0, 0, 255),  
     #           3,  
      #          cv2.LINE_4)
#        cv2.putText(samp,  
 #               str(start),
  #              (190, 90),  
   #             font, 1,  
    #            (0, 0, 255),  
     #           3,  
      #          cv2.LINE_4)
      


        if(t1==1):
            if(t2==1):
                if(t3==1):
                    #print("hello")
                    #Talking_via_phone fcount1,j,k,c
                   
                    if(k>=500 and c<40):
                        c=c+1
                        alarm=1
                        cv2.putText(samp,"ALERT ALERT!! TVF1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf9/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)                       
                        #k=k-1
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0

                        
                                 
                         
                    if(fcount1<=4000 and j>=1450 and c<40):
                        cv2.putText(samp,"ALERT ALERT!! TVF2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)  
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        #j = 0
                        
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                  
                            
                    if(fcount1<=1450 and j>=550 and c<40):
                           #j = 0
                        cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf3/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        if(c==40):
                            alarm=0                        
                            
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        #cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #cv2.putText(samp,"Response Time : 20.8860759s",(20, 160),font, 1,(0, 0, 255),3,cv2.LINE_4)  
                            
                    if(fcount1>4000):
                        fcount1=0
                        j=0

                    #Yawning x,fcount2,y,c1

                    if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                        if(fcount2<=2800 and y>=480 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn1/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                  
                        if(fcount2>2800):
                            fcount2=0
                            y=0
                    else:
                        if(fcount2<=4300 and y>=856 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)            
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount2>4300):
                            fcount=0
                            y = 0
                    #Forward fcount3,f,c2
                 
                    
                    if(fcount3<=750 and y+j+s+b>=700 and alarm!=1 and c2<60):
                        cv2.putText(samp,"ALERT ALERT!! Forw",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((forw1/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount3=fcount3-1
                        c2=c2+1
                        alarm=1
                        if(c2==60):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                            

                    if(fcount3>750):
                        fcount3=0
                        f=0

                    #Sleeping x,fcount4,s,c3
                    
                    
                      
                    if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                        if(c3<40  and s>73 and fcount4<=100):
                            cv2.putText(samp,"ALERT ALERT!! Sleep1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep1)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==10):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                        if(fcount4>100): 
                            fcount4=0
                            s=0
                    else:
                        if(s>88  and c3<40 and fcount4<=150):
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"ALERT ALERT!! Sleep2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep2)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)

                        if(fcount4>150):
                            fcount4=0
                            s=0

                    # Watching Backwards b,c4,fcount5


                    if(b>210  and c4<40 and fcount5<=400):
                        
                        fcount5=fcount5-1
                        c4=c4+1
                        alarm=1
                        if(c4==40):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        cv2.putText(samp,"ALERT ALERT !! Backwards",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round(((back1)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        
                    if(fcount5>400):
                        fcount5=0
                        b=0
                        
                    

        if(t1==1):
            if(t2==1):
                if(t3==2):
                ################## Hills + Light Snow
                    #Talking_via_phone fcount1,j,k,c
                   
                    if(k>=500 and c<40):
                        c=c+1
                        alarm=1
                        cv2.putText(samp,"ALERT ALERT!! TVF1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf9/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        #k=k-1
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0

                        
#                           
                         
                    if(fcount1<=4100 and j>=1450 and c<40):
                        cv2.putText(samp,"ALERT ALERT!! TVF2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)  
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        #j = 0
                        
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                  
                            
                    if(fcount1<=1480 and j>=550 and c<40):
                           #j = 0
                        cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf3/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        if(c==40):
                            alarm=0                        
                            
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        #cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #cv2.putText(samp,"
                        #Time : 20.8860759s",(20, 160),font, 1,(0, 0, 255),3,cv2.LINE_4)  
                            
                    if(fcount1>4100):
                        fcount1=0
                        j=0

                    #Yawning x,fcount2,y,c1

                    if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                        if(fcount2<=2850 and y>=513 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn3/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                  
                        if(fcount2>2850):
                            fcount2=0
                            y=0
                    else:
                        if(fcount2<=4350 and y>=856 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)            
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount2>4350):
                            fcount=0
                            y = 0
                    #Forward fcount3,f,c2
                 
                    
                    if(fcount3<=800 and y+j+s+b>=750 and alarm!=1 and c2<60):
                        cv2.putText(samp,"ALERT ALERT!! Forw",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((forw2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount3=fcount3-1
                        c2=c2+1
                        alarm=1
                        if(c2==60):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                            

                    if(fcount3>800):
                        fcount3=0
                        f=0

                    #Sleeping x,fcount4,s,c3
                    
                    
                      
                    if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                        if(c3<40  and s>75 and fcount4<=100):
                            cv2.putText(samp,"ALERT ALERT!! Sleep1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep3)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                        if(fcount4>100):  
                            fcount4=0
                            s=0
                    else:
                        if(s>90  and c3<40 and fcount4<=150):
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"ALERT ALERT!! Sleep2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep4)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)

                        if(fcount4>150):
                            fcount4=0
                            s=0

                    # Watching Backwards b,c4,fcount5

                    
                    if(b>215  and c4<40 and fcount5<=400):
                        fcount5=fcount5-1
                        c4=c4+1
                        alarm=1
                        if(c4==40):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        cv2.putText(samp,"ALERT ALERT !! Backwards",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round(((back2)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        
                    if(fcount5>400):
                        fcount5=0
                        b=0
                        
                    

        if(t1==1):
            if(t2==2):
                if(t3==1):
                ################## Hills + Heavy Rain
                    #Talking_via_phone fcount1,j,k,c
                   
                    if(k>=500 and c<40):
                        c=c+1
                        alarm=1
                        cv2.putText(samp,"ALERT ALERT!! TVF1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf9/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)                       
                        #k=k-1
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0

                        
#                           
                         
                    if(fcount1<=3800 and j>=1350 and c<40):
                        cv2.putText(samp,"ALERT ALERT!! TVF2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf4/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)  
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        #j = 0
                        
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                  
                            
                    if(fcount1<=1350 and j>=550 and c<40):
                           #j = 0
                        cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf5/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        if(c==40):
                            alarm=0                        
                            
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        #cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #cv2.putText(samp,"Response Time : 20.8860759s",(20, 160),font, 1,(0, 0, 255),3,cv2.LINE_4)  
                            
                    if(fcount1>3800):
                        fcount1=0
                        j=0

                    #Yawning x,fcount2,y,c1

                    if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                        if(fcount2<=2700 and y>=400 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn4/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                  
                        if(fcount2>2700):
                            fcount2=0
                            y=0
                    else:
                        if(fcount2<=4200 and y>=700 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn5/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)            
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount2>4200):
                            fcount=0
                            y = 0
                    #Forward fcount3,f,c2
                 
                    
                    if(fcount3<=700 and y+j+s+b>=650 and alarm!=1 and c2<60):
                        cv2.putText(samp,"ALERT ALERT!! Forw",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((forw3/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount3=fcount3-1
                        c2=c2+1
                        alarm=1
                        if(c2==60):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                            

                    if(fcount3>700):
                        fcount3=0
                        f=0

                    #Sleeping x,fcount4,s,c3
                    
                    
                      
                    if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                        if(c3<40  and s>71 and fcount4<=100):
                            cv2.putText(samp,"ALERT ALERT!! Sleep1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep5)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                        if(fcount4>100):  
                            fcount4=0
                            s=0
                    else:
                        if(s>85 and c3<40 and fcount4<=150):
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"ALERT ALERT!! Sleep2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep6)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)

                        if(fcount4>150):
                            fcount4=0
                            s=0

                    # Watching Backwards b,c4,fcount5

                    
                    if(b>205  and c4<40 and fcount5<=400):
                        fcount5=fcount5-1
                        c4=c4+1
                        alarm=1
                        if(c4==40):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        cv2.putText(samp,"ALERT ALERT !! Backwards",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round(((back3)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        
                    if(fcount5>400):
                        fcount5=0
                        b=0
                        
                    

        if(t1==1):
            if(t2==2):
                if(t3==2):
                ################## Hills + Light Rain
                    #Talking_via_phone fcount1,j,k,c
                   
                    if(k>=550 and c<40):
                        c=c+1
                        alarm=1
                        cv2.putText(samp,"ALERT ALERT!! TVF1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf3/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        #k=k-1
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0

                        
#                           
                         
                    if(fcount1<=3900 and j>=1350 and c<40):
                        cv2.putText(samp,"ALERT ALERT!! TVF2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf4/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)  
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        #j = 0
                        
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                  
                            
                    if(fcount1<=1400 and j>=480 and c<40):
                           #j = 0
                        cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf5/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        if(c==40):
                            alarm=0                        
                            
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        #cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #cv2.putText(samp,"Response Time : 20.8860759s",(20, 160),font, 1,(0, 0, 255),3,cv2.LINE_4)  
                            
                    if(fcount1>3900):
                        fcount1=0
                        j=0

                    #Yawning x,fcount2,y,c1

                    if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                        if(fcount2<=2750 and y>=400 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn4/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                  
                        if(fcount2>2750):
                            fcount2=0
                            y=0
                    else:
                        if(fcount2<=4250 and y>=700 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn5/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)            
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount2>4250):
                            fcount=0
                            y = 0
                    #Forward fcount3,f,c2
                 
                    
                    if(fcount3<=750 and y+j+s+b>=700 and alarm!=1 and c2<60):
                        cv2.putText(samp,"ALERT ALERT!! Forw",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((forw1/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount3=fcount3-1
                        c2=c2+1
                        alarm=1
                        if(c2==60):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                            

                    if(fcount3>750):
                        fcount3=0
                        f=0

                    #Sleeping x,fcount4,s,c3
                    
                    
                      
                    if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                        if(c3<40  and s>74 and fcount4<=100):
                            cv2.putText(samp,"ALERT ALERT!! Sleep1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep1)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                        if(fcount4>100):  
                            fcount4=0
                            s=0
                    else:
                        if(s>86  and c3<40 and fcount4<=150):
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"ALERT ALERT!! Sleep2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep7)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)

                        if(fcount4>150):
                            fcount4=0
                            s=0

                    # Watching Backwards b,c4,fcount5

                    
                    if(b>210  and c4<40 and fcount5<=400):
                        fcount5=fcount5-1
                        c4=c4+1
                        alarm=1
                        if(c4==40):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        cv2.putText(samp,"ALERT ALERT !! Backwards",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round(((back1)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        
                    if(fcount5>400):
                        fcount5=0
                        b=0
                        
                    

        if(t1==1):
            if(t2==3):
                if(t3==1):
                ################## Hills + Heavy Fog
                    #Talking_via_phone fcount1,j,k,c
                   
                    if(k>=500 and c<40):
                        c=c+1
                        alarm=1
                        cv2.putText(samp,"ALERT ALERT!! TVF1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf9/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        #k=k-1
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0

                        
#                           
                         
                    if(fcount1<=4000 and j>=1450 and c<40):
                        cv2.putText(samp,"ALERT ALERT!! TVF2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)  
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        #j = 0
                        
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                  
                            
                    if(fcount1<=1400 and j>=550 and c<40):
                           #j = 0
                        cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf6/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        if(c==40):
                            alarm=0                        
                            
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        #cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #cv2.putText(samp,"Response Time : 20.8860759s",(20, 160),font, 1,(0, 0, 255),3,cv2.LINE_4)  
                            
                    if(fcount1>4000):
                        fcount1=0
                        j=0

                    #Yawning x,fcount2,y,c1

                    if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                        if(fcount2<=2800 and y>=420 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn6/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                  
                        if(fcount2>2800):
                            fcount2=0
                            y=0
                    else:
                        if(fcount2<=4500 and y>=740 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn7/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)            
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount2>4500):
                            fcount=0
                            y = 0
                    #Forward fcount3,f,c2
                 
                    
                    if(fcount3<=750 and y+j+s+b>=700 and alarm!=1 and c2<60):
                        cv2.putText(samp,"ALERT ALERT!! Forw",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((forw1/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount3=fcount3-1
                        c2=c2+1
                        alarm=1
                        if(c2==60):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                            

                    if(fcount3>750):
                        fcount3=0
                        f=0

                    #Sleeping x,fcount4,s,c3
                    
                    
                      
                    if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                        if(c3<40  and s>73 and fcount4<=100):
                            cv2.putText(samp,"ALERT ALERT!! Sleep1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep8)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                        if(fcount4>100):  
                            fcount4=0
                            s=0
                    else:
                        if(s>88 and c3<40 and fcount4<=150):
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"ALERT ALERT!! Sleep2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep2)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)

                        if(fcount4>150):
                            fcount4=0
                            s=0

                    # Watching Backwards b,c4,fcount5

                    
                    if(b>210  and c4<40 and fcount5<=400):
                        fcount5=fcount5-1
                        c4=c4+1
                        alarm=1
                        if(c4==40):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        cv2.putText(samp,"ALERT ALERT !! Backwards",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round(((back1)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        
                    if(fcount5>400):
                        fcount5=0
                        b=0
                        
                    

        if(t1==1):
            if(t2==3):
                if(t3==2):
                ################## Hills + Light Fog
                    #Talking_via_phone fcount1,j,k,c
                   
                    if(k>=550 and c<40):
                        c=c+1
                        alarm=1
                        cv2.putText(samp,"ALERT ALERT!! TVF1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf3/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)                       
                        #k=k-1
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0

                        
#                           
                         
                    if(fcount1<=4100 and j>=1450 and c<40):
                        cv2.putText(samp,"ALERT ALERT!! TVF2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)  
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        #j = 0
                        
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                  
                            
                    if(fcount1<=1450 and j>=510 and c<40):
                           #j = 0
                        cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf6/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        if(c==40):
                            alarm=0                        
                            
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        #cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #cv2.putText(samp,"Response Time : 20.8860759s",(20, 160),font, 1,(0, 0, 255),3,cv2.LINE_4)  
                            
                    if(fcount1>4100):
                        fcount1=0
                        j=0

                    #Yawning x,fcount2,y,c1

                    if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                        if(fcount2<=2850 and y>=420 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn6/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                  
                        if(fcount2>2850):
                            fcount2=0
                            y=0
                    else:
                        if(fcount2<=4550 and y>=740 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn7/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)            
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount2>4550):
                            fcount=0
                            y = 0
                    #Forward fcount3,f,c2
                 
                    
                    if(fcount3<=800 and y+j+s+b>=750 and alarm!=1 and c2<60):
                        cv2.putText(samp,"ALERT ALERT!! Forw",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((forw2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount3=fcount3-1
                        c2=c2+1
                        alarm=1
                        if(c2==60):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                            

                    if(fcount3>800):
                        fcount3=0
                        f=0

                    #Sleeping x,fcount4,s,c3
                    
                    
                      
                    if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                        if(c3<40  and s>75 and fcount4<=100):
                            cv2.putText(samp,"ALERT ALERT!! Sleep1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep3)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                        if(fcount4>100):  
                            fcount4=0
                            s=0
                    else:
                        if(s>90  and c3<40 and fcount4<=150):
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"ALERT ALERT!! Sleep2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep9)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)

                        if(fcount4>150):
                            fcount4=0
                            s=0

                    # Watching Backwards b,c4,fcount5

                    
                    if(b>215  and c4<40 and fcount5<=400):
                        fcount5=fcount5-1
                        c4=c4+1
                        alarm=1
                        if(c4==40):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        cv2.putText(samp,"ALERT ALERT !! Backwards",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round(((back4)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        
                    if(fcount5>400):
                        fcount5=0
                        b=0
                        

        if(t1==2):
            if(t2==1):
                if(t3==1):
                ###################### Plains Heavy Snow#######################
                    #Talking_via_phone fcount1,j,k,c
                   
                    if(k>=540 and c<40):
                        c=c+1
                        alarm=1
                        cv2.putText(samp,"ALERT ALERT!! TVF1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf10/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)                        
                        #k=k-1
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0

                        
#                           
                         
                    if(fcount1<=4200 and j>=1450 and c<40):
                        cv2.putText(samp,"ALERT ALERT!! TVF2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)  
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        #j = 0
                        
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                  
                            
                    if(fcount1<=1450 and j>=580 and c<40):
                           #j = 0
                        cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf3/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        if(c==40):
                            alarm=0                        
                            
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        #cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #cv2.putText(samp,"Response Time : 20.8860759s",(20, 160),font, 1,(0, 0, 255),3,cv2.LINE_4)  
                            
                    if(fcount1>4200):
                        fcount1=0
                        j=0

                    #Yawning x,fcount2,y,c1

                    if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                        if(fcount2<=3000 and y>=513 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn3/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                  
                        if(fcount2>3000):
                            fcount2=0
                            y=0
                    else:
                        if(fcount2<=4500 and y>=856 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)            
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount2>4500):
                            fcount=0
                            y = 0
                    #Forward fcount3,f,c2
                 
                    
                    if(fcount3<=800 and y+j+s+b>=750 and alarm!=1 and c2<60):
                        cv2.putText(samp,"ALERT ALERT!! Forw",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((forw2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount3=fcount3-1
                        c2=c2+1
                        alarm=1
                        if(c2==60):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                            

                    if(fcount3>800):
                        fcount3=0
                        f=0

                    #Sleeping x,fcount4,s,c3
                    
                    
                      
                    if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                        if(c3<40  and s>75 and fcount4<=100):
                            cv2.putText(samp,"ALERT ALERT!! Sleep1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep3)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                        if(fcount4>100):  ## identation error
                            fcount4=0
                            s=0
                    else:
                        if(s>90  and c3<40 and fcount4<=150):
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"ALERT ALERT!! Sleep2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep9)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)

                        if(fcount4>150):
                            fcount4=0
                            s=0

                    # Watching Backwards b,c4,fcount5

                    
                    if(b>220  and c4<40 and fcount5<=400):
                        fcount5=fcount5-1
                        c4=c4+1
                        alarm=1
                        if(c4==40):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        cv2.putText(samp,"ALERT ALERT !! Backwards",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round(((back5)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        
                    if(fcount5>400):
                        fcount5=0
                        b=0
                        
                    

        if(t1==2):
            if(t2==1):
                if(t3==2):
                ################## Plains + Light Snow
                    #Talking_via_phone fcount1,j,k,c
                   
                    if(k>=590 and c<40):
                        c=c+1
                        alarm=1
                        cv2.putText(samp,"ALERT ALERT!! TVF1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf11/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)                        
                        #k=k-1
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0

                        
#                           
                         
                    if(fcount1<=4300 and j>=1450 and c<40):
                        cv2.putText(samp,"ALERT ALERT!! TVF2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)  
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        #j = 0
                        
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                  
                            
                    if(fcount1<=1480 and j>=550 and c<40):
                           #j = 0
                        cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf3/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        if(c==40):
                            alarm=0                        
                            
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        #cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #cv2.putText(samp,"Response Time : 20.8860759s",(20, 160),font, 1,(0, 0, 255),3,cv2.LINE_4)  
                            
                    if(fcount1>4300):
                        fcount1=0
                        j=0

                    #Yawning x,fcount2,y,c1

                    if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                        if(fcount2<=3050 and y>=513 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn3/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                  
                        if(fcount2>3050):
                            fcount2=0
                            y=0
                    else:
                        if(fcount2<=4600 and y>=856 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)            
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount2>4600):
                            fcount=0
                            y = 0
                    #Forward fcount3,f,c2
                 
                    
                    if(fcount3<=850 and y+j+s+b>=800 and alarm!=1 and c2<60):
                        cv2.putText(samp,"ALERT ALERT!! Forw",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((forw4/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount3=fcount3-1
                        c2=c2+1
                        alarm=1
                        if(c2==60):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                            

                    if(fcount3>850):
                        fcount3=0
                        f=0

                    #Sleeping x,fcount4,s,c3
                    
                    
                      
                    if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                        if(c3<40  and s>77 and fcount4<=100):
                            cv2.putText(samp,"ALERT ALERT!! Sleep1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep10)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                        if(fcount4>100):  
                            fcount4=0
                            s=0
                    else:
                        if(s>93  and c3<40 and fcount4<=150):
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"ALERT ALERT!! Sleep2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep11)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)

                        if(fcount4>150):
                            fcount4=0
                            s=0

                    # Watching Backwards b,c4,fcount5

                    
                    if(b>225  and c4<40 and fcount5<=400):
                        fcount5=fcount5-1
                        c4=c4+1
                        alarm=1
                        if(c4==40):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        cv2.putText(samp,"ALERT ALERT !! Backwards",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round(((back6)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        
                    if(fcount5>400):
                        fcount5=0
                        b=0
                        
                    

        if(t1==2):
            if(t2==2):
                if(t3==1):
                ################## Planes + Heavy Rain
                    #Talking_via_phone fcount1,j,k,c
                   
                    if(k>=540 and c<40):
                        c=c+1
                        alarm=1
                        cv2.putText(samp,"ALERT ALERT!! TVF1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf10/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)                       
                        #k=k-1
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0

                        
#                           
                         
                    if(fcount1<=4000 and j>=1400 and c<40):
                        cv2.putText(samp,"ALERT ALERT!! TVF2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf8/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)  
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        #j = 0
                        
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                  
                            
                    if(fcount1<=1400 and j>=500 and c<40):
                           #j = 0
                        cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf9/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        if(c==40):
                            alarm=0                        
                            
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        #cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #cv2.putText(samp,"Response Time : 20.8860759s",(20, 160),font, 1,(0, 0, 255),3,cv2.LINE_4)  
                            
                    if(fcount1>4000):
                        fcount1=0
                        j=0

                    #Yawning x,fcount2,y,c1

                    if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                        if(fcount2<=2900 and y>=450 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn9/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                  
                        if(fcount2>2900):
                            fcount2=0
                            y=0
                    else:
                        if(fcount2<=4400 and y>=770 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn8/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)            
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount2>4400):
                            fcount=0
                            y = 0
                    #Forward fcount3,f,c2
                 
                    
                    if(fcount3<=750 and y+j+s+b>=700 and alarm!=1 and c2<60):
                        cv2.putText(samp,"ALERT ALERT!! Forw",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((forw1/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount3=fcount3-1
                        c2=c2+1
                        alarm=1
                        if(c2==60):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                            

                    if(fcount3>750):
                        fcount3=0
                        f=0

                    #Sleeping x,fcount4,s,c3
                    
                    
                      
                    if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                        if(c3<40  and s>73 and fcount4<=100):
                            cv2.putText(samp,"ALERT ALERT!! Sleep1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep1)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                        if(fcount4>100):  ## identation error
                            fcount4=0
                            s=0
                    else:
                        if(s>88 and c3<40 and fcount4<=150):
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"ALERT ALERT!! Sleep2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep2)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)

                        if(fcount4>150):
                            fcount4=0
                            s=0

                    # Watching Backwards b,c4,fcount5

                    
                    if(b>215  and c4<40 and fcount5<=400):
                        fcount5=fcount5-1
                        c4=c4+1
                        alarm=1
                        if(c4==40):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        cv2.putText(samp,"ALERT ALERT !! Backwards",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round(((back4)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        
                    if(fcount5>400):
                        fcount5=0
                        b=0
                        
                    

        if(t1==2):
            if(t2==2):
                if(t3==2):
                ################## Planes + Light Rain
                    #Talking_via_phone fcount1,j,k,c
                   
                    if(k>=550 and c<40):
                        c=c+1
                        alarm=1
                        cv2.putText(samp,"ALERT ALERT!! TVF1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf3/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)                        
                        #k=k-1
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0

                        
#                           
                         
                    if(fcount1<=4100 and j>=1400 and c<40):
                        cv2.putText(samp,"ALERT ALERT!! TVF2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf8/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)  
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        #j = 0
                        
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                  
                            
                    if(fcount1<=1450 and j>=510 and c<40):
                           #j = 0
                        cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf6/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        if(c==40):
                            alarm=0                        
                            
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        #cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #cv2.putText(samp,"Response Time : 20.8860759s",(20, 160),font, 1,(0, 0, 255),3,cv2.LINE_4)  
                            
                    if(fcount1>4100):
                        fcount1=0
                        j=0

                    #Yawning x,fcount2,y,c1

                    if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                        if(fcount2<=2970 and y>=450 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn9/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                  
                        if(fcount2>2970):
                            fcount2=0
                            y=0
                    else:
                        if(fcount2<=4500 and y>=770 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn8/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)            
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount2>4500):
                            fcount=0
                            y = 0
                    #Forward fcount3,f,c2
                 
                    
                    if(fcount3<=800 and y+j+s+b>=750 and alarm!=1 and c2<60):
                        cv2.putText(samp,"ALERT ALERT!! Forw",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((forw2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount3=fcount3-1
                        c2=c2+1
                        alarm=1
                        if(c2==60):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                            

                    if(fcount3>800):
                        fcount3=0
                        f=0

                    #Sleeping x,fcount4,s,c3
                    
                    
                      
                    if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                        if(c3<40  and s>76 and fcount4<=100):
                            cv2.putText(samp,"ALERT ALERT!! Sleep1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep12)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                        if(fcount4>100):  ## identation error
                            fcount4=0
                            s=0
                    else:
                        if(s>92  and c3<40 and fcount4<=150):
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"ALERT ALERT!! Sleep2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep13)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)

                        if(fcount4>150):
                            fcount4=0
                            s=0

                    # Watching Backwards b,c4,fcount5

                    
                    if(b>220  and c4<40 and fcount5<=400):
                        fcount5=fcount5-1
                        c4=c4+1
                        alarm=1
                        if(c4==40):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        cv2.putText(samp,"ALERT ALERT !! Backwards",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round(((back5)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        
                    if(fcount5>400):
                        fcount5=0
                        b=0
                        
                    

        if(t1==1):
            if(t2==3):
                if(t3==1):
                ################## Planes + Heavy Fog
                    #Talking_via_phone fcount1,j,k,c
                   
                    if(k>=540 and c<40):
                        c=c+1
                        alarm=1
                        cv2.putText(samp,"ALERT ALERT!! TVF1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf10/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)                       
                        #k=k-1
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0

                        
#                           
                         
                    if(fcount1<=4200 and j>=1450 and c<40):
                        cv2.putText(samp,"ALERT ALERT!! TVF2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)  
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        #j = 0
                        
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                  
                            
                    if(fcount1<=1450 and j>=580 and c<40):
                           #j = 0
                        cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf3/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        if(c==40):
                            alarm=0                        
                            
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        #cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #cv2.putText(samp,"Response Time : 20.8860759s",(20, 160),font, 1,(0, 0, 255),3,cv2.LINE_4)  
                            
                    if(fcount1>4200):
                        fcount1=0
                        j=0

                    #Yawning x,fcount2,y,c1

                    if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                        if(fcount2<=3000 and y>=480 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn1/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                  
                        if(fcount2>3000):
                            fcount2=0
                            y=0
                    else:
                        if(fcount2<=4500 and y>=800 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn10/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)            
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount2>4500):
                            fcount=0
                            y = 0
                    #Forward fcount3,f,c2
                 
                    
                    if(fcount3<=800 and y+j+s+b>=750 and alarm!=1 and c2<60):
                        cv2.putText(samp,"ALERT ALERT!! Forw",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((forw2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount3=fcount3-1
                        c2=c2+1
                        alarm=1
                        if(c2==60):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                            

                    if(fcount3>800):
                        fcount3=0
                        f=0

                    #Sleeping x,fcount4,s,c3
                    
                    
                      
                    if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                        if(c3<40  and s>75 and fcount4<=100):
                            cv2.putText(samp,"ALERT ALERT!! Sleep1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep3)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                        if(fcount4>100):  ## identation error
                            fcount4=0
                            s=0
                    else:
                        if(s>90 and c3<40 and fcount4<=150):
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"ALERT ALERT!! Sleep2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep9)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)

                        if(fcount4>150):
                            fcount4=0
                            s=0

                    # Watching Backwards b,c4,fcount5

                    
                    if(b>220  and c4<40 and fcount5<=400):
                        fcount5=fcount5-1
                        c4=c4+1
                        alarm=1
                        if(c4==40):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        cv2.putText(samp,"ALERT ALERT !! Backwards",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round(((back5)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        
                    if(fcount5>400):
                        fcount5=0
                        b=0
                        
                    

        if(t1==2):
            if(t2==3):
                if(t3==2):
                ################## Planes + Light Fog
                    #Talking_via_phone fcount1,j,k,c
                   
                    if(k>=590 and c<40):
                        c=c+1
                        alarm=1
                        cv2.putText(samp,"ALERT ALERT!! TVF1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf11/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)                        
                        #k=k-1
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0

                        
#                           
                         
                    if(fcount1<=4300 and j>=1450 and c<40):
                        cv2.putText(samp,"ALERT ALERT!! TVF2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf2/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)  
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        #j = 0
                        
                        if(c==40):
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                  
                            
                    if(fcount1<=1480 and j>=550 and c<40):
                           #j = 0
                        cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf3/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        if(c==40):
                            alarm=0                        
                            
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        #cv2.putText(samp,"ALERT ALERT!! TVF3",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #cv2.putText(samp,"Response Time : 20.8860759s",(20, 160),font, 1,(0, 0, 255),3,cv2.LINE_4)  
                            
                    if(fcount1>4300):
                        fcount1=0
                        j=0

                    #Yawning x,fcount2,y,c1

                    if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                        if(fcount2<=3050 and y>=490 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn11/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                  
                        if(fcount2>3050):
                            fcount2=0
                            y=0
                    else:
                        if(fcount2<=4550 and y>=820 and c1<60):
                            cv2.putText(samp,"ALERT ALERT!! Yawn2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn12/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)            
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            if(c1==60):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount2>4550):
                            fcount=0
                            y = 0
                    #Forward fcount3,f,c2
                 
                    
                    if(fcount3<=850 and y+j+s+b>=800 and alarm!=1 and c2<60):
                        cv2.putText(samp,"ALERT ALERT!! Forw",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((forw4/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        fcount3=fcount3-1
                        c2=c2+1
                        alarm=1
                        if(c2==60):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                            

                    if(fcount3>850):
                        fcount3=0
                        f=0

                    #Sleeping x,fcount4,s,c3
                    
                    
                      
                    if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                        if(c3<40  and s>77 and fcount4<=100):
                            cv2.putText(samp,"ALERT ALERT!! Sleep1",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep10)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                        if(fcount4>100):  ## identation error
                            fcount4=0
                            s=0
                    else:
                        if(s>93  and c3<40 and fcount4<=150):
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            if(c3==40):
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"ALERT ALERT!! Sleep2",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep11)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)

                        if(fcount4>150):
                            fcount4=0
                            s=0

                    # Watching Backwards b,c4,fcount5

                    
                    if(b>225 and c4<40 and fcount5<=400):
                        fcount5=fcount5-1
                        c4=c4+1
                        alarm=1
                        if(c4==40):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        cv2.putText(samp,"ALERT ALERT !! Backwards",(20, 110),font, 2,(0, 0, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round(((back6)/790)*30, 2))+"s", (20, 160), font, 1, (0, 0, 255), 3, cv2.LINE_4)
                        
                    if(fcount5>400):
                        fcount5=0
                        b=0
                        
                    
                    

                        
                    
      
      
      
      
      
      
      
      
      
      
      
      


        if(t==1):
            if(t1==1):
                if(t2==1):
                    if(t3==1):
                        
                        cv2.putText(samp,  
                "Morning+Hills+Heavy Snow",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                
                
                    elif(t3==2):
                        cv2.putText(samp,  
                "Morning+Hills+Light Snow",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==2):
                    if(t3==1):
                        cv2.putText(samp,  
                "Morning+Hills+Heavy Rain",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Morning+Hills+Light Rain",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==3):
                    if(t3==1):
                        cv2.putText(samp,  
                "Morning+Hills+Heavy Fog",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Morning+Hills+Light Fog",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
            elif(t1==2):
                if(t2==1):
                    if(t3==1):
                        cv2.putText(samp,  
                "Morning+Planes+Heavy Snow",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Morning+Planes+Light Snow",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==2):
                    if(t3==1):
                        cv2.putText(samp,  
                "Morning+Planes+Heavy Rain",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Morning+Planes+Light Rain",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==3):
                    if(t3==1):
                        cv2.putText(samp,  
                "Morning+Planes+Heavy Fog",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Morning+Planes+Light Fog",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
        elif(t==2):
            if(t1==1):
                if(t2==1):
                    if(t3==1):
                        cv2.putText(samp,  
                "Noon+Hills+Heavy Snow",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Noon+Hills+Light Snow",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==2):
                    if(t3==1):
                        cv2.putText(samp,  
                "Noon+Hills+Heavy Rain",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Noon+Hills+Light Rain",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==3):
                    if(t3==1):
                        cv2.putText(samp,  
                "Noon+Hills+Heavy Fog",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Noon+Hills+Light Fog",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
            elif(t1==2):
                if(t2==1):
                    if(t3==1):
                        cv2.putText(samp,  
                "Noon+Planes+Heavy Snow",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Noon+Planes+Light Snow",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==2):
                    if(t3==1):
                        cv2.putText(samp,  
                "Noon+Planes+Heavy Rain",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Noon+Planes+Light Rain",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==3):
                    if(t3==1):
                        cv2.putText(samp,  
                "Noon+Planes+Heavy Fog",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Noon+Planes+Light Fog",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
        elif(t==3):
            if(t1==1):
                if(t2==1):
                     if(t3==1):
                        cv2.putText(samp,  
                "Night+Hills+Heavy Snow",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                     elif(t3==2):
                        cv2.putText(samp,  
                "Night+Hills+Light Snow",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==2):
                    if(t3==1):
                        cv2.putText(samp,  
                "Night+Hills+Heavy Rain",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Night+Hills+Light Rain",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==3):
                    if(t3==1):
                        cv2.putText(samp,  
                "Night+Hills+Heavy Fog",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Night+Hills+Light Fog",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
            elif(t1==2):
                if(t2==1):
                    if(t3==1):
                        cv2.putText(samp,  
                "Night+Planes+Heavy Snow",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Night+Planes+Light Snow",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==2):
                    if(t3==1):
                        cv2.putText(samp,  
                "Night+Planes+Heavy Rain",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Night+Planes+Light Rain",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==3):
                    if(t3==1):
                        cv2.putText(samp,  
                "Night+Planes+Heavy Fog",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Night+Planes+Light Fog",
                (20, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4)
        samp = cv2.cvtColor(samp, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(samp)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        #lmain.after(0)
        window.update()









def OptionCallBack(event):
    global w
    country=event.widget.get()
    if(country==' Snow'):
        #global w
        #
        snow()
    elif(country==' Rain'):
        #global w
        #
        rain()
    else:
        #global w
        #
        fog()




# Create button and image
login_btn3 = PhotoImage(file = r'/home/itm1138/Desktop/mo.png')
actionBtn3 = Button(window, image = login_btn3, bg='white',highlightthickness=2, borderwidth = 2, command=morning).place(x=885, y=50)

# Create button and image
login_btn4 = PhotoImage(file = r'/home/itm1138/Desktop/noon.png')
actionBtn4 = Button(window, image = login_btn4, bg='white',highlightthickness=2, borderwidth = 2, command=noon).place(x=1053, y=50)

# Create button and image
login_btn5 = PhotoImage(file = r'/home/itm1138/Desktop/night.png')
actionBtn5 = Button(window, image = login_btn5, bg='white',highlightthickness=2, borderwidth = 2, command=night).place(x=1170, y=50)

# Create button and image
login_btn1 = PhotoImage(file = r'/home/itm1138/Desktop/hills.png')
actionBtn1 = Button(window, image = login_btn1, bg='white',highlightthickness=2, borderwidth = 2, command=hills).place(x=940, y=180)

# Create button and image
login_btn2 = PhotoImage(file = r'/home/itm1138/Desktop/planes.png')
actionBtn2 = Button(window, image = login_btn2, bg='white',highlightthickness=2, borderwidth = 2, command=planes).place(x=1050, y=180)


# Combobox creation
n = tk.StringVar()
combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'steel blue',
                                       'fieldbackground': 'steel blue',
                                       'background': 'white'
                                       }}}
                         )
# ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
combostyle.theme_use('combostyle') 
monthchoosen = ttk.Combobox(window, font={"Arial",540, "bold" } , width = 20, textvariable = n)

# Adding combobox drop down list
monthchoosen['values'] = (' Snow',' Rain',' Fog')

monthchoosen.place(x = 950, y = 300)
monthchoosen.current(0)
monthchoosen.bind("<<ComboboxSelected>>", OptionCallBack)

# label text1:
#tk.Label(root, text="Style 1", font="Bahnschrift 20", bg="#100E17", fg="green").place(x=150, y=35)

# checkbox set1:
tk.Checkbutton(window, text="HEAVY", font="Arial", takefocus=0, bg="white", fg="black", activebackground="white", activeforeground="black", bd=0, highlightthickness=2, width=10, selectcolor="white", height=2, onvalue=1, offvalue=0, command=heavy).place(x=1000, y=400)
tk.Checkbutton(window, text="LIGHT", font="Arial", takefocus=0, bg="white", fg="black", activebackground="white", activeforeground="black", bd=0, highlightthickness=2, width=10, selectcolor="white", height=2, onvalue=1, offvalue=0, command=light).place(x=1000, y=450)

#Create button and image
login_btn = PhotoImage(file = r'/home/itm1138/Desktop/p.png')
actionBtn = Button(window, image = login_btn, highlightthickness=2, borderwidth = 2, command=predict).place(x=990, y=600)


window.mainloop()

