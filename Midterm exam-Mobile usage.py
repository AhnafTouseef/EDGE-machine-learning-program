import numpy as np

Gender_list=[]
Screen_time=[]
App_used=[]

DF = open('mobile_usage_behavioral_analysis - mobile_usage_behavioral_analysis.csv','r')
line=DF.readline()
line=DF.readline()
while (len(line)>0):
    arr=line.strip().split(',')
    gender=arr[2]
    screen=arr[3]
    app=arr[4]
    Gender_list.append(gender)
    Screen_time.append(screen)
    App_used.append(app)
    line=DF.readline()

DF.close()

Screen_time=np.array(Screen_time, dtype=float)
App_used=np.array(App_used, dtype=float)

print('\nList of Gender \n',Gender_list)
print('\nNumpy array of screen time \n',Screen_time)
print('\nNumpy array of app used \n',App_used)

print('\nMinimun screen time ',np.min(Screen_time))
print('Maximum screen time ',np.max(Screen_time))
print('Median of screen time ',np.median(Screen_time))

print('\nMinimun App used ',np.min(App_used))
print('Maximum App used ',np.max(App_used))
print('Median of App used ',np.median(App_used))