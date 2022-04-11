# 마라톤 훈련 지원 프로그램
import math
# 이 함수는 분과 초로 표시된 시간을 초 단위로 변환한다.
def total_seconds(min, sec):
    return min * 60 + sec
# 이 함수는 (초 단위로 주어지는) 마일 당 주행 시간으로부터
# 시간 당 마일 단위의 속도를 계산한다.
def speed(time):
    return 3600 / time
# 사용자에게 속도와 주행 거리를 입력하도록 안내한다.
pace_minutes = int(input('Minutes per mile? '))
pace_seconds = int(input('Seconds per mile? '))
miles = int(input('Total miles? '))
# 속도를 계산하여 출력한다.
mph = speed(total_seconds(pace_minutes, pace_seconds))
print('Your speed is ' + str(mph) + ' mph')
# 계획된 훈련에 대해 소요 시간을 계산한다.
total = miles * total_seconds(pace_minutes, pace_seconds)
elapsed_minutes = total // 60
elapsed_seconds = total % 60
print('Your elapsed time is ' + str(elapsed_minutes) +' mins ' + str(elapsed_seconds) + ' secs')