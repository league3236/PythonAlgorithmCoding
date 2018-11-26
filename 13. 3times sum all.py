# 디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇초일가?
# 디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됩니다.

sum = 0
for i in range(24):
    for j in range(60):
        if str(i).find('3')!=-1 or str(j).find('3')!=-1:
            sum+=int(i)*60*60+int(j)*60

print(sum)
