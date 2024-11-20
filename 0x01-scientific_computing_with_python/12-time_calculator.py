start = '3:00 PM'
duration = '3:10'

start_no_space=list(start.replace(' ',''))
start_no_pm_am =  start_no_space[:-2]
duration_lst = list(duration)

for i, j in start_no_pm_am, duration_lst:
    print(i+j)

