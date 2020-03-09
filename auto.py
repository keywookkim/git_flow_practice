import os
import time
from datetime import datetime, timedelta

time2 = datetime.now()

for i in range(365, 367):
    what_day = (time2 - timedelta(days=i)).strftime('%a %b %d %H:%M:%S %Y')

    f = open("/Users/kw/workspace/git_flow_practice/auto.txt", 'w')
    f.write(f'{i}')
    f.close

    os.system(f'git commit -am "오토 깃 테스트{i}"')
    os.system(
        f'git commit --amend --no-edit --date "{what_day} +0900T"')
    os.system(f'git push origin main')

    print(f'{i + 1}회차 완료되었음')
