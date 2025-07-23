import turtle
import serial
import time

s = turtle.getscreen()
t = turtle.Turtle()

t.color("red")
t.shape("turtle")

connection = None
servo_move = 0

def connect_sensor(port='COM5'):    # 시리얼 포트 설정
    global connection
    try:
        connection = serial.Serial(port, 9600)
        time.sleep(0.2)
        print("연결 성공")
        return True
    except:
       print("연결 실패")
       return False

def servo_move_check():    # 서보 모터의 움직임 확인
    global connection, servo_move
    if connection and connection.in_waiting > 0:
        data = connection.readline().decode().strip()
        return data == "0"
    return False
        
def main():
    if not connect_sensor():  # 연결 한 번만 시도
        return
    while True:
        move = servo_move_check()
        if move:
            t.fd(10)
        time.sleep(0.1)

if __name__ == "__main__":
    main()