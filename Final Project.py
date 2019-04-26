# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:07:08 2019

@author: issac
"""
import math

import matplotlib.pyplot as plt

#import matplotlib.animation as animation
#from matplotlib import style

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

#style.use('fivethirtyeight')

def cartoon():
    
    Vel = float(input ('enter the velocity the projectile was shot (in meters/second): '))
    angle = float(input ('enter the angle the projectile was shot at (in degrees): '))

    color = int(input ('chose a color 1 = blue, 2 = red, 3 = green, 4 cyan, 5 = white: '))

    
    if color == 1:
        color = 'b,'
    elif color == 2:
        color = 'r,'
    elif color == 3:
        color = 'g,'
    elif color == 4:
        color = 'c,'
    else:
        color = 'w,'

    #angle = 70  #           Begining the slider value
    #Vel = 35.7632 # m/s     Initial Velocity
    ay = -9.81 # m/s        Gravity
    
    Vel_y = Vel * math.sin( math.radians(angle) )  # Velocity in the y direction
    Vel_x = Vel * math.cos( math.radians(angle) )  # Velocity in the x direction
    time_F = (-Vel_y - math.sqrt(Vel_y**2) ) / ay  # object time of Flight
    
    Height_y = []      # Updated Heighth per fraction of second
    Distance_x = []    # Updated distance per fraction of second
    zeros = []
    count = 0
    equals = 0
    t = 0
    
    while equals < time_F:
        equals = equals + 0.000001 #(1*10**6)
        count = count + 1
    
    for i in range(0,count):
        zeros.append(t)
        Height_ynow = Vel_y * (t*10**-6) + 0.5 * ay * (t*10**-6)**2
        Height_y.append(Height_ynow)
        Distance_xnow = Vel_x * (t*10**-6)
        Distance_x.append(Distance_xnow)
        t += 1
#        plt.plot(Distance_x, Height_y, color)
#        plt.ylabel('Projectile Heighth')
#        plt.xlabel('Distance')
#        plt.cla()
#        plt.show()
    t = time_F
#    Height_ynow = Vel_y * (t*10**-6) + 0.5 * ay * (t*10**-6)**2
#    Height_y.append(Height_ynow)
#    Distance_xnow = Vel_x * (t*10**-6)
#    Distance_x.append(Distance_xnow)    
    zeros = len(Distance_x) - 1
    #final_point = Distance_x[count]     #len(Distance_x)

#    ax1.clear() 
#    ax1.plot(Height_y, Distance_x)

    plt.ylabel('Projectile Heighth')
    plt.xlabel('Distance')
    plt.title('Pojectile Motion')
    plt.style.use('dark_background')
    plt.plot(Distance_x, Height_y, color)    #label='F1')
    
#    plt.style.use('ggplot') #,'fivethirtyeight')
    
    Max_Height = Vel_y * (time_F/2) + 0.5 * ay * (time_F/2)**2
    Final_Time = time_F
    
    return(round(Max_Height,3), round(Distance_xnow,3), round(Final_Time,3))
    
#ani = animation.FuncAnimation(fig, cartoon, interval=1000)
#plt.show()

z = cartoon()
print('\n\n\n**Projectile Information** \nMaximum Height: ', z[0], '(m)', '\nFinal Distance of Impact: ', z[1], '(m)', '\nTime of Flight: ', z[2], '(s)')


#plt.axis([0, 50, 0, 70])
#plt.plot(final_point,0,'ro');



#plt.ylabel('Projectile Heighth')
#plt.xlabel('Distance')
#plt.title('Pojectile Motion')
#plt.show()
#
#zeros[6000000]
#zeros[6000001]



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
