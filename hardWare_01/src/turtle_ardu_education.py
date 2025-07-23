'''
목표 : 아두이노에서 전달받은 초음파 센서 값에 따른 turtle 제어

1. 센서 데이터 
2. 거북이 제어

MVP : Minimum Viable Product (최소 기능 제품)
'''
import turtle
import serial
import time

# 전역 변수
connection = None
current_distance = 0
MIN_DISTANCE = 10    # 불변하는 전역변수는 대문자로 적는다.

def connect_sensor(port='COM3'):
    global connection
    try:
        connection = serial.Serial(port, 9600)
        time.sleep(2)
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
            if 2 <= distance <= 400:          
                current_distance = distance
            return distance
        except:
            pass
    return None

# turtle 초기 설정
def setup_turtle():
    s = turtle.Screen()
    t = turtle.Turtle()
    
# turtle 제어 - 거리 조건에 따른 움직임 제어    
def control_turtle():
    if current_distance < MIN_DISTANCE:
        if is_moving:
            print(f"장애물")
            is_moving = False # 상태를 정지로 변경
    else:
        if is_moving:
            print(f"전진")
            is_moving = True  # 상태를 이동으로 변경
            
        turtle.forward(2)

def main():   
    try:
        control_turtle()      
    except KeyboardInterrupt:   
    if connect_sensor():
        for i in range(10):
            dist = read_distance()
            if dist:
                print(f"거리: {dist}cm")
            time.sleep(0.5)

if __name__ == "__main__":
    main()