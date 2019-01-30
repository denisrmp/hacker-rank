# https://www.hackerrank.com/challenges/time-conversion

time = input().strip()

if time[0:2] == '12':
    if time[-2] == 'A':
        time = '00' + time[2:]
elif time[-2] == 'P':
    time = str(int(time[0:2]) + 12) + time[2:]

print(time[0:len(time)-2])
