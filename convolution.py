import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import integrate


class Convolution ():

    #def __init__(self): # not necessary

    def Gaussian (self,x,sigma):
        const = math.sqrt(2*math.pi)
        appo = 1/const/sigma * np.exp(- np.power(x,2)/2./(sigma**2))
        return appo

    # convolution of f with a gaussian in the range E

    # using np.convolve()
    def np_conv(self,f,E,sigma='',a='',b='',plot_this=False): 

        Evis = E - 0.8

        if sigma != '':
            
            g = self.Gaussian(Evis-np.mean(Evis),sigma)
            self.conv_np = np.convolve(f,g,mode='same')

        if a != '' or b != '':
        
            rad = a**2 / Evis + b**2
            sigma_Evis = np.sqrt(rad) * Evis

            g = self.Gaussian(Evis-np.mean(Evis),sigma_Evis)
            self.conv_np = np.convolve(f,g,mode='same')

        if plot_this:

            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot(Evis,f,'b',linewidth=1,label='Unconvolved spectrum')
            ax.set_xlabel(r'$\text{E}_{\text{vis}}$ [\si{MeV}]')
            ax.set_ylabel(r'N($\bar{\nu}$) [arb. unit]')
            ax.set_title(r'Starting spectrum')
            ax.grid()
            ax.legend()

            fig1 = plt.figure()
            ax1 = fig1.add_subplot(111)
            ax1.plot(Evis,self.conv_np,'b',linewidth=1,label='Convolved spectrum')
            ax1.set_xlabel(r'$\text{E}_{\text{vis}}^{\text{obs}}$ [\si{MeV}]')
            ax1.set_ylabel(r'N($\bar{\nu}$) [arb. unit]')
            ax1.set_title(r'Convolution (numpy) with a Gaussian' + '\nwith variable width')
            ax1.grid()
            ax1.legend()

        return self.conv_np



    # using a numerical method
    # fixed sigma as input
    def numerical_conv(self,f,E,sigma='',a='',b='',plot_this=False):

        Evis = E - 0.8

        if sigma != '':

            #print('fixed sigma')

            # numerical convolution (over Evis)
            self.conv_num = np.zeros(len(Evis))
            n=0
            for E0 in Evis:
                appo = self.Gaussian(Evis-E0,sigma)
                prod = appo * f
                #self.conv_num[n] = prod.sum() # da sostituire con integrale simpson
                self.conv_num[n] = integrate.simps(prod,Evis) # da sostituire con integrale simpson
                n += 1
            
        if a != '' or b != '':

            #print('variable sigma')
        
            rad = a**2 / Evis + b**2
            sigma_Evis = np.sqrt(rad) * Evis

            # numerical convolution (over Evis)
            self.conv_num = np.zeros(len(Evis))
            n=0
            for E0 in Evis:
                appo = self.Gaussian(Evis-E0,sigma_Evis)
                prod = appo * f
                #self.conv_num[n] = prod.sum() # da sostituire con integrale simpson
                self.conv_num[n] = integrate.simps(prod,Evis) # da sostituire con integrale simpson
                n += 1

        if plot_this:

            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot(Evis,f,'b',linewidth=1,label='Unconvolved spectrum')
            ax.set_xlabel(r'$\text{E}_{\text{vis}}$ [\si{MeV}]')
            ax.set_ylabel(r'N($\bar{\nu}$) [arb. unit]')
            ax.set_ylim(-0.005,0.095)
            ax.set_title(r'Starting spectrum')
            ax.grid()
            ax.legend()

            fig1 = plt.figure()
            ax1 = fig1.add_subplot(111)
            ax1.plot(Evis,self.conv_num,'b',linewidth=1,label='Convolved spectrum')
            ax1.set_xlabel(r'$\text{E}_{\text{vis}}^{\text{obs}}$ [\si{MeV}]')
            ax1.set_ylabel(r'N($\bar{\nu}$) [arb. unit]')
            ax1.set_ylim(-0.005,0.095)
            ax1.set_title(r'Numerical convolution with a Gaussian' + '\nwith variable width')
            ax1.grid()
            ax1.legend()

        return self.conv_num        








