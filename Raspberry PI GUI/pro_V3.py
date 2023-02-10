import pygame
import mysql.connector
from tkinter import *
from PIL import ImageTk, Image  #pip install pillow
import hashlib
import random
import serial
from time import sleep



# hosT="127.0.0.1"
# porT=3306
# useR="root"
# passWD=""
# databasE="my_project"

hosT=""
porT=
useR=""
passWD=""
databasE=""

connection = mysql.connector.connect(host=hosT,
                             port=porT,
                             user=useR,
                             passwd=passWD,
                             database=databasE)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (217, 217, 217)
BLUE2 = (215, 213, 255)


pygame.init()
dis = pygame.display.set_mode((1024, 600))

width = 1024
height = 600

pygame.display.update()
pygame.display.set_caption('The machine Purchase of recycled plastic bottles sorted by AI system')
imp = pygame.image.load('/home/pi/Desktop/Project/T1.png')
dis.blit(imp, (0, 0))
font1 = pygame.font.SysFont(None, 100)
font2 = pygame.font.SysFont(None, 120)
font3 = pygame.font.SysFont(None, 40)

A = 0
USer = ''
size = 'k'
Po = 0          #แต้มกระป๋อง
PP = 0          #แต้มสะสม
TP = 0          #total points
EP = 0
SST = 0


pygame.display.flip()

z = 0
x = 0

count = 0

phone_N = ''
passworD = ''
namE = ''
mycursor = connection.cursor()

