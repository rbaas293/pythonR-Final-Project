# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:07:08 2019

@author: issac
"""


#t = 0:1  #               Time
#x = -10:10
#y = -1*(x**2)+100
import math
import matplotlib.pyplot as plt

angle = 89  #              Begining the slider value
Vel = 35.7632 # m/s        Initial Velocity
ay = -9.81 # m/s           Gravity
#math.sin(x)  #            Return the sine of x radians.
#math.radians(x)  #        Convert angle x from degrees to radians.
Vel_y = Vel * math.sin( math.radians(angle) )  # Velocity in the y direction
Vel_x = Vel * math.cos( math.radians(angle) )  # Velocity in the x direction

time_F = (-Vel_y - math.sqrt(Vel_y**2) ) / ay  # object time of Flight

Height_y = []      # Updated Heighth per fraction of second
Distance_x = []    # Updated distance per fraction of second

count = 0
equals = 0


while equals < time_F:
    equals = equals + 0.000001 #(1*10**6)
    count = count + 1

t = 0
#time_F = 5
#count = 0
#equals = 0
#while equals < time_F: # > (1*10**6):
#    equals = equals + (1*10**6)
#    count += 1

for i in range(0,count):
    Height_ynow = Vel_y * (t*10**-6) + 0.5 * ay * (t*10**-6)**2
    Height_y.append(Height_ynow)
    Distance_xnow = Vel_x * (t*10**-6)
    Distance_x.append(Distance_xnow)
    t += 1
t = time_F
Height_ynow = Vel_y * (t*10**-6) + 0.5 * ay * (t*10**-6)**2
Height_y.append(Height_ynow)
Distance_xnow = Vel_x * (t*10**-6)
Distance_x.append(Distance_xnow)    
    
#len(Distance_x)
final_point = Distance_x[count]

plt.plot(Distance_x,Height_y,'r')      #label='F1')
#plt.plot(final_point,0,'ro');
plt.ylabel('Projectile Heighth')
plt.xlabel('t in time')
plt.title('Pojectile Motion')
plt.show()
    
#time_Fcount = time_F

#for i in range(0,6):
#    Height_ynow = Vel_y * (t) + 0.5 * ay * (t)**2
#    Height_y.append(Height_ynow)
#    Distance_xnow = Vel_x * (t)
#    Distance_x.append(Distance_xnow)
#for i in range(0,(time_F*(10**6))):
#    Height_ynow = Vel_y * (t*10**-6) + 0.5 * ay * (t*10**-6)**2
#    Height_y.append(Height_ynow)
#    Distance_xnow = Vel_x * (t*10**-6)
#    Distance_x.append(Distance_xnow)

#plt.plot(x,f2,'b',label='F2')
#plt.plot(x,f3,'g',label='F3')
#legend = plt.legend(loc='lower center', shadow=True, fontsize='x-large')











#thislist = []
#thislist.append(1)
#thislist[0] + 1
#
#2*(1*10**(-6))
#2*(1*10**-6)
#1e-6+1e-6+1e-6
#
#
#len(thislist)











