from reactor import Reactor_Spectrum
from oscillation import Oscillation_Prob

import matplotlib.pyplot as plt
import numpy as np

class Oscillated_Spectrum (Oscillation_Prob,Reactor_Spectrum):

    def __init__(self,t12,m21,t13_N,m3l_N,t13_I,m3l_I):
        Reactor_Spectrum.__init__(self)
        Oscillation_Prob.__init__(self,t12,m21,t13_N,m3l_N,t13_I,m3l_I)

    def osc_spectrum(self,E,ordering,plot_this=False):

        # uses methods of parent classes 
        Reactor_Spectrum.unosc_spectrum(self,E,plot_this=False)
        Oscillation_Prob.eval_prob(self,E,0,plot_this=False)

        self.osc_spect_N = self.spectrum_un * self.prob_E_N
        self.osc_spect_I = self.spectrum_un * self.prob_E_I

        # normalized spectra
        self.norm_osc_spect_N = self.norm_spectrum_un * self.prob_E_N
        self.norm_osc_spect_I = self.norm_spectrum_un * self.prob_E_I

        if plot_this:

            fig = plt.figure()
            #fig.suptitle(r'Antineutrino spectrum')
            ax = fig.add_subplot(111)
            ax.legend()
            ax.grid()
            ax.set_xlabel(r'$\text{E}_{\nu}$ [\si{MeV}]')
            ax.set_ylabel(r'N($\bar{\nu}$) [arb. unit]')
            ax.set_title(r'Antineutrino spectrum')

            if ordering == 1 or ordering == 0: # NO

                ax.plot(E,self.norm_spectrum_un,'k',linewidth=1,label='Unoscillated spectrum')
                ax.plot(E,self.norm_osc_spect_N,'b',linewidth=1,label='NO')
                ax.legend()
                fig.savefig('Spectrum/osc_spectrum_N.pdf',format='pdf',transparent=True)

            if ordering == -1: # IO

                ax.plot(E,self.norm_spectrum_un,'k',linewidth=1,label='Unoscillated spectrum')
                ax.plot(E,self.norm_osc_spect_I,'r',linewidth=1,label='IO')
                ax.legend()
                fig.savefig('Spectrum/osc_spectrum_I.pdf',format='pdf',transparent=True)

            if ordering == 0: # IO

                ax.plot(E,self.norm_osc_spect_I,'r--',linewidth=1,label='IO')
                ax.legend()
                fig.savefig('Spectrum/osc_spectrum.pdf', format='pdf', transparent=True)