####################### หน้าต่าง Register
def registration():
    global root2
    root2 = Tk()
    root2.title("Register")
    root2.geometry("1020x575")
    Label(root2, text="Register", fg="red", font=("bold", 36)).pack()
    Label(root2, text="").pack()
    Label(root2, text="คุณสามารถลงทะเบียนได้ ผ่านแอพพลิเคชั่นไลน์", fg="blue", font=("bold", 18)).pack()
    Label(root2, text="Register in the LINE application. ", fg="blue", font=("bold", 18)).pack()
    load = Image.open("/home/pi/Desktop/Project/QR_Line.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(root2, image=render)
    img.image = render
    img.place(x=300, y=160)
    root2.after(10000, lambda: root2.destroy())

####################### แลกเปลี่ยน 
def exchange():
    mycursor = connection.cursor()
    #phone_N = '0933368624'
    sql = "SELECT * FROM project WHERE phone_number = %s "
    mycursor.execute(sql, (str(phone_N),))
    myresult = mycursor.fetchall()
    print("Exchange Points")
    print(myresult)
    global phone
    global nam
    global point
    global point_P
    global passworD
    global EP


    if myresult:
        for i in myresult:
            phone = i[2]
            nam = i[1]
            point = i[6]
            point_P = i[5]
            passworD = i[3]
            print("point")
            print(phone)
            print(nam)
            print(point)
            print(point_P)
            print(passworD)

    EP = point
    exchange_P()

def exchange_P():
    print (EP)
    global root3
    root3 = Tk()
    root3.title("Exchange Points")
    root3.geometry("1020x575")
    Label(root3, text="Exchange Points", fg="red", font=("bold", 36)).pack()
    Label(root3, text="").pack()
    Label(root3, text="ID        =   " + phone, fg="blue", font=("bold", 28)).place(x=100, y=80)
    Label(root3, text="Name  =   " + nam, fg="blue", font=("bold", 28)).place(x=100, y=120)
    Label(root3, text="Point", fg="blue", font=("bold", 18)).place(x=650, y=80)
    Label(root3, text=str(point), fg="red", font=("bold", 72)).place(x=740, y=65)
    Label(root3, text="Exchange rate       100 Point   =   1 Baht ", fg="red", font=("bold", 22)).place(x=100, y=180)

    Button(root3, text="+", font=("bold", 20), bg="grey", width=5, command=lambda: on_click1()).place(x=600, y=380)
    Button(root3, text="-", font=("bold", 20), bg="grey", width=5, command=lambda: on_click2()).place(x=710, y=380)
   # Button(root3, text="-1", font=("bold", 20), bg="grey", width=5, command=lambda: on_click(-1)).place(x=600, y=380)
   # Button(root3, text="-10", font=("bold", 20), bg="grey", width=5, command=lambda: on_click(-10)).place(x=700, y=380)


    Label(root3, text="Exchange  ", fg="red", font=("bold", 22)).place(x=100, y=270)
    Label(root3, text=str(point), fg="red", font=("bold", 60)).place(x=300, y=250)
    Label(root3, text=" = ", fg="red", font=("bold", 22)).place(x=500, y=270)
    Label(root3, text=str(count), fg="red", font=("bold", 60)).place(x=600, y=250)

    Button(root3, text="Confirm", font=("bold", 25), bg="red", width=10, command=lambda: exchange_Confirm()).place(x=200, y=450)
    Button(root3, text="Cancel", font=("bold", 25), bg="red", width=10, command=lambda: exchange_OUT()).place(x=600, y=450)

    def on_click1():
        print("EP2")
        global count
        count += 100
        if count > 1000:
            count = 1000
        print(count)
        Label(root3, text="                       1", fg="red", font=("bold", 60)).place(x=600, y=250)
        Label(root3, text=str(count), fg="red", font=("bold", 60)).place(x=600, y=250)

    def on_click2():
        print("EP3")
        global count
        count -= 100
        if count < 0:
            count = 0
        print(count)
        Label(root3, text="                       1", fg="red", font=("bold", 60)).place(x=600, y=250)
        Label(root3, text=str(count), fg="red", font=("bold", 60)).place(x=600, y=250)

    def exchange_Confirm():
        global count
        global point
        print("count")
        print(count)
        if count > point:
            count = 0
            Label(root3, text="point ของคุณไม่เพียงพอ", fg="red", font=("bold", 36)).place(x=100, y=350)
            root3.after(3000, lambda: root3.destroy())
        else:
            point -= count
            print('exchange_Confirm')
            print(phone)
            print(nam)
            print(point)
            print(point_P)
            print(passworD)
            Label(root3, text="แลก point สำเร็จ", fg="red", font=("bold", 36)).place(x=100, y=350)
            
            ser = serial.Serial ("/dev/ttyAMA0", 9600,timeout=0.1)
            if count == 100:
                ser.write(b"1")
                print("exchange = 100 point")
            if count == 200:
                ser.write(b"2")
                print("1")
            if count == 300:
                ser.write(b"3")
            if count == 400:
                ser.write(b"4")
            if count == 500:
                ser.write(b"5")
            if count == 600:
                ser.write(b"6")
            if count == 700:
                ser.write(b"7")
            if count == 800:
                ser.write(b"8")
            if count == 900:
                ser.write(b"9")
            if count == 1000:
                ser.write(b"0")
            
            count = 0      
            root3.after(1000, lambda: root3.destroy())
            ww()

    def exchange_OUT():
        global count
        root3.after(100, lambda: root3.destroy())
        count = 0
#END###################### แลกเปลี่ยน 
        
def ww():
    mycursor = connection.cursor()
    global num
    print("ww")
    print(phone)
    print(nam)
    print(point)
    print(point_P)
    print(passworD)
    num = random.randrange(0, 10000, 3)
    print(num)
    sql = "UPDATE project SET points = %s , passPoints = %s WHERE phone_number = %s && password = %s"
    val = ((str(point)), (str(num)), (str(phone_N)), (str(passworD)))
    mycursor.execute(sql, val)
    connection.commit()
    print(point)
    print(mycursor.rowcount, "record(s) affected")

####################### login
def Cancel_destroy():
    root.after(100, lambda: root.destroy())

def login_varify():
    
    global phone_N
    global passworD
    global namE
    user_varify = username_varify.get()
    pas_varify = password_varify.get()

    sql = "select * from project where phone_number = %s and password = %s "
    mycursor.execute(sql,[(user_varify),(pas_varify)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            phone_N = i[2]
            passworD = i[3]
            namE = i[1]
            print("Var")
            print(phone_N)
            print(passworD)
            print(namE)
            root.after(10, lambda: root.destroy())

            break
    else:
        global fail
        fail = Toplevel(root)
        fail.title("Login Failed")
        fail.geometry("500x250")
        Label(fail, text="login Failed", fg="red", font=("bold", 36)).pack()
        Label(fail, text="").pack()
        Label(fail, text="").pack()
        Label(fail, text="Please check the accuracy again", fg="blue", font=("bold", 18)).pack()
        Label(fail, text="Ro Register in the LINE application.", fg="blue", font=("bold", 18)).pack()
        root.after(1500, lambda: fail.destroy())
        root.after(1800, lambda: root.destroy())



#หน้าล็อกอิน
def main_screen():
    
    global root
    root = Tk()
    root.title("Login or Register")
    root.geometry("1020x575")
    global username_varify
    global password_varify
    Label(root, text="Log-In Portal", bg="grey", fg="black", font="bold", width=300).pack()
    username_varify = StringVar()
    password_varify = StringVar()
    Label(root, text="").pack()
    Label(root, text="Username", font=("bold",25)).pack()
    Entry(root, textvariable=username_varify,font=("bold",25)).pack()
    Label(root, text="").pack()
    Label(root, text="Password", font=("bold",25)).pack()
    Entry(root, textvariable=password_varify,font=("bold",25), show="*").pack()
    Label(root, text="").pack()
    Button(root, text="Login",font=("bold",25), bg="red", width=20, command=login_varify).pack()
    Label(root, text="").pack()
    Button(root, text="Cancel", font=("bold", 25), bg="red", width=20, command=Cancel_destroy).pack()
    Label(root, text="").pack()
    root.after(40000, lambda: root.destroy())


ser = serial.Serial ("/dev/ttyAMA0", 9600,timeout=0.1)

status = True
while (status):
    
    if (SST == 0):
        received_data = ser.readline().hex()         #read serial port
        print (received_data)
        print("AA")
        if received_data == '53':
            size = 'S'
            SST = 1
            print("S")
        elif received_data == '4d':
            size = 'M'
            SST = 1
            print("M")
        elif  received_data == '4c':
            size = 'L'
            SST = 1
            print("L")

#END###################### login


#ชื่อผู้ใช้

    img11 = font3.render('ID : ', True, BLUE)
    dis.blit(img11, (50, 110))
    img12 = font3.render('Name : ', True, BLUE)
    dis.blit(img12, (300, 110))
    pygame.draw.rect(dis, BLUE2, pygame.Rect(105, 110, 180, 30))
    img13 = font3.render(str(phone_N), True, BLUE)
    dis.blit(img13, (110, 110))
    pygame.draw.rect(dis, BLUE2, pygame.Rect(395, 110, 320, 30))
    img13 = font3.render(str(namE), True, BLUE)
    dis.blit(img13, (400, 110))



# แต้มคงเหลือ
    if(phone_N!=''):
        mycursor = connection.cursor()
        sql = "SELECT * FROM project WHERE phone_number = %s "
        mycursor.execute(sql, (str(phone_N),))
        myresult = mycursor.fetchall()
        print(myresult)
        for row in myresult:
            TP = row[6]
            print(TP)
        pygame.draw.rect(dis, GRAY, pygame.Rect(770, 390, 230, 90))
        img3 = font2.render(str(TP), True, BLUE)
        if TP >= 1000:
            dis.blit(img3, (780, 400))
        elif TP >= 100:
            dis.blit(img3, (810, 400))
        elif TP >= 10:
            dis.blit(img3, (840, 400))
        else:
            dis.blit(img3, (860, 400))
        pygame.display.flip()
    else:
        pygame.draw.rect(dis, GRAY, pygame.Rect(770, 390, 230, 90))
        img3 = font2.render('0', True, BLUE)
        dis.blit(img3, (860, 400))

# ไซต์ขวด
    pygame.draw.rect(dis, GRAY, pygame.Rect(570, 245, 100, 80))
    if size == 'S':
        img1 = font1.render('S', True, BLUE)
        dis.blit(img1, (580, 245))
    elif size == 'M':
        img1 = font1.render('M', True, BLUE)
        dis.blit(img1, (580, 245))
    elif size == 'L':
        img1 = font1.render('L', True, BLUE)
        dis.blit(img1, (580, 245))
    elif size == '':
        img1 = font1.render('   ', True, BLUE)
        dis.blit(img1, (580, 245))


# แต้มขวด
    pygame.draw.rect(dis, GRAY, pygame.Rect(570, 400, 100, 80))
    if size == 'S':
        Po = 2
        img1 = font1.render(str(Po), True, BLUE)
        dis.blit(img1, (580, 410))
    elif size == 'M':
        Po = 4
        img1 = font1.render(str(Po), True, BLUE)
        dis.blit(img1, (580, 410))
    elif size == 'L':
        Po = 6
        img1 = font1.render(str(Po), True, BLUE)
        dis.blit(img1, (580, 410))
    elif size == '':
        img1 = font1.render('  ', True, BLUE)
        dis.blit(img1, (580, 410))


# แต้มสะสม
    pygame.draw.rect(dis, GRAY, pygame.Rect(800, 230, 180, 80))
    img2 = font2.render(str(PP), True, BLUE)
    if PP >= 100:
        dis.blit(img2, (810, 230))
    elif PP >= 10:
        dis.blit(img2, (830, 230))
    else :
        dis.blit(img2, (860, 230))


# เช็คการกด
    mouse = pygame.mouse.get_pos()
    for i in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if i.type == pygame.QUIT:
            status = False

# กดปุ่ม CENCEL
        if i.type == pygame.MOUSEBUTTONDOWN:
            if 280 <= mouse[0] <= 280 + 185 and 505 <= mouse[1] <= 505 + 80:
                PP = 0
                SST = 0
                
                phone_N = ''
                passworD = ''
                namE = ''
                
                size = ''
                ser.write(b"E")
                
                

# กดปุ่ม NEXT
        if i.type == pygame.MOUSEBUTTONDOWN:
            if 510 <= mouse[0] <= 510 + 185 and 505 <= mouse[1] <= 505 + 80:
                if size == 'S':
                    PP += 2
                    
                elif size == 'M':
                    PP += 4
            
                elif size == 'L':
                    PP += 6
                    
                ser.write(b"O")
                size = ''
                SST = 0
            


# กดปุ่ม แลก
        if i.type == pygame.MOUSEBUTTONDOWN:
            if 790 <= mouse[0] <= 790 + 185 and 505 <= mouse[1] <= 505 + 80:
                if phone_N != '':
                    exchange()
                    root3.mainloop()



# กดปุ่ม Login
        if i.type == pygame.MOUSEBUTTONDOWN:
            if 770 <= mouse[0] <= 770 + 230 and 15 <= mouse[1] <= 15 + 60:

                connection = mysql.connector.connect(host=hosT,
                             port=porT,
                             user=useR,
                             passwd=passWD,
                             database=databasE)
                mycursor = connection.cursor()
                
                main_screen()
                root.mainloop()

                #A, B, C = login_varify()
                # print("BBBBB")
                print(phone_N)
                # phone_N = A
                print(passworD)
                # passworD = B
                print(namE)
                # namE = C
                # PP=0




# กดปุ่ม Register
        if i.type == pygame.MOUSEBUTTONDOWN:
            if 770 <= mouse[0] <= 770 + 230 and 85 <= mouse[1] <= 85 + 60:
                registration()
                root2.mainloop()

# กดปุ่ม FINISH
        if i.type == pygame.MOUSEBUTTONDOWN:
            if 50 <= mouse[0] <= 50 + 185 and 505 <= mouse[1] <= 505 + 80:
                sql = "SELECT * FROM project WHERE phone_number = %s "
                mycursor.execute(sql, (str(phone_N),))
                myresult = mycursor.fetchall()
                print(myresult)
                for row in myresult:
                    x = row[6]
                    print(row[6])
                z = PP + x
                num = random.randrange(0, 10000, 3)
                print(num)
                sql = "UPDATE project SET points = %s , passPoints = %s WHERE phone_number = %s && password = %s"
                val = ((str(z)), (str(num)), (str(phone_N)), (str(passworD)))
                mycursor.execute(sql, val)
                connection.commit()
                print(z)
                print(mycursor.rowcount, "record(s) affected")
                PP=0
                phone_N = ''
                passworD = ''
                namE = ''
                SST = 0



    #pygame.draw.rect(dis, BLUE, [770, 15, 230, 60])
    #pygame.draw.rect(dis, BLUE, [770, 85, 230, 60])

    pygame.display.flip()
    #pygame.display.update()
pygame.quit()
quit()

