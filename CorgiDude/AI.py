import sensor, image, lcd, time
import KPU as kpu
from machine import UART
from board import board_info
from fpioa_manager import fm

#######################################เรียกใช้กล้อง
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
#sensor.set_windowing((224, 224))
sensor.set_vflip(1)

#######################################เรียกใช้จอ 
lcd.init()
lcd.rotation(2)

#######################################กำหนดขา เชื่อมต่อข้อมูลกับ ESP32
fm.register(18, fm.fpioa.UART1_TX, force=True)
fm.register(19, fm.fpioa.UART1_RX, force=True)
uart_A = UART(UART.UART1, 9600, 8, 1, 0, timeout=1, read_buf_len=4096)


labels=['level1','level2','level3','level4']            #คราสทั้งหมดที่ได้เทรนมา
task = kpu.load(0x300000)                               #เรียกใช้โมเดล AI 
kpu.set_outputs(task, 0, 1, 1, 4)                       #the actual shape needs to match the last layer shape of your model
while(True):
    #kpu.memtest()

    img = sensor.snapshot()                             #อ่านรูปภาพจากกล้อง 
    #img = image.Image("/sd/42.jpg")

    ##############################################################################################สร้างกรอบดำ
    img=img.draw_rectangle((0, 0, 130, 240), color = (0, 0, 0), thickness = 1, fill = True)
    img=img.draw_rectangle((193, 0,360, 240), color = (0, 0, 0), thickness = 1, fill = True)

    img = img.resize(224,224)                          #ประขนาดรูปภาพ

    lcd.display(img)
    #img = img.rotation_corr(z_rotation=90.0) uncomment if need rotation correction - only present in full maixpy firmware
    
    ############################################################################################### เปลียบเทียบรูปภาพที่เข้ามากับ ข้อมูงจาก โมเดล AI
    a = img.pix_to_ai()
    fmap = kpu.forward(task, img)
    plist=fmap[:]
    pmax=max(plist)
    max_index=plist.index(pmax)
    a = img.draw_string(0,0, str(labels[max_index].strip()), color=(255,0,0), scale=2)
    a = img.draw_string(0,20, str(pmax), color=(255,0,0), scale=2)
    print((pmax, labels[max_index].strip()))
    a = lcd.display(img)
    AA = (labels[max_index].strip())

    ############################################### pmax = %ความถูกต้อง , labels[max_index].strip() = ข้อมูลที่มันทายผลออกมา

    ############################################### ตรวจสอบ % ความถูกต้องก่อนส่งข้อมูล ไปยัง ESP32
    if pmax > 0.9:
        if AA == 'level1':
            print("level = 1")
            uart_A.write(b'S')
            time.sleep(3)
        elif AA == 'level2':
            print("level = 2")
            uart_A.write(b'M')
            time.sleep(3)
        elif AA == 'level3':
            print("level = 3")
            uart_A.write(b'L')
            time.sleep(3)
        elif AA == 'level4':
            print("level = 4")
            uart_A.write(b'N')
            time.sleep(1)

    time.sleep(5)

