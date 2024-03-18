#IMPORT COMMANDS
from tkinter import *
from tkinter import messagebox
import mysql.connector as mc
import pandas as pd
import matplotlib.pyplot as p
from PIL import Image
from PIL import ImageTk

#LOGIN FORM
def Ok():
    uname=e1.get()
    password=e2.get()
    if(uname=="admin" and password=="sejal"):
        messagebox.showinfo("","You\'ve successfully logged in")
        root.destroy()
    elif(uname=="" and password==""):
        messagebox.showinfo("","Blank is not allowed")
    else:
        messagebox.showinfo("","Incorrect Username or Password")
root=Tk()  
root.title("Login Form")
root.geometry('500x500')
global e1
global e2
root.configure(background='HotPink2')
Label(root,text='Username',fg='lavender blush',bg='DarkOrchid2',font=('Times',16,'bold'),textvariable='uname').place(x=50,y=50)
Label(root,text='Password',fg='lavender blush',bg='DarkOrchid2',font=('Times',16,'bold'),textvariable='password').place(x=50,y=100)
uname=StringVar()
password=StringVar()
e1=Entry(root,width=20)
e1.place(x=220,y=50)
e2=Entry(root,width=20)
e2.place(x=220,y=100)
e2.config(show="@")
Button(root,text='LOGIN',fg='goldenrod1',font=('Helvetica',20,'bold',),command=Ok,bg='dark orchid').place(x=200,y=200)
root.mainloop()

#MENU
print("------------------------MENU------------------------")
print("------------------------1)DISPLAY RECORDS-----------")
print("------------------------2)SEARCH RECORDS------------")
print("------------------------3)INSERT RECORDS------------")
print("------------------------4)GRAPHS--------------------")
print("------------------------5)IMAGES--------------------")
print("------------------------6)EXIT----------------------")

#EDITING TABLE
con=mc.connect(host='localhost', user='root', password='sejal')
print("Connection established")
cur=con.cursor()
qr="use sejal"
cur.execute(qr)
choice=int(input('Enter Your Choice: '))

#TO DISPLAY THE RECORDS
if choice==1:
    qr1='SELECT * FROM KINGS'
    cur.execute(qr1)
    for i in cur:
        print(i)
        print('Serial No.',i[0])
        print('Ruler : ',i[1])
        print('Reign : ',i[2])
        print('Age : ',i[3])
        print('Country : ',i[4])
        print('Wives : ',i[5])
        print()


#TO SEARCH THE RECORDS
elif choice==2:
    r=input('Enter any Ruler\'s Name : ')
    qr2="select*from kings where ruler=%s"
    cur.execute(qr2,(r,))
    for i in cur:
        print(i)
        print('Serial No. : ',i[0])
        print('Name of the Ruler : ',i[1])
        print('Reign : ',i[2])
        print('Age : ',i[3])
        print('Country : ',i[4])
        print('Number of Wives(s) : ',i[5])
        print()
        
#TO INSERT THE RECORDS
elif choice==3:
    r1=int(input('Serial No. : '))
    r2=input('Name of the Ruler : ')
    r3=input('Reign : ')
    r4=int(input('Age :   '))
    r5=input('Country : ')
    r6=int(input('Number of Wive(s) : '))
    d='insert into kings(sno ,Ruler, Reign, Age, Country, Wives) values(%s,%s,%s,%s,%s,%s)'
    val=(r1,r2,r3,r4,r5,r6)
    cur.execute(d,val)
    print('Record Inserted')

#INSERTING GRAPHS
elif choice==4:
    print('--------1.LINE GRAPH----------')
    print('--------2.PIE CHART-----------')
    print('--------3.SCATTERED GRAPH-----')
    print('--------4.BAR GRAPH-----------')
    print('--------5.HISTOGRAM-----------')
    X=int(input('Enter Your Choice : '))
    c="select*from kings"
    cur.execute(c)
    df=pd.DataFrame(cur)
    r=df.loc[:,1]
    v=df.loc[:,3]
    w=df.loc[:,5]
    ruler=['Alexander The Great','Julius Caesar','Augustus','Constantine I','Tiberius','Nero','Philip II of Macedon','Ptolemy I Soter','Archelaus I','Demetrius I']
    age=[32,55,75,65,77,30,46,84,39,55,43]

#CREATING LINE GRAPH
    if X==1:
        ax=p.axes()
        ax.set_facecolor('purple')
        p.title("Line Graph",fontsize=30, color='red')      
        p.xlabel("Ruler",fontsize=20, color='indigo')
        p.ylabel("Age",fontsize=20, color='indigo')
        p.plot(r, v, color='violet', marker='*', markersize=20, markerfacecolor='pink')
        p.xticks(rotation=45)
        p.show()
        
#CREATING PIE CHART
    elif X==2:
       p.title("Pie Chart",fontsize=30, color='violet')      
       col=['orange','pink','violet','blue','indigo','green','yellow','red','crimson','purple']
       s=sum(age)
       p.pie(v, labels=r, colors=col, radius=1, autopct=lambda x: '{:.0f}'.format(x*s/100)) 
       p.show()
       
#CREATING SCATTERED GRAPH
    elif X==3:
        p.title("Scattered Graph",fontsize=30, color='violet')              
        ax=p.axes()      
        ax.set_facecolor('pink')      
        p.scatter(v,w,marker='.',color='k', s=200)
        p.xlabel('Age',fontsize=20)
        p.ylabel("Number of Wives", fontsize=20)
        p.show()
        
