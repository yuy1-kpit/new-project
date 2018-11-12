"""
Created on Tue Nov  6 14:36:11 2018
What Pandas stand for? I don not care :)
I go downstairs and upstairs in the building where KPIT office is 
to collect datas. The whole time is about 5 min. 
Features:
    1. The height of the buildings(The building has 6 floors.)
    2. How many stairs (I counts the stairs maunlly, it is totally 212 stairs.)
    3. The magnetic filed distribution with respect of the Altitude in
       the building.
@author: yuy1
"""
from math import sqrt
import pandas as pd
#from sklearn import preprocessing
from scipy.signal import savgol_filter, find_peaks
#from mpl_toolkits import mplot3d
#import matplotlib.animation as animation
#from matplotlib import style
import matplotlib.pyplot as plt
#from scipy import integrate
import numpy as np

def Speed_calulation(Acc, time_interval):
    """
    In order to calculate the speed using acceleration data
    """
    Speed = [0,]
    speed_temp = 0
    for i in range(len(Acc)-1):
        speed_temp = speed_temp + (Acc[i]+Acc[i+1])*time_interval/2
        Speed.append(speed_temp)
    return Speed
def distance_calulation(acc_value, speed_value, time_interval):
    """
    In order to calculate the distance using acceleration and speed data
    """
    Distance = [0,]
    distance_temp = 0
    for i in range(len(speed_value)-1):
        distance_temp = distance_temp \
                        + (speed_value[i] \
                        +speed_value[i+1])*time_interval/2 #\
                        # + (acc_value[i]+acc_value[i+1])*(time_interval**2)/2
        Distance.append(distance_temp)
    return Distance
"""load datas"""
data_file = pd.read_csv('Sensor_record_20181108_115327_AndroSensor.csv')
time = data_file['Time since start in ms']
total_time = time[69138] - time[0]
print('total recording time is : %f min' %(total_time/60000))
#acceloration
acc_X = data_file['ACCELEROMETER X (m/s²)']
acc_Y = data_file['ACCELEROMETER Y (m/s²)']
acc_Z = data_file['ACCELEROMETER Z (m/s²)']
#gravity
grav_X = data_file['GRAVITY X (m/s²)']
grav_Y = data_file['GRAVITY Y (m/s²)']
grav_Z = data_file['GRAVITY Z (m/s²)']
#MAGNETIC FIELD X (Î¼T)
Mag_X = data_file['MAGNETIC FIELD X (μT)']
Mag_Y = data_file['MAGNETIC FIELD Y (μT)']
Mag_Z = data_file['MAGNETIC FIELD Z (μT)']
#linear acc
linear_acc_X = data_file['LINEAR ACCELERATION X (m/s²)']
linear_acc_Y = data_file['LINEAR ACCELERATION Y (m/s²)']
linear_acc_Z = data_file['LINEAR ACCELERATION Z (m/s²)']
#print(linear_acc_X.mean())
#print(linear_acc_Y.mean())
#print(linear_acc_Z.mean())
#GYROSCOPE (rad/s)
Gyro_X = data_file['GYROSCOPE X (rad/s)']
Gyro_Y = data_file['GYROSCOPE Y (rad/s)']
Gyro_Z = data_file['GYROSCOPE Z (rad/s)']
#LOCATION
Loca_Latitude = data_file['LOCATION Latitude : ']
Loca_Longitude = data_file['LOCATION Longitude : ']
Loca_Altitude = data_file['LOCATION Altitude ( m)']
Aver_Loca_accuracy = data_file['LOCATION Accuracy ( m)'].mean()
Aver_Latitude = data_file['LOCATION Latitude : '].mean()
Aver_Longitude = data_file['LOCATION Longitude : '].mean()

"""visualization"""
#acceleration comperation and show
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes[0, 0].plot(time[::1000], acc_X[::1000]-grav_X[::1000], label='acc_X-grav_X')
axes[0, 1].plot(time[::1000], acc_Y[::1000]-grav_Y[::1000], label='acc_Y-grav_Y')
axes[1, 0].plot(time[::1000], acc_Z[::1000]-grav_Z[::1000], label='acc_Z-grav_Z')
axes[0, 0].plot(time[::1000], linear_acc_X[::1000], label='linear_acc_X')
axes[0, 1].plot(time[::1000], linear_acc_Y[::1000], label='linear_acc_Y')
axes[1, 0].plot(time[::1000], linear_acc_Z[::1000], label='linear_acc_Z')
axes[0, 0].set_xlabel('Time in ms')
axes[0, 0].set_ylabel('Accelerometer value X(m/s²)')
axes[0, 0].legend(loc='upper right')
axes[0, 1].set_xlabel('Time in ms')
axes[0, 1].set_ylabel('Accelerometer value Y(m/s²)')
axes[0, 1].legend(loc='upper right')
axes[1, 0].set_xlabel('Time in ms')
axes[1, 0].set_ylabel('Accelerometer value Z(m/s²)')
axes[1, 0].legend(loc='upper right')
linear_acc_X = savgol_filter(linear_acc_X, 49, 3, mode='nearest')
linear_acc_Y = savgol_filter(linear_acc_Y, 49, 3, mode='nearest')
linear_acc_Z = savgol_filter(linear_acc_Z, 49, 3, mode='nearest')
axes[1, 1].plot(time[::1000], linear_acc_X[::1000], time[::1000], \
                linear_acc_Y[::1000], time[::1000], linear_acc_Z[::1000])
