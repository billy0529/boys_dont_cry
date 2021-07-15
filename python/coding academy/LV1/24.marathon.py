# 항상 일정한 속도로 달리는 기계가 있다고 합시다. 
# 이 기계의 100m 달리기 기록을 입력받으면 마라톤에서의 기록을 구하시면 됩니다. 마라톤 경기에서 달리는 거리는 42.195km입니다. 100m 달리기와 마라톤의 코스는 모두 직선이라고 합니다(회전 시 걸리는 시간을 고려하지 않습니다). 
# 기계의 파손 및 배터리 방전 시간도 고려하지 않습니다.

record = float(input('enter your record: '))
time = record * 42195 / 100
marathon_record = []
marathon_record.append(int(time) // 3600)
marathon_record.append((int(time) - marathon_record[0] * 3600) // 60)
marathon_record.append((int(time) - marathon_record[0] * 3600 - marathon_record[1] * 60))
marathon_record.append(int(round(time - int(time), 2) * 100))
print('The marathon record is: {}h {}m {}s {:0<}'
    .format(marathon_record[0], marathon_record[1], marathon_record[2], marathon_record[3]))





