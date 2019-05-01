# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:07:08 2019

@author: issac
"""
import math
import matplotlib.pyplot as plt


def cartoon():
    
    Vel = float(input ('enter the velocity the projectile was shot (in meters/second): '))
    angle = float(input ('enter the angle the projectile was shot at (in degrees): '))

    colore = int(input ('chose a color for Earth 1 = blue, 2 = red, 3 = green, 4 cyan, 5 = white: '))
    colormo = int(input ('chose a color for our Moon 1 = blue, 2 = red, 3 = green, 4 cyan, 5 = white: '))
    colorma = int(input ('chose a color for Mars 1 = blue, 2 = red, 3 = green, 4 cyan, 5 = white: '))

    while (Vel < 0) or (angle < 0):
        print('PLEASE CHOOSE A POSITIVE NUMBER ABOVE ZERO')
        Vel = float(input ('enter the velocity the projectile was shot (in meters/second): '))
        angle = float(input ('enter the angle the projectile was shot at (in degrees): '))
    
        
    if colore == 1:
        colore = 'b,'
    elif colore == 2:
        colore = 'r,'
    elif colore == 3:
        colore = 'g,'
    elif colore == 4:
        colore = 'c,'
    else:
        colormo = 'w,'
    if colormo == 1:
        colormo = 'b,'
    elif colormo == 2:
        colormo = 'r,'
    elif colormo == 3:
        colormo = 'g,'
    elif colormo == 4:
        colormo = 'c,'
    else:
        colorma = 'w,'
    if colorma == 1:
        colorma = 'b,'
    elif colorma == 2:
        colorma = 'r,'
    elif colorma == 3:
        colorma = 'g,'
    elif colorma == 4:
        colorma = 'c,'
    else:
        colorma = 'w,'


    ay = -9.81 # m/s              Gravity on Earth
    aymoon = -1.62 # m/s^2        Gravity on the Moon
    aymars = -3.71 # m/s^2        Gravity on Mars
    
    
    
    Vel_y = Vel * math.sin( math.radians(angle) )  # Velocity in the y direction
    Vel_x = Vel * math.cos( math.radians(angle) )  # Velocity in the x direction
    time_F = (-Vel_y - math.sqrt(Vel_y**2) ) / ay  # object time of Flight
    time_Fmoon = (-Vel_y - math.sqrt(Vel_y**2) ) / aymoon  # object time of Flight
    time_Fmars = (-Vel_y - math.sqrt(Vel_y**2) ) / aymars  # object time of Flight
    
    Height_y = []      # Updated Heighth per fraction of second
    Height_ymoon = []      # Updated Heighth per fraction of second
    Height_ymars = []      # Updated Heighth per fraction of second
    Distance_x = []    # Updated distance per fraction of second
    Distance_xmoon = []    # Updated distance per fraction of second
    Distance_xmars = []    # Updated distance per fraction of second
    zeros = []
    zerosmoon = []
    zerosmars = []
    count = 0
    countmoon = 0
    countmars = 0
    equals = 0
    equalsmoon = 0
    equalsmars = 0
    t = 0
    tmoon = 0
    tmars = 0
    
    while equals < time_F:
        equals = equals + 0.001 #(1*10**3)
        count = count + 1
    while equalsmoon < time_Fmoon:
        equalsmoon = equalsmoon + 0.001 #(1*10**3)
        countmoon = countmoon + 1
    while equalsmars < time_Fmars:
        equalsmars = equalsmars + 0.001 #(1*10**3)
        countmars = countmars + 1
    
    for i in range(0,count):
        zeros.append(t)
        Height_ynow = Vel_y * (t*10**-3) + 0.5 * ay * (t*10**-3)**2
        Height_y.append(Height_ynow)
        Distance_xnow = Vel_x * (t*10**-3)
        Distance_x.append(Distance_xnow)
        t += 1
    for j in range(0,countmoon):
        zerosmoon.append(tmoon)
        Height_ynowmoon = Vel_y * (tmoon*10**-3) + 0.5 * aymoon * (tmoon*10**-3)**2
        Height_ymoon.append(Height_ynowmoon)
        Distance_xnowmoon = Vel_x * (tmoon*10**-3)
        Distance_xmoon.append(Distance_xnowmoon)
        tmoon += 1
    for k in range(0,countmars):
        zerosmars.append(tmars)
        Height_ynowmars = Vel_y * (tmars*10**-3) + 0.5 * aymars * (tmars*10**-3)**2
        Height_ymars.append(Height_ynowmars)
        Distance_xnowmars = Vel_x * (tmars*10**-3)
        Distance_xmars.append(Distance_xnowmars)
        tmars += 1

    Max_Length = Distance_xnow
    Max_Lengthmoon = Distance_xnowmoon
    Max_Lengthmars = Distance_xnowmars
    t = time_F
    tmoon = time_Fmoon
    tmars = time_Fmars

    zeros = len(Distance_x) - 1
    zerosmoon = len(Distance_xmoon) - 1
    zerosmars = len(Distance_xmars) - 1
    Max_Height = Vel_y * (time_F/2) + 0.5 * ay * (time_F/2)**2;
    Max_Heightmoon = Vel_y * (time_Fmoon/2) + 0.5 * aymoon * (time_Fmoon/2)**2;
    Max_Heightmars = Vel_y * (time_Fmars/2) + 0.5 * aymars * (time_Fmars/2)**2;
    Final_Time = time_F;
    Final_Timemoon = time_Fmoon;
    Final_Timemars = time_Fmars;


    xaxis = Max_Lengthmoon + Max_Lengthmoon*0.05
    yaxis = Max_Heightmoon + Max_Heightmoon*0.05
    

    plt.figure(figsize=(15,7.5))
    plt.style.use('dark_background')
    plt.subplots_adjust(top=0.9, hspace=0.7)

    plt.subplot(3,1,1)
    plt.axis([0, xaxis, 0, yaxis])
    plt.plot(Distance_x, Height_y, colore)    #label='F1')
    plt.title('Pojectile Motion on Earth')
    plt.ylabel('Projectile Heighth (m)')
    plt.xlabel('Distance (m)')

    plt.subplot(3,1,2)
    plt.axis([0, xaxis, 0, yaxis])
    plt.plot(Distance_xmoon, Height_ymoon, colormo)    #label='F1')
    plt.title('Pojectile Motion our Moon')
    plt.ylabel('Projectile Heighth (m)')
    plt.xlabel('Distance (m)')

    plt.subplot(3,1,3)
    plt.axis([0, xaxis, 0, yaxis])
    plt.plot(Distance_xmars, Height_ymars, colorma)    #label='F1')
    plt.title('Pojectile Motion on Mars')
    plt.ylabel('Projectile Heighth (m)')
    plt.xlabel('Distance(m)')

    print('\n\n\n**Projectile Information**\nOn Earth \nMaximum Height: ', round(Max_Height,3), '(m)', '\nFinal Distance of Impact: ', round(Max_Length,3), '(m)', '\nTime of Flight: ', round(Final_Time,3), '(s)')
    print('\n\n\n**Projectile Information**\nOn Our Moon \nMaximum Height: ', round(Max_Heightmoon,3), '(m)', '\nFinal Distance of Impact: ', round(Max_Lengthmoon,3), '(m)', '\nTime of Flight: ', round(Final_Timemoon,3), '(s)')
    print('\n\n\n**Projectile Information**\nOn Mars \nMaximum Height: ', round(Max_Heightmars,3), '(m)', '\nFinal Distance of Impact: ', round(Max_Lengthmars,3), '(m)', '\nTime of Flight: ', round(Final_Timemars,3), '(s)')
    
    
    return()


z = cartoon()







