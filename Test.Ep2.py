import turtle
tao = turtle.Pen() #ดึงความสามารถการใช้ปากกา
tao.shape('turtle') #แปลงรางเป็นเต่า
def Siri():
    '''ฟังชั่นนี้เอาไว้วาดรูป'''
for i in range(8):
    tao.fd(100)
    tao.lt(45)

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()


Siri()
Go(200,100)




    