#CREATING BAR GRAPH
    elif X==4:
        ax=p.axes()
        ax.set_facecolor('indigo')
        p.title("Bar Graph",fontsize=20)
        p.xlabel('Ruler',fontsize=16)
        p.ylabel('Age',fontsize=16)
        p.bar(r,v,width=0.5,color='black',label='Ruler',edgecolor='k',hatch='x')
        p.bar(r,v,width=0.5,color='pink',label='Age',edgecolor='k',hatch='x')
        p.xticks(rotation=45)
        p.yticks(rotation=45)
        p.legend(loc=2)
        p.show()


#CREATING HISTOGRAM
    elif X==5:
        ax=p.axes()
        ax.set_facecolor('blue')
        p.xlabel('Ruler',fontsize=16)
        p.title("Age",fontsize=20,color='green')
        p.hist(v,bins=[10,20,30,40,50,60,70,80,90,100],color='red',edgecolor='k',hatch='o',histtype='stepfilled')
        p.xticks(rotation=45)
        p.yticks(rotation=45)
        p.show()

        
#INSERTING IMAGES
elif choice==5:
    print("-------------------RULERS------------------------------------------")      
    print("-------------------1)Alexander the Great --------------------------")
    print("-------------------2)Julius Caesar --------------------------------")
    print("-------------------3)Augustus (Octavian Caesar) -------------------")
    print("-------------------4)Constantine the Great (Constantine I) --------")
    print("-------------------5)Tiberius -------------------------------------")      
    print("-------------------6)Nero -----------------------------------------")
    print("-------------------7)Philip II of Macedon -------------------------")
    print("-------------------8)Ptolemy I Soter ------------------------------")      
    print("-------------------9)Archelaus I ----------------------------------")
    print("-------------------10)Demetrius I ---------------------------------")    
   
    i=int(input('ENTER YOUR CHOICE  :  '))
    if i==1:
        a_root=Tk()
        image=Image.open(r"C:\Users\sanjeev\Desktop\ip\alexandar.jpg")
        photo=ImageTk.PhotoImage(image)
        img_label=Label(image=photo)
        img_label.pack()
        a_root.mainloop()

    elif i==2:
        a_root=Tk()
        image=Image.open(r"C:\Users\sanjeev\Desktop\ip\Julius Caesar.jpg")
        photo=ImageTk.PhotoImage(image)
        img_label=Label(image=photo)
        img_label.pack()
        a_root.mainloop()
       
    elif i==3:
        a_root=Tk()
        image=Image.open(r"C:\Users\sanjeev\Desktop\ip\Augustus (Octavian Caesar).jpg")
        photo=ImageTk.PhotoImage(image)
        img_label=Label(image=photo)
        img_label.pack()
        a_root.mainloop()
       
    elif i==4:
        a_root=Tk()
        image=Image.open(r"C:\Users\sanjeev\Desktop\ip\Constantine the Great (Constantine I).jpg")
        photo=ImageTk.PhotoImage(image)
        img_label=Label(image=photo)
        img_label.pack()
        a_root.mainloop()
       
    elif i==5:
        a_root=Tk()
        image=Image.open(r"C:\Users\sanjeev\Desktop\ip\Tiberius.jpg")
        photo=ImageTk.PhotoImage(image)
        img_label=Label(image=photo)
        img_label.pack()
        a_root.mainloop()
     
    elif i==6:
        a_root=Tk()
        image=Image.open(r"C:\Users\sanjeev\Desktop\ip\Nero.jpg")
        photo=ImageTk.PhotoImage(image)
        img_label=Label(image=photo)
        img_label.pack()
        a_root.mainloop()
 
    elif i==7:
        a_root=Tk()
        image=Image.open(r"C:\Users\sanjeev\Desktop\ip\Philip II of Macedon.jpg")
        photo=ImageTk.PhotoImage(image)
        img_label=Label(image=photo)
        img_label.pack()
        a_root.mainloop()
 
    elif i==8:
        a_root=Tk()
        image=Image.open(r"C:\Users\sanjeev\Desktop\ip\Ptolemy I Soter.jpg")
        photo=ImageTk.PhotoImage(image)
        img_label=Label(image=photo)
        img_label.pack()
        a_root.mainloop()
         
    elif i==9:
        a_root=Tk()
        image=Image.open(r"C:\Users\sanjeev\Desktop\ip\Archelaus I.jpg")
        photo=ImageTk.PhotoImage(image)
        img_label=Label(image=photo)
        img_label.pack()
        a_root.mainloop()
 
    elif i==10:
        a_root=Tk()
        image=Image.open(r"C:\Users\sanjeev\Desktop\ip\Demetrius I.jpg")
        photo=ImageTk.PhotoImage(image)
        img_label=Label(image=photo)
        img_label.pack()
        a_root.mainloop()

    elif i==11:
        a_root=Tk()
        image=Image.open(r"C:\Users\sanjeev\Desktop\ip\Amyntas II.jpg")
        photo=ImageTk.PhotoImage(image)
        img_label=Label(image=photo)
        img_label.pack()
        a_root.mainloop()
 
else:
  print('EXIT')

con.commit()
con.close()
    




    