axes[1, 1].set_xlabel('Time in ms')
axes[1, 1].set_ylabel('Accelerometer value after fliter(m/s²)')
#altitude show
plt.figure(2, figsize=(15, 10))
plt.plot(time, Loca_Altitude-data_file['LOCATION Accuracy ( m)'])
print("Altitude difference(The Hight of KPIT office): %f m" %(abs(max(Loca_Altitude)-min(Loca_Altitude)-Aver_Loca_accuracy)))
plt.xlabel('Time in ms')
plt.ylabel('Altitude in m')
#Speed calculation + preprocessing(Savitzky–Golay filter)
#linear_acc_X = preprocessing.scale(linear_acc_X)
#linear_acc_Y = preprocessing.scale(linear_acc_Y)
#linear_acc_Z = preprocessing.scale(linear_acc_Z)
x_speed = np.trapz(linear_acc_X, time/1000)
y_speed = np.trapz(linear_acc_Y, time/1000)
z_speed = np.trapz(linear_acc_Z, time/1000)
print('X_final speed %f m/s' %x_speed)
print('Y_final speed %f m/s' %y_speed)
print('Z_final speed %f m/s' %z_speed)
x = Speed_calulation(linear_acc_X, 0.005)
y = Speed_calulation(linear_acc_Y, 0.005)
z = Speed_calulation(linear_acc_Z, 0.005)
plt.figure(3, figsize=(15, 10))
location_speed = data_file['LOCATION Speed ( Kmh)']*60/1000
plt.plot(time, location_speed, 'black', label='location speed from original data')
plt.plot(time, x, 'r', label='x speed')
plt.plot(time, y, 'b--', label='y speed')
plt.plot(time, z, 'g', label='z speed')
plt.xlabel('Time in ms')
plt.ylabel('Location speed in m/s')
plt.legend(loc='upper right')
#distance calculation
x = savgol_filter(x, 5, 2)
y = savgol_filter(y, 5, 2)
z = savgol_filter(z, 5, 2)
plt.figure(4, figsize=(15, 10))
x_distance = distance_calulation(linear_acc_X, x, 0.005)
y_distance = distance_calulation(linear_acc_Y, y, 0.005)
z_distance = distance_calulation(linear_acc_Z, z, 0.005)
plt.plot(time, x_distance, 'r', time, y_distance, 'b--', time, z_distance, 'g')
plt.xlabel('Time in ms')
plt.ylabel('Distance in m')
#plt.plot(time,total_Mag_sqrt,time,abs(Loca_Altitude-Aver_Loca_accuracy))
plt.figure(5, figsize=(15, 10))
peak, _ = find_peaks(linear_acc_Z, 2.9)
plt.plot(linear_acc_Z)
plt.plot(peak, linear_acc_Z[peak], "ob")
plt.xlabel('linear_acc_Z')
plt.ylabel('Peaks in linear_acc_Z')
print('Their are total %d stairs'%len(peak))
#Magnetic field vs Altitude
total_Mag = Mag_X**2+Mag_Y**2+Mag_Z**2
total_Mag_sqrt = [sqrt(number) for number in total_Mag]
fig, ax1 = plt.subplots(figsize=(15, 10))
ax1.plot(time, total_Mag_sqrt, label='Magnetic Field')
plt.legend(loc='upper left')
ax2 = ax1.twinx()
ax2.plot(time, abs(Loca_Altitude[:]-Aver_Loca_accuracy), 'r--', label='Altitude')
ax1.set_xlabel('time in ms')
ax1.set_ylabel('Magnetic Field in μT', color='g')
ax2.set_ylabel('Altitude in m', color='b')
plt.legend(loc='upper right')
#plt.hist(total_Mag_sqrt, bins=100)
