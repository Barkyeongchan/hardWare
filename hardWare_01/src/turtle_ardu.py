import turtle
import serial
import time

# 스크린 생성
s = turtle.getscreen()

# 거북이 변수에 지정, 거북이 초기화
t = turtle.Turtle()
t.color("red")
t.shape("turtle")
t.penup()
t.goto(-300, 0)
t.pendown()

connection = None
current_distance = 0

def connect_sensor(port='COM5'):    # 시리얼 포트 설정
    global connection
    try:
        connection = serial.Serial(port, 9600)
        time.sleep(0.1)
        print("연결 성공")
        return True
    except:
       print("연결 실패")
       return False

def read_distance():
    global connection, current_distance
    if connection and connection.in_waiting > 0:
        data = connection.readline().decode().strip()
        try:
            distance = float(data)
            current_distance = distance
            return distance
        except:
            pass
    return None 

def main():
    if not connect_sensor():  # 연결 한 번만 시도
        return

    while True:
        dist = read_distance()  # print_distance 함수의 동작을 이곳으로 이동
        if dist:
            print(f"거리: {dist}cm")
            if dist > 10:  # 거리가 10보다 멀면 움직임, 반대면 멈춤
                t.fd(10)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
    
