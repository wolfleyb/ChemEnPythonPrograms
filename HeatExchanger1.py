# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 19:12:24 2015

@author: Ben
"""

from __future__ import division
import numpy as np


# Function to ensure liquid state
def state_test(stream_type, streamtemp):
    if stream_type == 1 and streamtemp > 373.15 or streamtemp < 273:
        print('Temperature outside of liquid range')
        quit()
    
    elif stream_type == 2 and streamtemp > 247.08 or streamtemp < 172.00:
        print('Temperature outside of liquid range')        
        quit()
    
    elif stream_type == 3 and streamtemp > 351.44 or streamtemp < 159.05:
        print('Temperature outside of liquid range')        
        quit()
    
    elif stream_type == 4 and streamtemp > 372.388 or streamtemp < 165.777:
        print('Temperature outside of liquid range')        
        quit()


# Function to ensure correct input type.
def num_test(var):
    try:
        var = float(var)
    except ValueError:
        print "Invalid Input: Numbers Only"
        quit()


#Figure out units
print('Choose unit system:')
print('1-SI')
print('2-AES')
system = raw_input('Selection: ')
num_test(system)
system = int(system)
if system != 1 and system != 2:
    print('Invalid Entry')
    quit()
    

#Specify known out
print(' ')
print('Are you specifying the Temperature of the Hot Stream or Cold Stream out?:')
print('1-Hot Stream')
print('2-Cold Stream')
hotcoldselection = raw_input('Selection: ')
num_test(hotcoldselection)
hotcoldselection = int(hotcoldselection)
if  hotcoldselection != 1 and  hotcoldselection != 2:
    print("Invalid Entry")
    quit()

#Input info, SI units
if system == 1 :
    #mass flow rate cold input
    print(' ')
    mcold = raw_input('Input mass flow rate cold stream in kg/s: ')  #kg/s
    num_test(mcold)
    mcold = float(mcold)
    
    #mass flow rate hot input
    mhot = raw_input('Input mass flow rate hot stream in kg/s: ')  #kg/s
    num_test(mhot)
    mhot = float(mhot)
    
    #Hot inlet temperature
    Thot_in = raw_input('Input inlet temp hot stream K: ') #K
    num_test(Thot_in)
    Thot_in = float(Thot_in)    
    
    #Cold inlet temperature    
    Tcold_in = raw_input('Input inlet temp cold stream K: ') #K
    num_test(Tcold_in)
    Tcold_in = float(Tcold_in)
    
    #Known Outlet temperature
    if hotcoldselection == 1:
        Thot_out = raw_input('Desired outlet temp, hot stream in K: ')
        num_test(Thot_out)
        Thot_out = float(Thot_out)
        
    elif hotcoldselection == 2:
        Tcold_out = raw_input('Desired outlet temp, cold stream in K: ')#K
        num_test(Tcold_out)
        Tcold_out = float(Tcold_out)



elif system == 2:       #AES Conversion
    
    #mass flow rate cold stream
    print(' ')
    mcold = raw_input('Input mass flow rate cold stream in lbm/s: ')  #kg/s
    num_test(mcold)
    mcold = float(mcold)
    
    #mass flow rate hot stream
    mhot = raw_input('Input mass flow rate hot stream in lbm/s: ')  #kg/s
    num_test(mhot)
    mhot = float(mhot)
    
    #Hot inlet temperature input
    Thot_in = raw_input('Input inlet temp hot stream F: ') #K
    num_test(Thot_in)
    Thot_in = float(Thot_in)
    
    #Cold inlet temperature input
    Tcold_in = (raw_input('Input inlet temp cold stream F: ')) #K
    num_test(Tcold_in)
    Tcold_in = float(Tcold_in)
    
    #Known Outlet temperature input
    if hotcoldselection == 1:
        Thot_out = (raw_input('Desired outlet temp, hot stream in F: '))
        num_test(Thot_out)        
        Thot_out = float(Thot_out)
        Thot_out = (Thot_out + 459.67) * (5/9)
        
        
    elif hotcoldselection == 2:
        Tcold_out = (raw_input('Desired outlet temp, cold stream in F: ')) #K
        num_test(Tcold_out)
        Tcold_out = float(Tcold_out)
        Tcold_out = (Tcold_out + 459.67) * (5/9)
        
    
    
    
    #Convert to SI
    mcold = mcold * 0.453592
    mhot = mhot * 0.453592
    Thot_in = (Thot_in + 459.67) * (5/9)
    Tcold_in = (Tcold_in + 459.67) * (5/9)
    
#input Heat Transfer Coefficient
U = (raw_input ('Overall Heat Transfer Coefficient (J/(s*m^2*K)): '))
num_test(U)
U = float(U)

#find hot liquid type liquid type
print('------------------------------------------------')
print('Select hot liquid type:')
print('1-water')
print('2-R134a')
print('3-ethanol')
print('4-2,2,4-trimethylpentane')
hliq = raw_input('Selection: ')
num_test(hliq)
hliq = int(hliq)
  
    
#specify cold stream
print (' ')
print('------------------------------------------------')
print('Select cold liquid type:')
print('1-water')
print('2-R134a')
print('3-ethanol')
print('4-2,2,4-trimethylpentane')
cliq = raw_input('Selection: ')
num_test(cliq)
cliq = int(cliq)

#specify specific heat on hot stream
if hliq == 1: #water
    cp_hot = 2.7637 * 10 ** 5 + (-2.0901 * 10 ** 3) * Thot_in + 8.125 * Thot_in ** 2 + (-1.4116 * 10 ** -2) * Thot_in ** 3 + (9.3701 * 10 ** -6) * Thot_in ** 4
    cp_hot = cp_hot / 18.015 #Coverting kmol to kg

elif hliq == 2: #R134a
    cp_hot = 6.5108 * 10 ** 5 + (-9.5057 * 10 ** 3) * Thot_in + 62.835 * Thot_in ** 2 + (-1.8264 * 10 ** -1) * Thot_in ** 3 + (2.0031 * 10 ** -4) * Thot_in ** 4
    cp_hot = cp_hot / 102.0309

elif hliq == 3: #ethanol
    cp_hot = 1.0264 * 10 ** 5 + (-1.3963 * 10 ** 2) * Thot_in + (-3.0341 * 10 ** -2) * Thot_in ** 2 + (-2.0386 * 10 ** -3) * Thot_in ** 3
    cp_hot = cp_hot / 46.068

elif hliq == 4 #2,2,4-trimethylpentane
    cp_hot = 9.5275 * 10 ** 4 + (6.967 * 10 ** 2) * Thot_in + -1.3765 * Thot_in ** 2 + (2.1734 * 10 ** -3) * Thot_in ** 3
    cp_hot = cp_hot / 114.228

else:
    print("invalid input on hot stream in, terminating")
	quit()
    
#Specific heat on cold stream    
if cliq == 1: #water
    cp_cold = 2.7637 * 10 ** 5 + (-2.0901 * 10 ** 3) * Tcold_in + 8.125 * Tcold_in ** 2 + (-1.4116 * 10 ** -2) * Tcold_in ** 3 + (9.3701 * 10 ** -6) * Tcold_in ** 4
    cp_cold = cp_cold / 18.015 #Converting per kmol to per kg
elif cliq == 2: #R134a
    cp_cold = 6.5108 * 10 ** 5 + (-9.5057 * 10 ** 3) * Tcold_in + 62.835 * Tcold_in ** 2 + (-1.8264 * 10 ** -1) * Tcold_in ** 3 + (2.0031 * 10 ** -4) * Tcold_in ** 4
    cp_cold = cp_cold / 102.0309
elif cliq == 3: #ethanol
    cp_cold = 1.0264 * 10 ** 5 + (-1.3963 * 10 ** 2) * Tcold_in + (-3.0341 * 10 ** -2) * Tcold_in ** 2 + (-2.0386 * 10 ** -3) * Tcold_in ** 3
    cp_cold = cp_cold / 46.068
elif cliq == 4: #2,2,4-trimethylpentane
    cp_cold = 9.5275 * 10 ** 4 + (6.967 * 10 ** 2) * Tcold_in + -1.3765 * Tcold_in ** 2 + (2.1734 * 10 ** -3) * Tcold_in ** 3
    cp_cold = cp_cold / 114.228
else:
    print("invalid input cold stream in, terminating")
	quit()
    
#Solve for unknown Variable
if hotcoldselection == 1:
    Tcold_out = (((mhot * cp_hot) * (Thot_in - Thot_out)) / (mcold * cp_cold) + Tcold_in)

elif hotcoldselection == 2:
    Thot_out = -1 * (((mcold * cp_cold) * (Tcold_out - Tcold_in)) / (mhot * cp_hot) - Thot_in)

#make sure inlet in a liquid state
state_test(hliq, Thot_in)
state_test(hliq, Thot_out)
state_test(cliq, Tcold_in)
state_test(cliq, Tcold_out)



#Find q
q = mhot * cp_hot * (Thot_in - Thot_out)

#Tlog mean
dT1 = float(Thot_in - Tcold_out)
dT2 = Thot_out - Tcold_in

#Tlogmean
dTlm = float((dT2-dT1)/(np.log(dT2/dT1)))

#Compute Random Factors that I don't know what they do
R = (Thot_in - Thot_out)/(Tcold_out - Tcold_in)
P = (Tcold_out - Tcold_in)/(Thot_in-Tcold_in)

#Compute Fudge Factor
F = (np.sqrt(R**2 + 1)/(R-1))*((np.log((1-P)/(1-P*R)))/np.log((2-P*(R+1-np.sqrt(R**2+1)))/(2-P*(R+1+np.sqrt(R**2 + 1)))))
F = float(F)


#print outlet temperatures
print(' ')
print('****************************************************')
Thot_out = str("%.2f" % Thot_out)
Tcold_out = str("%.2f" % Tcold_out)
print ("Temperature of hot stream out: " + Thot_out + 'K')
print "Temperature of cold stream out: " + Tcold_out + 'K'

#Compute Area and Cost
A = q/(F*U*dTlm)
Cost = 1000 * A

#print surface area and cost
A = float("%.2f" % A)
Cost = float("%.2f" % Cost)
print('Surface area needed (m^2): ' + str(A))
print('Cost of Heat Exchanger: $' + str(Cost))
