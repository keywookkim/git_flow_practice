import os
import time
from datetime import datetime, timedelta


# day_box = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
# month_box = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# thisyear = 2021
# start_date = 5

time2 = datetime.now()

for i in range(180):
    f = open("/Users/kw/workspace/git_flow_practice/auto.txt", 'w')
    f.write(f'{i}')
    f.close
    os.system(f'git commit -am "오토 깃 테스트{i}"')

    what_day = (time2 + timedelta(days=-1*i)).strftime('%a %b %d %H:%M:%S %Y')
    os.system(
        f'git commit --amend --no-edit --date "{what_day} +0900T"')
    os.system(f'git push origin main')
    print(f'{i + 1}번 완료')


# print('현재 시간부터 0일 뒤')
# # 2018-07-28 20:58:59.666626
# print((time2 + timedelta(days=0)).strftime('%a %b %d %H:%M:%S %Y'))
# print('현재 시간부터 3일 전')
# print(time2 + timedelta(days=-3))  # 2018-07-20 20:58:59.666626
# print('현재 시간부터 1일 뒤의 2시간 전')
# print(time2 + timedelta(days=1, hours=-2))  # 2018-07-24 18:58:59.666626
# print(time.localtime(time.time()))
