#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 12:37:21 2021

@author: Viktor Sumida
"""

import matplotlib.pyplot as plt
import numpy as np

############################################################################
############### Parâmetro do CE: x #########################################
############################################################################

PKS_20161210_doublesize_C1_x = -0.502
PKS_20161210_doublesize_C1_sigma_x = 0.097
PKS_20161210_doublesize_C2_x = -1.820
PKS_20161210_doublesize_C2_sigma_x = 0.098
PKS_20161210_doublesize_C3_x = -2.467
PKS_20161210_doublesize_C3_sigma_x = 0.102

PKS_20161210_cropped_C1_x = -0.502
PKS_20161210_cropped_C1_sigma_x = 0.097
PKS_20161210_cropped_C2_x = -1.811
PKS_20161210_cropped_C2_sigma_x = 0.099
PKS_20161210_cropped_C3_x = -2.442
PKS_20161210_cropped_C3_sigma_x = 0.100

fig = plt.figure()

graph1 = fig.add_subplot(6, 4, 1)
ponto_inicial = [10, -10]
ponto_final = [10, -10]
graph1.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
graph1.set_title('PKS 0502+049 \n 2016-12-10', fontsize=10, fontweight='bold')
graph1.set_ylabel('x', fontsize=9, labelpad=6, fontweight="bold")
graph1.set_xlabel('x', fontsize=9, fontweight="bold", labelpad=0)
graph1.plot(PKS_20161210_doublesize_C1_x, PKS_20161210_cropped_C1_x,  'o', linestyle='none', markersize=5, color='black', label='C3')
graph1.errorbar(PKS_20161210_doublesize_C1_x, PKS_20161210_cropped_C1_x, xerr=PKS_20161210_doublesize_C1_sigma_x, yerr=PKS_20161210_cropped_C1_sigma_x, linestyle='none', markersize=9, color='black')
graph1.plot(PKS_20161210_doublesize_C2_x, PKS_20161210_cropped_C2_x,'o', linestyle='none', markersize=5, color='blue', label='C2')
graph1.errorbar(PKS_20161210_doublesize_C2_x, PKS_20161210_cropped_C2_x, xerr=PKS_20161210_doublesize_C2_sigma_x, yerr=PKS_20161210_cropped_C2_sigma_x, linestyle='none', markersize=9, color='blue')
graph1.plot(PKS_20161210_doublesize_C3_x, PKS_20161210_cropped_C3_x,'o', linestyle='none', markersize=5, color='green', label='C1')
graph1.errorbar(PKS_20161210_doublesize_C3_x, PKS_20161210_cropped_C3_x, xerr=PKS_20161210_doublesize_C3_sigma_x, yerr=PKS_20161210_cropped_C3_sigma_x, linestyle='none', markersize=9, color='green')
graph1.legend(loc='upper left', fontsize=6)
graph1.tick_params(axis="x", direction="in", labelsize=9)
graph1.tick_params(axis="y", direction="in", labelsize=9)
graph1.xaxis.set_ticks(np.arange(-3, 3, 1))
graph1.yaxis.set_ticks(np.arange(-3, 3, 1))
graph1.set_xlim(-3, 0)
graph1.set_ylim(-3, 0)

#################################################################################
PKS_20201201_doublesize_C1_x = -0.327
PKS_20201201_doublesize_C1_sigma_x = 0.083
PKS_20201201_doublesize_C2_x = -1.606
PKS_20201201_doublesize_C2_sigma_x = 0.085

PKS_20201201_cropped_C1_x = -0.412
PKS_20201201_cropped_C1_sigma_x = 0.090
PKS_20201201_cropped_C2_x = -1.661
PKS_20201201_cropped_C2_sigma_x = 0.086

graph2 = fig.add_subplot(6, 4, 2)
ponto_inicial = [10, -10]
ponto_final = [10, -10]
graph2.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
graph2.set_title('PKS 0502+049 \n 2020-12-01', fontsize=10, fontweight='bold')
#graph2.set_ylabel('x (mas)', fontsize=9, labelpad=-1, fontweight="bold")
graph2.set_xlabel('x', fontsize=9, fontweight="bold", labelpad=0)
graph2.plot(PKS_20201201_doublesize_C1_x, PKS_20201201_cropped_C1_x,  'o', linestyle='none', markersize=5, color='black', label='U')
graph2.errorbar(PKS_20201201_doublesize_C1_x, PKS_20201201_cropped_C1_x, xerr=PKS_20201201_doublesize_C1_sigma_x, yerr=PKS_20201201_cropped_C1_sigma_x, linestyle='none', markersize=9, color='black')
graph2.plot(PKS_20201201_doublesize_C2_x, PKS_20201201_cropped_C2_x,'o', linestyle='none', markersize=5, color='blue', label='C7')
graph2.errorbar(PKS_20201201_doublesize_C2_x, PKS_20201201_cropped_C2_x, xerr=PKS_20201201_doublesize_C2_sigma_x, yerr=PKS_20201201_cropped_C2_sigma_x, linestyle='none', markersize=9, color='blue')
graph2.legend(loc='upper left', fontsize=6)
graph2.tick_params(axis="x", direction="in", labelsize=9)
graph2.tick_params(axis="y", direction="in", labelsize=9)
graph2.xaxis.set_ticks(np.arange(-3, 3, 1))
graph2.yaxis.set_ticks(np.arange(-3, 3, 1))
graph2.set_xlim(-3, 0)
graph2.set_ylim(-3, 0)

###############################################################################
TXS_20120206_doublesize_C1_x = -0.168
TXS_20120206_doublesize_C1_sigma_x = 0.098
TXS_20120206_doublesize_C2_x = -0.390
TXS_20120206_doublesize_C2_sigma_x = 0.093
TXS_20120206_doublesize_C3_x = 0.004
TXS_20120206_doublesize_C3_sigma_x = 0.152

TXS_20120206_cropped_C1_x = -0.172
TXS_20120206_cropped_C1_sigma_x = 0.087
TXS_20120206_cropped_C2_x = -0.393
TXS_20120206_cropped_C2_sigma_x = 0.088
TXS_20120206_cropped_C3_x = 0.003
TXS_20120206_cropped_C3_sigma_x = 0.124

graph3 = fig.add_subplot(6, 4, 3)
ponto_inicial = [10, -10]
ponto_final = [10, -10]
graph3.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
graph3.set_title('TXS 0506+056 \n 2012-02-06', fontsize=10, fontweight='bold')
#graph3.set_ylabel('x (mas)', fontsize=9, labelpad=-1, fontweight="bold")
graph3.set_xlabel('x', fontsize=9, fontweight="bold", labelpad=0)
graph3.plot(TXS_20120206_doublesize_C1_x, TXS_20120206_cropped_C1_x,  'o', linestyle='none', markersize=5, color='black', label='C4')
graph3.errorbar(TXS_20120206_doublesize_C1_x, TXS_20120206_cropped_C1_x, xerr=TXS_20120206_doublesize_C1_sigma_x, yerr=TXS_20120206_cropped_C1_sigma_x, linestyle='none', markersize=9, color='black')
graph3.plot(TXS_20120206_doublesize_C2_x, TXS_20120206_cropped_C2_x,'o', linestyle='none', markersize=5, color='blue', label='C2')
graph3.errorbar(TXS_20120206_doublesize_C2_x, TXS_20120206_cropped_C2_x, xerr=TXS_20120206_doublesize_C2_sigma_x, yerr=TXS_20120206_cropped_C2_sigma_x, linestyle='none', markersize=9, color='blue')
graph3.plot(TXS_20120206_doublesize_C3_x, TXS_20120206_cropped_C3_x,'o', linestyle='none', markersize=5, color='green', label='C3')
graph3.errorbar(TXS_20120206_doublesize_C3_x, TXS_20120206_cropped_C3_x, xerr=TXS_20120206_doublesize_C3_sigma_x, yerr=TXS_20120206_cropped_C3_sigma_x, linestyle='none', markersize=9, color='green')
graph3.legend(loc='upper left', fontsize=6)
graph3.tick_params(axis="x", direction="in", labelsize=9)
graph3.tick_params(axis="y", direction="in", labelsize=9)
graph3.xaxis.set_ticks(np.arange(-0.6, 0.301, 0.3))
graph3.yaxis.set_ticks(np.arange(-0.6, 0.301, 0.3))
graph3.set_xlim(-0.6, 0.3)
graph3.set_ylim(-0.6, 0.3)

############################################################################################################################################
TXS_20200409_doublesize_C1_x = 0.016
TXS_20200409_doublesize_C1_sigma_x = 0.117
TXS_20200409_doublesize_C2_x = -0.052
TXS_20200409_doublesize_C2_sigma_x = 0.119

TXS_20200409_cropped_C1_x = 0.015
TXS_20200409_cropped_C1_sigma_x = 0.117
TXS_20200409_cropped_C2_x = -0.054
TXS_20200409_cropped_C2_sigma_x = 0.119

graph4 = fig.add_subplot(6, 4, 4)
ponto_inicial = [10, -10]
ponto_final = [10, -10]
graph4.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
graph4.set_title('TXS 0506+056 \n 2020-04-09', fontsize=10, fontweight='bold')
#graph4.set_ylabel('x (mas)', fontsize=9, fontweight="bold", labelpad=-1)
graph4.set_xlabel('x', fontsize=9, fontweight="bold", labelpad=0)
graph4.plot(TXS_20200409_doublesize_C1_x, TXS_20200409_cropped_C1_x,  'o', linestyle='none', markersize=5, color='black', label='C12')
graph4.errorbar(TXS_20200409_doublesize_C1_x, TXS_20200409_cropped_C1_x, xerr=TXS_20200409_doublesize_C1_sigma_x, yerr=TXS_20200409_cropped_C1_sigma_x, linestyle='none', markersize=9, color='black')
graph4.plot(TXS_20200409_doublesize_C2_x, TXS_20200409_cropped_C2_x,'o', linestyle='none', markersize=5, color='blue', label='C11')
graph4.errorbar(TXS_20200409_doublesize_C2_x, TXS_20200409_cropped_C2_x, xerr=TXS_20200409_doublesize_C2_sigma_x, yerr=TXS_20200409_cropped_C2_sigma_x, linestyle='none', markersize=9, color='blue')
graph4.legend(loc='upper left', fontsize=6)
graph4.tick_params(axis="x", direction="in", labelsize=9)
graph4.tick_params(axis="y", direction="in", labelsize=9)
graph4.xaxis.set_ticks(np.arange(-0.6, 0.301, 0.3))
graph4.yaxis.set_ticks(np.arange(-0.6, 0.301, 0.3))
graph4.set_xlim(-0.6, 0.3)
graph4.set_ylim(-0.6, 0.3)


############################################################################
############### Parâmetro do CE: y #########################################
############################################################################

PKS_20161210_doublesize_C1_y = -0.466
PKS_20161210_doublesize_C1_sigma_y = 0.097
PKS_20161210_doublesize_C2_y = -1.421
PKS_20161210_doublesize_C2_sigma_y = 0.098
PKS_20161210_doublesize_C3_y = -2.272
PKS_20161210_doublesize_C3_sigma_y = 0.113

PKS_20161210_cropped_C1_y = -0.467
PKS_20161210_cropped_C1_sigma_y = 0.097
PKS_20161210_cropped_C2_y = -1.407
PKS_20161210_cropped_C2_sigma_y = 0.099
PKS_20161210_cropped_C3_y = -2.236
PKS_20161210_cropped_C3_sigma_y = 0.114


graph5 = fig.add_subplot(6, 4, 5)
ponto_inicial = [10, -10]
ponto_final = [10, -10]
graph5.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph5.set_title('y (mas)', fontsize=15, fontweight='bold')
graph5.set_ylabel('y', fontsize=9, fontweight="bold", labelpad=6)
graph5.set_xlabel('y', fontsize=9, fontweight="bold", labelpad=0)
graph5.plot(PKS_20161210_doublesize_C1_y, PKS_20161210_cropped_C1_y,  'o', linestyle='none', markersize=5, color='black',label='C3')
graph5.errorbar(PKS_20161210_doublesize_C1_y, PKS_20161210_cropped_C1_y, xerr=PKS_20161210_doublesize_C1_sigma_y, yerr=PKS_20161210_cropped_C1_sigma_y, linestyle='none', markersize=9, color='black')
graph5.plot(PKS_20161210_doublesize_C2_y, PKS_20161210_cropped_C2_y,'o', linestyle='none', markersize=5, color='blue',label='C2')
graph5.errorbar(PKS_20161210_doublesize_C2_y, PKS_20161210_cropped_C2_y, xerr=PKS_20161210_doublesize_C2_sigma_y, yerr=PKS_20161210_cropped_C2_sigma_y, linestyle='none', markersize=9, color='blue')
graph5.plot(PKS_20161210_doublesize_C3_y, PKS_20161210_cropped_C3_y,'o', linestyle='none', markersize=5, color='green',label='C1')
graph5.errorbar(PKS_20161210_doublesize_C3_y, PKS_20161210_cropped_C3_y, xerr=PKS_20161210_doublesize_C3_sigma_y, yerr=PKS_20161210_cropped_C3_sigma_y, linestyle='none', markersize=9, color='green')
graph5.legend(loc='upper left', fontsize=6)
graph5.tick_params(axis="x", direction="in", labelsize=9)
graph5.tick_params(axis="y", direction="in", labelsize=9)
graph5.xaxis.set_ticks(np.arange(-3, 0.001, 1))
graph5.yaxis.set_ticks(np.arange(-3, 0.001, 1))
graph5.set_xlim(-3, 0)
graph5.set_ylim(-3, 0)

##############################################################################################
PKS_20201201_doublesize_C1_y = -0.280
PKS_20201201_doublesize_C1_sigma_y = 0.083
PKS_20201201_doublesize_C2_y = -1.187
PKS_20201201_doublesize_C2_sigma_y = 0.086

PKS_20201201_cropped_C1_y = -0.319
PKS_20201201_cropped_C1_sigma_y = 0.086
PKS_20201201_cropped_C2_y = -1.249
PKS_20201201_cropped_C2_sigma_y = 0.086

graph6 = fig.add_subplot(6, 4, 6)
ponto_inicial = [10, -10]
ponto_final = [10, -10]
graph6.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph6.set_title('y (mas)', fontsize=15, fontweight='bold')
#graph6.set_ylabel('y (mas)', fontsize=9, fontweight="bold", labelpad=-1)
graph6.set_xlabel('y', fontsize=9, fontweight="bold", labelpad=0)
graph6.plot(PKS_20201201_doublesize_C1_y, PKS_20201201_cropped_C1_y,  'o', linestyle='none', markersize=5, color='black',label='U')
graph6.errorbar(PKS_20201201_doublesize_C1_y, PKS_20201201_cropped_C1_y, xerr=PKS_20201201_doublesize_C1_sigma_y, yerr=PKS_20201201_cropped_C1_sigma_y, linestyle='none', markersize=9, color='black')
graph6.plot(PKS_20201201_doublesize_C2_y, PKS_20201201_cropped_C2_y,'o', linestyle='none', markersize=5, color='blue',label='C7')
graph6.errorbar(PKS_20201201_doublesize_C2_y, PKS_20201201_cropped_C2_y, xerr=PKS_20201201_doublesize_C2_sigma_y, yerr=PKS_20201201_cropped_C2_sigma_y, linestyle='none', markersize=9, color='blue')
graph6.legend(loc='upper left', fontsize=6)
graph6.tick_params(axis="x", direction="in", labelsize=9)
graph6.tick_params(axis="y", direction="in", labelsize=9)
graph6.xaxis.set_ticks(np.arange(-3, 0.001, 1))
graph6.yaxis.set_ticks(np.arange(-3, 0.001, 1))
graph6.set_xlim(-3, 0)
graph6.set_ylim(-3, 0)

####################################################################################################
TXS_20120206_doublesize_C1_y = -0.635
TXS_20120206_doublesize_C1_sigma_y = 0.190
TXS_20120206_doublesize_C2_y = -1.518
TXS_20120206_doublesize_C2_sigma_y = 0.147
TXS_20120206_doublesize_C3_y = -2.657
TXS_20120206_doublesize_C3_sigma_y = 0.267

TXS_20120206_cropped_C1_y = -0.654
TXS_20120206_cropped_C1_sigma_y = 0.103
TXS_20120206_cropped_C2_y = -1.514
TXS_20120206_cropped_C2_sigma_y = 0.119
TXS_20120206_cropped_C3_y = -2.646
TXS_20120206_cropped_C3_sigma_y = 0.191

graph7 = fig.add_subplot(6, 4, 7)
ponto_inicial = [10, -10]
ponto_final = [10, -10]
graph7.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph7.set_title('y (mas)', fontsize=15, fontweight='bold')
#graph7.set_ylabel('y (mas)', fontsize=9, fontweight="bold", labelpad=-1)
graph7.set_xlabel('y', fontsize=9, fontweight="bold", labelpad=0)
graph7.plot(TXS_20120206_doublesize_C1_y, TXS_20120206_cropped_C1_y,  'o', linestyle='none', markersize=5, color='black',label='C4')
graph7.errorbar(TXS_20120206_doublesize_C1_y, TXS_20120206_cropped_C1_y, xerr=TXS_20120206_doublesize_C1_sigma_y, yerr=TXS_20120206_cropped_C1_sigma_y, linestyle='none', markersize=9, color='black')
graph7.plot(TXS_20120206_doublesize_C2_y, TXS_20120206_cropped_C2_y,'o', linestyle='none', markersize=5, color='blue',label='C3')
graph7.errorbar(TXS_20120206_doublesize_C2_y, TXS_20120206_cropped_C2_y, xerr=TXS_20120206_doublesize_C2_sigma_y, yerr=TXS_20120206_cropped_C2_sigma_y, linestyle='none', markersize=9, color='blue')
graph7.plot(TXS_20120206_doublesize_C3_y, TXS_20120206_cropped_C3_y,'o', linestyle='none', markersize=5, color='green',label='C2')
graph7.errorbar(TXS_20120206_doublesize_C3_y, TXS_20120206_cropped_C3_y, xerr=TXS_20120206_doublesize_C3_sigma_y, yerr=TXS_20120206_cropped_C3_sigma_y, linestyle='none', markersize=9, color='green')
graph7.legend(loc='upper left', fontsize=6)
graph7.tick_params(axis="x", direction="in", labelsize=9)
graph7.tick_params(axis="y", direction="in", labelsize=9)
graph7.xaxis.set_ticks(np.arange(-3, 0.001, 1))
graph7.yaxis.set_ticks(np.arange(-3, 0.001, 1))
graph7.set_xlim(-3, 0)
graph7.set_ylim(-3, 0)

###########################################################################################
TXS_20200409_doublesize_C1_y = -0.583
TXS_20200409_doublesize_C1_sigma_y = 0.140
TXS_20200409_doublesize_C2_y = -1.736
TXS_20200409_doublesize_C2_sigma_y = 0.150

TXS_20200409_cropped_C1_y = -0.589
TXS_20200409_cropped_C1_sigma_y = 0.139
TXS_20200409_cropped_C2_y = -1.754
TXS_20200409_cropped_C2_sigma_y = 0.137

graph8 = fig.add_subplot(6, 4, 8)
ponto_inicial = [-10, 10]
ponto_final = [-10, 10]
graph8.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph8.set_title('y (mas)', fontsize=15, fontweight='bold')
#graph8.set_ylabel('y (mas)', fontsize=9, fontweight="bold", labelpad=-1)
graph8.set_xlabel('y', fontsize=9, fontweight="bold", labelpad=0)
graph8.plot(TXS_20200409_doublesize_C1_y, TXS_20200409_cropped_C1_y,  'o', linestyle='none', markersize=5, color='black',label='C12')
graph8.errorbar(TXS_20200409_doublesize_C1_y, TXS_20200409_cropped_C1_y, xerr=TXS_20200409_doublesize_C1_sigma_y, yerr=TXS_20200409_cropped_C1_sigma_y, linestyle='none', markersize=9, color='black')
graph8.plot(TXS_20200409_doublesize_C2_y, TXS_20200409_cropped_C2_y,'o', linestyle='none', markersize=5, color='blue',label='C11')
graph8.errorbar(TXS_20200409_doublesize_C2_y, TXS_20200409_cropped_C2_y, xerr=TXS_20200409_doublesize_C2_sigma_y, yerr=TXS_20200409_cropped_C2_sigma_y, linestyle='none', markersize=9, color='blue')
graph8.legend(loc='upper left', fontsize=6)
graph8.tick_params(axis="x", direction="in", labelsize=9)
graph8.tick_params(axis="y", direction="in", labelsize=9)
graph8.xaxis.set_ticks(np.arange(-3, 0.001, 1))
graph8.yaxis.set_ticks(np.arange(-3, 0.001, 1))
graph8.set_xlim(-3, 0)
graph8.set_ylim(-3, 0)


############################################################################
############### Parâmetro do CE: a_fwhm ####################################
############################################################################

PKS_20161210_doublesize_core_a = 0.045
PKS_20161210_doublesize_core_sigma_a = 0.002
PKS_20161210_doublesize_C1_a = 0.123
PKS_20161210_doublesize_C1_sigma_a = 0.006
PKS_20161210_doublesize_C2_a = 0.205
PKS_20161210_doublesize_C2_sigma_a = 0.015
PKS_20161210_doublesize_C3_a = 0.306
PKS_20161210_doublesize_C3_sigma_a = 0.046

PKS_20161210_cropped_core_a = 0.045
PKS_20161210_cropped_core_sigma_a = 0.002
PKS_20161210_cropped_C1_a = 0.123
PKS_20161210_cropped_C1_sigma_a = 0.005
PKS_20161210_cropped_C2_a = 0.200
PKS_20161210_cropped_C2_sigma_a = 0.018
PKS_20161210_cropped_C3_a = 0.328
PKS_20161210_cropped_C3_sigma_a = 0.036

graph9 = fig.add_subplot(6, 4, 9)
ponto_inicial = [-10, 10]
ponto_final = [-10, 10]
graph9.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph9.set_title('a', fontsize=15, fontweight='bold')
graph9.set_ylabel('Semi-major axis', fontsize=9, fontweight="bold", labelpad=6)
graph9.set_xlabel('Semi-major axis', fontsize=9, fontweight="bold", labelpad=0)
graph9.plot(PKS_20161210_doublesize_core_a, PKS_20161210_cropped_core_a,  'o', linestyle='none', markersize=5, color='red',label='Core')
graph9.errorbar(PKS_20161210_doublesize_core_a, PKS_20161210_cropped_core_a, xerr=PKS_20161210_doublesize_core_sigma_a, yerr=PKS_20161210_cropped_core_sigma_a, linestyle='none', markersize=9, color='red')
graph9.plot(PKS_20161210_doublesize_C1_a, PKS_20161210_cropped_C1_a,  'o', linestyle='none', markersize=5, color='black',label='C3')
graph9.errorbar(PKS_20161210_doublesize_C1_a, PKS_20161210_cropped_C1_a, xerr=PKS_20161210_doublesize_C1_sigma_a, yerr=PKS_20161210_cropped_C1_sigma_a, linestyle='none', markersize=9, color='black')
graph9.plot(PKS_20161210_doublesize_C2_a, PKS_20161210_cropped_C2_a,'o', linestyle='none', markersize=5, color='blue',label='C2')
graph9.errorbar(PKS_20161210_doublesize_C2_a, PKS_20161210_cropped_C2_a, xerr=PKS_20161210_doublesize_C2_sigma_a, yerr=PKS_20161210_cropped_C2_sigma_a, linestyle='none', markersize=9, color='blue')
graph9.plot(PKS_20161210_doublesize_C3_a, PKS_20161210_cropped_C3_a,'o', linestyle='none', markersize=5, color='green',label='C1')
graph9.errorbar(PKS_20161210_doublesize_C3_a, PKS_20161210_cropped_C3_a, xerr=PKS_20161210_doublesize_C3_sigma_a, yerr=PKS_20161210_cropped_C3_sigma_a, linestyle='none', markersize=9, color='green')
graph9.legend(loc='upper left', fontsize=6)
graph9.tick_params(axis="x", direction="in", labelsize=9)
graph9.tick_params(axis="y", direction="in", labelsize=9)
graph9.xaxis.set_ticks(np.arange(0, 0.4001, 0.2))
graph9.yaxis.set_ticks(np.arange(0, 0.4001, 0.2))
graph9.set_xlim(0.0, 0.4)
graph9.set_ylim(0.0, 0.4)

#########################################################################################################
PKS_20201201_doublesize_core_a = 0.057
PKS_20201201_doublesize_core_sigma_a = 0.006
PKS_20201201_doublesize_C1_a = 0.323
PKS_20201201_doublesize_C1_sigma_a = 0.003
PKS_20201201_doublesize_C2_a = 0.353
PKS_20201201_doublesize_C2_sigma_a = 0.018

PKS_20201201_cropped_core_a = 0.066
PKS_20201201_cropped_core_sigma_a = 0.002
PKS_20201201_cropped_C1_a = 0.322
PKS_20201201_cropped_C1_sigma_a = 0.020
PKS_20201201_cropped_C2_a = 0.325
PKS_20201201_cropped_C2_sigma_a = 0.013

graph10 = fig.add_subplot(6, 4, 10)
ponto_inicial = [-10, 10]
ponto_final = [-10, 10]
graph10.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph10.set_title('a', fontsize=15, fontweight='bold')
#graph10.set_ylabel('Semi-major axis', fontsize=9, fontweight="bold", labelpad=-1)
graph10.set_xlabel('Semi-major axis', fontsize=9, fontweight="bold", labelpad=0)
graph10.plot(PKS_20201201_doublesize_core_a, PKS_20201201_cropped_core_a,  'o', linestyle='none', markersize=5, color='red',label='Core')
graph10.errorbar(PKS_20201201_doublesize_core_a, PKS_20201201_cropped_core_a, xerr=PKS_20201201_doublesize_core_sigma_a, yerr=PKS_20201201_cropped_core_sigma_a, linestyle='none', markersize=9, color='red')
graph10.plot(PKS_20201201_doublesize_C1_a, PKS_20201201_cropped_C1_a,  'o', linestyle='none', markersize=5, color='black',label='U')
graph10.errorbar(PKS_20201201_doublesize_C1_a, PKS_20201201_cropped_C1_a, xerr=PKS_20201201_doublesize_C1_sigma_a, yerr=PKS_20201201_cropped_C1_sigma_a, linestyle='none', markersize=9, color='black')
graph10.plot(PKS_20201201_doublesize_C2_a, PKS_20201201_cropped_C2_a,'o', linestyle='none', markersize=5, color='blue',label='C7')
graph10.errorbar(PKS_20201201_doublesize_C2_a, PKS_20201201_cropped_C2_a, xerr=PKS_20201201_doublesize_C2_sigma_a, yerr=PKS_20201201_cropped_C2_sigma_a, linestyle='none', markersize=9, color='blue')
graph10.legend(loc='upper left', fontsize=6)
graph10.tick_params(axis="x", direction="in", labelsize=9)
graph10.tick_params(axis="y", direction="in", labelsize=9)
graph10.xaxis.set_ticks(np.arange(0, 0.4001, 0.2))
graph10.yaxis.set_ticks(np.arange(0, 0.4001, 0.2))
graph10.set_xlim(0.0, 0.4)
graph10.set_ylim(0.0, 0.4)

########################################################################################################
TXS_20120206_doublesize_core_a = 0.012
TXS_20120206_doublesize_core_sigma_a = 0.018
TXS_20120206_doublesize_C1_a = 0.105
TXS_20120206_doublesize_C1_sigma_a = 0.055
TXS_20120206_doublesize_C2_a = 0.407
TXS_20120206_doublesize_C2_sigma_a = 0.042
TXS_20120206_doublesize_C3_a = 0.580
TXS_20120206_doublesize_C3_sigma_a = 0.043

TXS_20120206_cropped_core_a = 0.016
TXS_20120206_cropped_core_sigma_a = 0.013
TXS_20120206_cropped_C1_a = 0.102
TXS_20120206_cropped_C1_sigma_a = 0.038
TXS_20120206_cropped_C2_a = 0.403
TXS_20120206_cropped_C2_sigma_a = 0.023
TXS_20120206_cropped_C3_a = 0.580
TXS_20120206_cropped_C3_sigma_a = 0.026

graph11 = fig.add_subplot(6, 4, 11)
ponto_inicial = [-10, 10]
ponto_final = [-10, 10]
graph11.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph11.set_title('a', fontsize=15, fontweight='bold')
#graph11.set_ylabel('Semi-major axis', fontsize=9, fontweight="bold", labelpad=-1)
graph11.set_xlabel('Semi-major axis', fontsize=9, fontweight="bold", labelpad=0)
graph11.plot(TXS_20120206_doublesize_core_a, TXS_20120206_cropped_core_a,  'o', linestyle='none', markersize=5, color='red',label='Core')
graph11.errorbar(TXS_20120206_doublesize_core_a, TXS_20120206_cropped_core_a, xerr=TXS_20120206_doublesize_core_sigma_a, yerr=TXS_20120206_cropped_core_sigma_a, linestyle='none', markersize=9, color='red')
graph11.plot(TXS_20120206_doublesize_C1_a, TXS_20120206_cropped_C1_a,  'o', linestyle='none', markersize=5, color='black',label='C4')
graph11.errorbar(TXS_20120206_doublesize_C1_a, TXS_20120206_cropped_C1_a, xerr=TXS_20120206_doublesize_C1_sigma_a, yerr=TXS_20120206_cropped_C1_sigma_a, linestyle='none', markersize=9, color='black')
graph11.plot(TXS_20120206_doublesize_C2_a, TXS_20120206_cropped_C2_a,'o', linestyle='none', markersize=5, color='blue',label='C3')
graph11.errorbar(TXS_20120206_doublesize_C2_a, TXS_20120206_cropped_C2_a, xerr=TXS_20120206_doublesize_C2_sigma_a, yerr=TXS_20120206_cropped_C2_sigma_a, linestyle='none', markersize=9, color='blue')
graph11.plot(TXS_20120206_doublesize_C3_a, TXS_20120206_cropped_C3_a,'o', linestyle='none', markersize=5, color='green',label='C2')
graph11.errorbar(TXS_20120206_doublesize_C3_a, TXS_20120206_cropped_C3_a, xerr=TXS_20120206_doublesize_C3_sigma_a, yerr=TXS_20120206_cropped_C3_sigma_a, linestyle='none', markersize=9, color='green')
graph11.legend(loc='upper left', fontsize=6)
graph11.tick_params(axis="x", direction="in", labelsize=9)
graph11.tick_params(axis="y", direction="in", labelsize=9)
graph11.xaxis.set_ticks(np.arange(0, 0.751, 0.25))
graph11.yaxis.set_ticks(np.arange(0, 0.751, 0.25))
graph11.set_xlim(0.0, 0.75)
graph11.set_ylim(0.0, 0.75)

########################################################################################################
TXS_20200409_doublesize_core_a = 0.058
TXS_20200409_doublesize_core_sigma_a = 0.007
TXS_20200409_doublesize_C1_a = 0.192
TXS_20200409_doublesize_C1_sigma_a = 0.034
TXS_20200409_doublesize_C2_a = 0.549
TXS_20200409_doublesize_C2_sigma_a = 0.038

TXS_20200409_cropped_core_a = 0.058
TXS_20200409_cropped_core_sigma_a = 0.007
TXS_20200409_cropped_C1_a = 0.198
TXS_20200409_cropped_C1_sigma_a = 0.036
TXS_20200409_cropped_C2_a = 0.561
TXS_20200409_cropped_C2_sigma_a = 0.033

graph12 = fig.add_subplot(6, 4, 12)
ponto_inicial = [-10, 10]
ponto_final = [-10, 10]
graph12.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph12.set_title('a', fontsize=15, fontweight='bold')
#graph12.set_ylabel('Semi-major axis', fontsize=9, fontweight="bold", labelpad=-1)
graph12.set_xlabel('Semi-major axis', fontsize=9, fontweight="bold", labelpad=0)
graph12.plot(TXS_20200409_doublesize_core_a, TXS_20200409_cropped_core_a,  'o', linestyle='none', markersize=5, color='red',label='Core')
graph12.errorbar(TXS_20200409_doublesize_core_a, TXS_20200409_cropped_core_a, xerr=TXS_20200409_doublesize_core_sigma_a, yerr=TXS_20200409_cropped_core_sigma_a, linestyle='none', markersize=9, color='red')
graph12.plot(TXS_20200409_doublesize_C1_a, TXS_20200409_cropped_C1_a,  'o', linestyle='none', markersize=5, color='black',label='C12')
graph12.errorbar(TXS_20200409_doublesize_C1_a, TXS_20200409_cropped_C1_a, xerr=TXS_20200409_doublesize_C1_sigma_a, yerr=TXS_20200409_cropped_C1_sigma_a, linestyle='none', markersize=9, color='black')
graph12.plot(TXS_20200409_doublesize_C2_a, TXS_20200409_cropped_C2_a,'o', linestyle='none', markersize=5, color='blue',label='C11')
graph12.errorbar(TXS_20200409_doublesize_C2_a, TXS_20200409_cropped_C2_a, xerr=TXS_20200409_doublesize_C2_sigma_a, yerr=TXS_20200409_cropped_C2_sigma_a, linestyle='none', markersize=9, color='blue')
graph12.legend(loc='upper left', fontsize=6)
graph12.tick_params(axis="x", direction="in", labelsize=9)
graph12.tick_params(axis="y", direction="in", labelsize=9)
graph12.xaxis.set_ticks(np.arange(0, 0.751, 0.25))
graph12.yaxis.set_ticks(np.arange(0, 0.751, 0.25))
graph12.set_xlim(0.0, 0.75)
graph12.set_ylim(0.0, 0.75)

############################################################################
############### Parâmetro do CE: epsilon ###################################
############################################################################

PKS_20161210_doublesize_core_e = 0.117
PKS_20161210_doublesize_core_sigma_e = 0.312
PKS_20161210_doublesize_C1_e = 0.066
PKS_20161210_doublesize_C1_sigma_e = 0.170
PKS_20161210_doublesize_C2_e = 0.113
PKS_20161210_doublesize_C2_sigma_e = 0.237
PKS_20161210_doublesize_C3_e = 0.312
PKS_20161210_doublesize_C3_sigma_e = 0.523

PKS_20161210_cropped_core_e = 0.075
PKS_20161210_cropped_core_sigma_e = 0.223
PKS_20161210_cropped_C1_e = 0.051
PKS_20161210_cropped_C1_sigma_e = 0.149
PKS_20161210_cropped_C2_e = 0.113
PKS_20161210_cropped_C2_sigma_e = 0.295
PKS_20161210_cropped_C3_e = 0.493
PKS_20161210_cropped_C3_sigma_e = 0.051

graph13 = fig.add_subplot(6, 4, 13)
ponto_inicial = [10, -10]
ponto_final = [10, -10]
graph13.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph13.set_title('$\epsilon$', fontsize=15, fontweight='bold')
graph13.set_ylabel('Eccentricity', fontsize=9, fontweight="bold", labelpad=7)
graph13.set_xlabel('Eccentricity', fontsize=9, fontweight="bold", labelpad=0)
#graph13.set_xlabel('Double size image', fontsize=12, labelpad=12, fontweight="bold")
graph13.plot(PKS_20161210_doublesize_core_e, PKS_20161210_cropped_core_e,  'o', linestyle='none', markersize=5, color='red',label='Core')
graph13.errorbar(PKS_20161210_doublesize_core_e, PKS_20161210_cropped_core_e, xerr=PKS_20161210_doublesize_core_sigma_e, yerr=PKS_20161210_cropped_core_sigma_e, linestyle='none', markersize=9, color='red')
graph13.plot(PKS_20161210_doublesize_C1_e, PKS_20161210_cropped_C1_e,  'o', linestyle='none', markersize=5, color='black',label='C3')
graph13.errorbar(PKS_20161210_doublesize_C1_e, PKS_20161210_cropped_C1_e, xerr=PKS_20161210_doublesize_C1_sigma_e, yerr=PKS_20161210_cropped_C1_sigma_e, linestyle='none', markersize=9, color='black')
graph13.plot(PKS_20161210_doublesize_C2_e, PKS_20161210_cropped_C2_e,'o', linestyle='none', markersize=5, color='blue',label='C2')
graph13.errorbar(PKS_20161210_doublesize_C2_e, PKS_20161210_cropped_C2_e, xerr=PKS_20161210_doublesize_C2_sigma_e, yerr=PKS_20161210_cropped_C2_sigma_e, linestyle='none', markersize=9, color='blue')
graph13.plot(PKS_20161210_doublesize_C3_e, PKS_20161210_cropped_C3_e,'o', linestyle='none', markersize=5, color='green',label='C1')
graph13.errorbar(PKS_20161210_doublesize_C3_e, PKS_20161210_cropped_C3_e, xerr=PKS_20161210_doublesize_C3_sigma_e, yerr=PKS_20161210_cropped_C3_sigma_e, linestyle='none', markersize=9, color='green')
graph13.legend(loc='lower right', fontsize=6)
graph13.tick_params(axis="x", direction="in", labelsize=9)
graph13.tick_params(axis="y", direction="in", labelsize=9)
graph13.xaxis.set_ticks(np.arange(0.0, 0.901, 0.3))
graph13.yaxis.set_ticks(np.arange(0.0, 0.901, 0.3))
graph13.set_xlim(0.0, 0.9)
graph13.set_ylim(0.0, 0.9)

#########################################################################################################
PKS_20201201_doublesize_core_e = 0.469
PKS_20201201_doublesize_core_sigma_e = 0.322
PKS_20201201_doublesize_C1_e = 0.496
PKS_20201201_doublesize_C1_sigma_e = 0.065
PKS_20201201_doublesize_C2_e = 0.020
PKS_20201201_doublesize_C2_sigma_e = 0.105

PKS_20201201_cropped_core_e = 0.481
PKS_20201201_cropped_core_sigma_e = 0.109
PKS_20201201_cropped_C1_e = 0.498
PKS_20201201_cropped_C1_sigma_e = 0.029
PKS_20201201_cropped_C2_e = 0.020
PKS_20201201_cropped_C2_sigma_e = 0.080

graph14 = fig.add_subplot(6, 4, 14)
ponto_inicial = [-10, 10]
ponto_final = [-10, 10]
graph14.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph14.set_title('$\epsilon$', fontsize=15, fontweight='bold')
#graph14.set_ylabel('Eccentricity', fontsize=9, fontweight="bold", labelpad=-1)
graph14.set_xlabel('Eccentricity', fontsize=9, fontweight="bold", labelpad=0)
graph14.plot(PKS_20201201_doublesize_core_e, PKS_20201201_cropped_core_e, 'o', linestyle='none', markersize=5, color='red',label='Core')
graph14.errorbar(PKS_20201201_doublesize_core_e, PKS_20201201_cropped_core_e, xerr=PKS_20201201_doublesize_core_sigma_e, yerr=PKS_20201201_cropped_core_sigma_e, linestyle='none', markersize=9, color='red')
graph14.plot(PKS_20201201_doublesize_C1_e, PKS_20201201_cropped_C1_e, 'o', linestyle='none', markersize=5, color='black',label='U')
graph14.errorbar(PKS_20201201_doublesize_C1_e, PKS_20201201_cropped_C1_e, xerr=PKS_20201201_doublesize_C1_sigma_e, yerr=PKS_20201201_cropped_C1_sigma_e, linestyle='none', markersize=9, color='black')
graph14.plot(PKS_20201201_doublesize_C2_e, PKS_20201201_cropped_C2_e, 'o', linestyle='none', markersize=5, color='blue',label='C7')
graph14.errorbar(PKS_20201201_doublesize_C2_e, PKS_20201201_cropped_C2_e, xerr=PKS_20201201_doublesize_C2_sigma_e, yerr=PKS_20201201_cropped_C2_sigma_e, linestyle='none', markersize=9, color='blue')
graph14.legend(loc='lower right', fontsize=6)
graph14.tick_params(axis="x", direction="in", labelsize=9)
graph14.tick_params(axis="y", direction="in", labelsize=9)
graph14.xaxis.set_ticks(np.arange(0.0, 0.901, 0.3))
graph14.yaxis.set_ticks(np.arange(0.0, 0.901, 0.3))
graph14.set_xlim(0.0, 0.9)
graph14.set_ylim(0.0, 0.9)

########################################################################################################
TXS_20120206_doublesize_core_e = 0.392
TXS_20120206_doublesize_core_sigma_e = 0.428
TXS_20120206_doublesize_C1_e = 0.458
TXS_20120206_doublesize_C1_sigma_e = 0.300
TXS_20120206_doublesize_C2_e = 0.500
TXS_20120206_doublesize_C2_sigma_e = 0.007
TXS_20120206_doublesize_C3_e = 0.498
TXS_20120206_doublesize_C3_sigma_e = 0.028

TXS_20120206_cropped_core_e = 0.454
TXS_20120206_cropped_core_sigma_e = 0.321
TXS_20120206_cropped_C1_e = 0.489
TXS_20120206_cropped_C1_sigma_e = 0.079
TXS_20120206_cropped_C2_e = 0.500
TXS_20120206_cropped_C2_sigma_e = 0.004
TXS_20120206_cropped_C3_e = 0.499
TXS_20120206_cropped_C3_sigma_e = 0.037

graph15 = fig.add_subplot(6, 4, 15)
ponto_inicial = [-10, 10]
ponto_final = [-10, 10]
graph15.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph15.set_title('$\epsilon$', fontsize=15, fontweight='bold')
#graph15.set_ylabel('Eccentricity', fontsize=9, fontweight="bold", labelpad=-1)
graph15.set_xlabel('Eccentricity', fontsize=9, fontweight="bold", labelpad=0)
graph15.plot(TXS_20120206_doublesize_core_e, TXS_20120206_cropped_core_e,  'o', linestyle='none', markersize=5, color='red',label='Core')
graph15.errorbar(TXS_20120206_doublesize_core_e, TXS_20120206_cropped_core_e, xerr=TXS_20120206_doublesize_core_sigma_e, yerr=TXS_20120206_cropped_core_sigma_e, linestyle='none', markersize=9, color='red')
graph15.plot(TXS_20120206_doublesize_C1_e, TXS_20120206_cropped_C1_e, 'o', linestyle='none', markersize=5, color='black',label='C4')
graph15.errorbar(TXS_20120206_doublesize_C1_e, TXS_20120206_cropped_C1_e, xerr=TXS_20120206_doublesize_C1_sigma_e, yerr=TXS_20120206_cropped_C1_sigma_e, linestyle='none', markersize=9, color='black')
graph15.plot(TXS_20120206_doublesize_C2_e, TXS_20120206_cropped_C2_e, 'o', linestyle='none', markersize=7, color='blue',label='C3')
graph15.errorbar(TXS_20120206_doublesize_C2_e, TXS_20120206_cropped_C2_e, xerr=TXS_20120206_doublesize_C2_sigma_e, yerr=TXS_20120206_cropped_C2_sigma_e, linestyle='none', markersize=9, color='blue')
graph15.plot(TXS_20120206_doublesize_C3_e, TXS_20120206_cropped_C3_e, 'o', linestyle='none', markersize=4.5, color='green',label='C2')
graph15.errorbar(TXS_20120206_doublesize_C3_e, TXS_20120206_cropped_C3_e, xerr=TXS_20120206_doublesize_C3_sigma_e, yerr=TXS_20120206_cropped_C3_sigma_e, linestyle='none', markersize=9, color='green')
graph15.legend(loc='upper left', fontsize=6)
graph15.tick_params(axis="x", direction="in", labelsize=9)
graph15.tick_params(axis="y", direction="in", labelsize=9)
graph15.xaxis.set_ticks(np.arange(0.0, 0.901, 0.3))
graph15.yaxis.set_ticks(np.arange(0.0, 0.901, 0.3))
graph15.set_xlim(0.0, 0.9)
graph15.set_ylim(0.0, 0.9)

########################################################################################################
TXS_20200409_doublesize_core_e = 0.498
TXS_20200409_doublesize_core_sigma_e = 0.016
TXS_20200409_doublesize_C1_e = 0.226
TXS_20200409_doublesize_C1_sigma_e = 0.634
TXS_20200409_doublesize_C2_e = 0.498
TXS_20200409_doublesize_C2_sigma_e = 0.031

TXS_20200409_cropped_core_e = 0.499
TXS_20200409_cropped_core_sigma_e = 0.010
TXS_20200409_cropped_C1_e = 0.300
TXS_20200409_cropped_C1_sigma_e = 0.653
TXS_20200409_cropped_C2_e = 0.499
TXS_20200409_cropped_C2_sigma_e = 0.029

graph16 = fig.add_subplot(6, 4, 16)
ponto_inicial = [-10, 10]
ponto_final = [-10, 10]
graph16.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph16.set_title('$\epsilon$', fontsize=15, fontweight='bold')
#graph16.set_ylabel('Eccentricity', fontsize=9, fontweight="bold", labelpad=-1)
graph16.set_xlabel('Eccentricity', fontsize=9, fontweight="bold", labelpad=0)
graph16.plot(TXS_20200409_doublesize_core_e, TXS_20200409_cropped_core_e,  'o', linestyle='none', markersize=7, color='red',label='Core')
graph16.errorbar(TXS_20200409_doublesize_core_e, TXS_20200409_cropped_core_e, xerr=TXS_20200409_doublesize_core_sigma_e, yerr=TXS_20200409_cropped_core_sigma_e, linestyle='none', markersize=9, color='red')
graph16.plot(TXS_20200409_doublesize_C1_e, TXS_20200409_cropped_C1_e,  'o', linestyle='none', markersize=5, color='black',label='C12')
graph16.errorbar(TXS_20200409_doublesize_C1_e, TXS_20200409_cropped_C1_e, xerr=TXS_20200409_doublesize_C1_sigma_e, yerr=TXS_20200409_cropped_C1_sigma_e, linestyle='none', markersize=9, color='black')
graph16.plot(TXS_20200409_doublesize_C2_e, TXS_20200409_cropped_C2_e,'o', linestyle='none', markersize=4.5, color='blue',label='C11')
graph16.errorbar(TXS_20200409_doublesize_C2_e, TXS_20200409_cropped_C2_e, xerr=TXS_20200409_doublesize_C2_sigma_e, yerr=TXS_20200409_cropped_C2_sigma_e, linestyle='none', markersize=9, color='blue')
graph16.legend(loc='upper right', fontsize=6)
graph16.tick_params(axis="x", direction="in", labelsize=9)
graph16.tick_params(axis="y", direction="in", labelsize=9)
graph16.xaxis.set_ticks(np.arange(0.0, 0.901, 0.3))
graph16.yaxis.set_ticks(np.arange(0.0, 0.901, 0.3))
graph16.set_xlim(0.0, 0.9)
graph16.set_ylim(0.0, 0.9)

############################################################################
############### Parâmetro do CE: psi #######################################
############################################################################

PKS_20161210_doublesize_core_psi = -32.667
PKS_20161210_doublesize_core_sigma_psi = 0.017
PKS_20161210_doublesize_C1_psi = -58.254
PKS_20161210_doublesize_C1_sigma_psi = 39.404
PKS_20161210_doublesize_C2_psi = -29.641
PKS_20161210_doublesize_C2_sigma_psi = 0.919
PKS_20161210_doublesize_C3_psi = -67.993  
PKS_20161210_doublesize_C3_sigma_psi = 22.273

PKS_20161210_cropped_core_psi = -32.667
PKS_20161210_cropped_core_sigma_psi = 0.017
PKS_20161210_cropped_C1_psi = -59.090
PKS_20161210_cropped_C1_sigma_psi = 37.043
PKS_20161210_cropped_C2_psi = -30.469
PKS_20161210_cropped_C2_sigma_psi = 13.595
PKS_20161210_cropped_C3_psi = -54.049
PKS_20161210_cropped_C3_sigma_psi = 14.534

graph17 = fig.add_subplot(6, 4, 17)
ponto_inicial = [-120, 100]
ponto_final = [-120, 100]
graph17.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph17.set_title('$\psi$', fontsize=15, fontweight='bold')
graph17.set_ylabel('Position angle', fontsize=9, fontweight="bold", labelpad=-2)
graph17.set_xlabel('Position angle', fontsize=9, fontweight="bold", labelpad=0)
graph17.plot(PKS_20161210_doublesize_core_psi, PKS_20161210_cropped_core_psi,  'o', linestyle='none', markersize=5, color='red',label='Core')
graph17.errorbar(PKS_20161210_doublesize_core_psi, PKS_20161210_cropped_core_psi, xerr=PKS_20161210_doublesize_core_sigma_psi, yerr=PKS_20161210_cropped_core_sigma_psi, linestyle='none', markersize=9, color='red')
graph17.plot(PKS_20161210_doublesize_C1_psi, PKS_20161210_cropped_C1_psi,  'o', linestyle='none', markersize=5, color='black',label='C3')
graph17.errorbar(PKS_20161210_doublesize_C1_psi, PKS_20161210_cropped_C1_psi, xerr=PKS_20161210_doublesize_C1_sigma_psi, yerr=PKS_20161210_cropped_C1_sigma_psi, linestyle='none', markersize=9, color='black')
graph17.plot(PKS_20161210_doublesize_C2_psi, PKS_20161210_cropped_C2_psi,'o', linestyle='none', markersize=5, color='blue',label='C2')
graph17.errorbar(PKS_20161210_doublesize_C2_psi, PKS_20161210_cropped_C2_psi, xerr=PKS_20161210_doublesize_C2_sigma_psi, yerr=PKS_20161210_cropped_C2_sigma_psi, linestyle='none', markersize=9, color='blue')
graph17.plot(PKS_20161210_doublesize_C3_psi, PKS_20161210_cropped_C3_psi,'o', linestyle='none', markersize=5, color='green',label='C1')
graph17.errorbar(PKS_20161210_doublesize_C3_psi, PKS_20161210_cropped_C3_psi, xerr=PKS_20161210_doublesize_C3_sigma_psi, yerr=PKS_20161210_cropped_C3_sigma_psi, linestyle='none', markersize=9, color='green')
graph17.legend(loc='lower right', fontsize=6)
graph17.tick_params(axis="x", direction="in", labelsize=9)
graph17.tick_params(axis="y", direction="in", labelsize=9)
graph17.xaxis.set_ticks(np.arange(-100, -9.99, 30))
graph17.yaxis.set_ticks(np.arange(-100, -9.99, 30))
graph17.set_xlim(-100, -10)
graph17.set_ylim(-100, -10)

#########################################################################################################
PKS_20201201_doublesize_core_psi = -58.521 
PKS_20201201_doublesize_core_sigma_psi = 6.838
PKS_20201201_doublesize_C1_psi = -35.292
PKS_20201201_doublesize_C1_sigma_psi = 0.427
PKS_20201201_doublesize_C2_psi = -36.537
PKS_20201201_doublesize_C2_sigma_psi = 1.820

PKS_20201201_cropped_core_psi = -50.287
PKS_20201201_cropped_core_sigma_psi = 0.046
PKS_20201201_cropped_C1_psi = -36.476
PKS_20201201_cropped_C1_sigma_psi = 1.863
PKS_20201201_cropped_C2_psi = -38.127
PKS_20201201_cropped_C2_sigma_psi = 1.006

graph18 = fig.add_subplot(6, 4, 18)
ponto_inicial = [-100, 100]
ponto_final = [-100, 100]
graph18.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph18.set_title('$\psi$', fontsize=15, fontweight='bold')
#graph18.set_ylabel('Position angle', fontsize=9, fontweight="bold", labelpad=-1)
graph18.set_xlabel('Position angle', fontsize=9, fontweight="bold", labelpad=0)
graph18.plot(PKS_20201201_doublesize_core_psi, PKS_20201201_cropped_core_psi, 'o', linestyle='none', markersize=5, color='red',label='Core')
graph18.errorbar(PKS_20201201_doublesize_core_psi, PKS_20201201_cropped_core_psi, xerr=PKS_20201201_doublesize_core_sigma_psi, yerr=PKS_20201201_cropped_core_sigma_psi, linestyle='none', markersize=9, color='red')
graph18.plot(PKS_20201201_doublesize_C1_psi, PKS_20201201_cropped_C1_psi, 'o', linestyle='none', markersize=5, color='black',label='U')
graph18.errorbar(PKS_20201201_doublesize_C1_psi, PKS_20201201_cropped_C1_psi, xerr=PKS_20201201_doublesize_C1_sigma_psi, yerr=PKS_20201201_cropped_C1_sigma_psi, linestyle='none', markersize=9, color='black')
graph18.plot(PKS_20201201_doublesize_C2_psi, PKS_20201201_cropped_C2_psi, 'o', linestyle='none', markersize=5, color='blue',label='C7')
graph18.errorbar(PKS_20201201_doublesize_C2_psi, PKS_20201201_cropped_C2_psi, xerr=PKS_20201201_doublesize_C2_sigma_psi, yerr=PKS_20201201_cropped_C2_sigma_psi, linestyle='none', markersize=9, color='blue')
graph18.legend(loc='upper left', fontsize=6)
graph18.tick_params(axis="x", direction="in", labelsize=9)
graph18.tick_params(axis="y", direction="in", labelsize=9)
graph18.xaxis.set_ticks(np.arange(-100, -9.99, 30))
graph18.yaxis.set_ticks(np.arange(-100, -9.99, 30))
graph18.set_xlim(-100, -10)
graph18.set_ylim(-100, -10)

########################################################################################################
TXS_20120206_doublesize_core_psi = 81.917
TXS_20120206_doublesize_core_sigma_psi = 31.965
TXS_20120206_doublesize_C1_psi = 35.183
TXS_20120206_doublesize_C1_sigma_psi = 23.808
TXS_20120206_doublesize_C2_psi = 74.081
TXS_20120206_doublesize_C2_sigma_psi = 5.702
TXS_20120206_doublesize_C3_psi = 53.941
TXS_20120206_doublesize_C3_sigma_psi = 9.035

TXS_20120206_cropped_core_psi = 87.768
TXS_20120206_cropped_core_sigma_psi = 16.988
TXS_20120206_cropped_C1_psi = 33.065
TXS_20120206_cropped_C1_sigma_psi = 6.379
TXS_20120206_cropped_C2_psi = 73.790
TXS_20120206_cropped_C2_sigma_psi = 3.730
TXS_20120206_cropped_C3_psi = 54.099
TXS_20120206_cropped_C3_sigma_psi = 6.771

graph19 = fig.add_subplot(6, 4, 19)
ponto_inicial = [-200, 200]
ponto_final = [-200, 200]
graph19.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph19.set_title('$\psi$', fontsize=15, fontweight='bold')
#graph19.set_ylabel('Position angle', fontsize=9, fontweight="bold", labelpad=-1)
graph19.set_xlabel('Position angle', fontsize=9, fontweight="bold", labelpad=0)
graph19.plot(TXS_20120206_doublesize_core_psi, TXS_20120206_cropped_core_psi,  'o', linestyle='none', markersize=5, color='red',label='Core')
graph19.errorbar(TXS_20120206_doublesize_core_psi, TXS_20120206_cropped_core_psi, xerr=TXS_20120206_doublesize_core_sigma_psi, yerr=TXS_20120206_cropped_core_sigma_psi, linestyle='none', markersize=9, color='red')
graph19.plot(TXS_20120206_doublesize_C1_psi, TXS_20120206_cropped_C1_psi,  'o', linestyle='none', markersize=5, color='black',label='C4')
graph19.errorbar(TXS_20120206_doublesize_C1_psi, TXS_20120206_cropped_C1_psi, xerr=TXS_20120206_doublesize_C1_sigma_psi, yerr=TXS_20120206_cropped_C1_sigma_psi, linestyle='none', markersize=9, color='black')
graph19.plot(TXS_20120206_doublesize_C2_psi, TXS_20120206_cropped_C2_psi,'o', linestyle='none', markersize=5, color='blue',label='C3')
graph19.errorbar(TXS_20120206_doublesize_C2_psi, TXS_20120206_cropped_C2_psi, xerr=TXS_20120206_doublesize_C2_sigma_psi, yerr=TXS_20120206_cropped_C2_sigma_psi, linestyle='none', markersize=9, color='blue')
graph19.plot(TXS_20120206_doublesize_C3_psi, TXS_20120206_cropped_C3_psi,'o', linestyle='none', markersize=5, color='green',label='C2')
graph19.errorbar(TXS_20120206_doublesize_C3_psi, TXS_20120206_cropped_C3_psi, xerr=TXS_20120206_doublesize_C3_sigma_psi, yerr=TXS_20120206_cropped_C3_sigma_psi, linestyle='none', markersize=9, color='green')
graph19.legend(loc='upper left', fontsize=6)
graph19.tick_params(axis="x", direction="in", labelsize=9)
graph19.tick_params(axis="y", direction="in", labelsize=9)
graph19.xaxis.set_ticks(np.arange(-130, 110.001, 80))
graph19.yaxis.set_ticks(np.arange(-130, 110.001, 80))
graph19.set_xlim(-130, 110)
graph19.set_ylim(-130, 110)

########################################################################################################
TXS_20200409_doublesize_core_psi = -89.304
TXS_20200409_doublesize_core_sigma_psi = 3.639
TXS_20200409_doublesize_C1_psi = -79.925
TXS_20200409_doublesize_C1_sigma_psi = 43.425
TXS_20200409_doublesize_C2_psi = 81.825
TXS_20200409_doublesize_C2_sigma_psi = 7.026

TXS_20200409_cropped_core_psi = -89.598
TXS_20200409_cropped_core_sigma_psi = 2.850
TXS_20200409_cropped_C1_psi = -83.341
TXS_20200409_cropped_C1_sigma_psi = 35.898
TXS_20200409_cropped_C2_psi = 82.571
TXS_20200409_cropped_C2_sigma_psi = 5.798

graph20 = fig.add_subplot(6, 4, 20)
ponto_inicial = [-200, 200]
ponto_final = [-200, 200]
graph20.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#raph20.set_title('$\psi$', fontsize=15, fontweight='bold')
#graph20.set_ylabel('Position angle', fontsize=9, fontweight="bold", labelpad=-1)
graph20.set_xlabel('Position angle', fontsize=9, fontweight="bold", labelpad=0)
graph20.plot(TXS_20200409_doublesize_core_psi, TXS_20200409_cropped_core_psi,  'o', linestyle='none', markersize=5, color='red',label='Core')
graph20.errorbar(TXS_20200409_doublesize_core_psi, TXS_20200409_cropped_core_psi, xerr=TXS_20200409_doublesize_core_sigma_psi, yerr=TXS_20200409_cropped_core_sigma_psi, linestyle='none', markersize=9, color='red')
graph20.plot(TXS_20200409_doublesize_C1_psi, TXS_20200409_cropped_C1_psi,  'o', linestyle='none', markersize=5, color='black',label='C12')
graph20.errorbar(TXS_20200409_doublesize_C1_psi, TXS_20200409_cropped_C1_psi, xerr=TXS_20200409_doublesize_C1_sigma_psi, yerr=TXS_20200409_cropped_C1_sigma_psi, linestyle='none', markersize=9, color='black')
graph20.plot(TXS_20200409_doublesize_C2_psi, TXS_20200409_cropped_C2_psi,'o', linestyle='none', markersize=5, color='blue',label='C11')
graph20.errorbar(TXS_20200409_doublesize_C2_psi, TXS_20200409_cropped_C2_psi, xerr=TXS_20200409_doublesize_C2_sigma_psi, yerr=TXS_20200409_cropped_C2_sigma_psi, linestyle='none', markersize=9, color='blue')
graph20.legend(loc='upper left', fontsize=6)
graph20.tick_params(axis="x", direction="in", labelsize=9)
graph20.tick_params(axis="y", direction="in", labelsize=9)
graph20.xaxis.set_ticks(np.arange(-130, 110.001, 80))
graph20.yaxis.set_ticks(np.arange(-130, 110.001, 80))
graph20.set_xlim(-130, 110)
graph20.set_ylim(-130, 110)

############################################################################
############### Parâmetro do CE: I_0 #######################################
############################################################################

PKS_20161210_doublesize_core_I0 = 0.8008
PKS_20161210_doublesize_core_sigma_I0 = 0.1352
PKS_20161210_doublesize_C1_I0 = 0.0814
PKS_20161210_doublesize_C1_sigma_I0 = 0.0129
PKS_20161210_doublesize_C2_I0 = 0.0289
PKS_20161210_doublesize_C2_sigma_I0 = 0.0041
PKS_20161210_doublesize_C3_I0 = 0.0151
PKS_20161210_doublesize_C3_sigma_I0 = 0.0026

PKS_20161210_cropped_core_I0 = 0.8009
PKS_20161210_cropped_core_sigma_I0 = 0.1352
PKS_20161210_cropped_C1_I0 = 0.0813
PKS_20161210_cropped_C1_sigma_I0 = 0.0129
PKS_20161210_cropped_C2_I0 = 0.0278
PKS_20161210_cropped_C2_sigma_I0 = 0.0040
PKS_20161210_cropped_C3_I0 = 0.0160
PKS_20161210_cropped_C3_sigma_I0 = 0.0034

graph21 = fig.add_subplot(6, 4, 21)
ponto_inicial = [-10, 10]
ponto_final = [-10, 10]
graph21.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph21.set_title('I', fontsize=15, fontweight='bold')
graph21.set_ylabel('Peak intensity', fontsize=9, labelpad=-0.5, fontweight="bold")
graph21.set_xlabel('Peak intensity', fontsize=9, labelpad=0, fontweight="bold")
#graph21.set_xlabel('Double size image', fontsize=12, labelpad=12, fontweight="bold")
graph21.plot(PKS_20161210_doublesize_core_I0, PKS_20161210_cropped_core_I0,  'o', linestyle='none', markersize=5, color='red',label='Core')
graph21.errorbar(PKS_20161210_doublesize_core_I0, PKS_20161210_cropped_core_I0, xerr=PKS_20161210_doublesize_core_sigma_I0, yerr=PKS_20161210_cropped_core_sigma_I0, linestyle='none', markersize=9, color='red')
graph21.plot(PKS_20161210_doublesize_C1_I0, PKS_20161210_cropped_C1_I0,  'o', linestyle='none', markersize=5, color='black',label='C3')
graph21.errorbar(PKS_20161210_doublesize_C1_I0, PKS_20161210_cropped_C1_I0, xerr=PKS_20161210_doublesize_C1_sigma_I0, yerr=PKS_20161210_cropped_C1_sigma_I0, linestyle='none', markersize=9, color='black')
graph21.plot(PKS_20161210_doublesize_C2_I0, PKS_20161210_cropped_C2_I0,'o', linestyle='none', markersize=5, color='blue',label='C2')
graph21.errorbar(PKS_20161210_doublesize_C2_I0, PKS_20161210_cropped_C2_I0, xerr=PKS_20161210_doublesize_C2_sigma_I0, yerr=PKS_20161210_cropped_C2_sigma_I0, linestyle='none', markersize=9, color='blue')
graph21.plot(PKS_20161210_doublesize_C3_I0, PKS_20161210_cropped_C3_I0,'o', linestyle='none', markersize=5, color='green',label='C1')
graph21.errorbar(PKS_20161210_doublesize_C3_I0, PKS_20161210_cropped_C3_I0, xerr=PKS_20161210_doublesize_C3_sigma_I0, yerr=PKS_20161210_cropped_C3_sigma_I0, linestyle='none', markersize=9, color='green')
graph21.legend(loc='upper left', fontsize=6)
graph21.set_xscale('log', nonpositive='clip')
graph21.set_yscale('log', nonpositive='clip')
#graph21.xaxis.set_ticks(np.arange(0.01, 2, 1))
#graph21.yaxis.set_ticks(np.arange(0.01, 2, 1))
graph21.set_xlim(0.01, 3)
graph21.set_ylim(bottom=0.01, top=3)
graph21.tick_params(axis="x", direction="in", which='both', labelsize=9)
graph21.tick_params(axis="y", direction="in", which='both', labelsize=9)


#########################################################################################################
PKS_20201201_doublesize_core_I0 = 0.5462
PKS_20201201_doublesize_core_sigma_I0 = 0.0910
PKS_20201201_doublesize_C1_I0 = 0.1346
PKS_20201201_doublesize_C1_sigma_I0 = 0.0233
PKS_20201201_doublesize_C2_I0 = 0.0255
PKS_20201201_doublesize_C2_sigma_I0 = 0.0028

PKS_20201201_cropped_core_I0 = 0.5682
PKS_20201201_cropped_core_sigma_I0 = 0.0945
PKS_20201201_cropped_C1_I0 = 0.1146
PKS_20201201_cropped_C1_sigma_I0 = 0.0205
PKS_20201201_cropped_C2_I0 = 0.0229
PKS_20201201_cropped_C2_sigma_I0 = 0.0026

graph22 = fig.add_subplot(6, 4, 22)
ponto_inicial = [-10, 10]
ponto_final = [-10, 10]
graph22.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph22.set_title('$I$', fontsize=15, fontweight='bold')
#graph22.set_ylabel('Peak intensity', fontsize=9, labelpad=-1, fontweight="bold")
graph22.set_xlabel('Peak intensity', fontsize=9, labelpad=0, fontweight="bold")
graph22.plot(PKS_20201201_doublesize_core_I0, PKS_20201201_cropped_core_I0, 'o', linestyle='none', markersize=5, color='red',label='Core')
graph22.errorbar(PKS_20201201_doublesize_core_I0, PKS_20201201_cropped_core_I0, xerr=PKS_20201201_doublesize_core_sigma_I0, yerr=PKS_20201201_cropped_core_sigma_I0, linestyle='none', markersize=9, color='red')
graph22.plot(PKS_20201201_doublesize_C1_I0, PKS_20201201_cropped_C1_I0, 'o', linestyle='none', markersize=5, color='black',label='U')
graph22.errorbar(PKS_20201201_doublesize_C1_I0, PKS_20201201_cropped_C1_I0, xerr=PKS_20201201_doublesize_C1_sigma_I0, yerr=PKS_20201201_cropped_C1_sigma_I0, linestyle='none', markersize=9, color='black')
graph22.plot(PKS_20201201_doublesize_C2_I0, PKS_20201201_cropped_C2_I0, 'o', linestyle='none', markersize=5, color='blue',label='C7')
graph22.errorbar(PKS_20201201_doublesize_C2_I0, PKS_20201201_cropped_C2_I0, xerr=PKS_20201201_doublesize_C2_sigma_I0, yerr=PKS_20201201_cropped_C2_sigma_I0, linestyle='none', markersize=9, color='blue')
graph22.legend(loc='upper left', fontsize=6)

graph22.set_xscale('log', nonpositive='clip')
graph22.set_yscale('log', nonpositive='clip')
graph22.set_xlim(0.01, 3)
graph22.set_ylim(bottom=0.01, top=3)
graph22.tick_params(axis="x", direction="in", which='both', labelsize=9)
graph22.tick_params(axis="y", direction="in", which='both', labelsize=9)

########################################################################################################
TXS_20120206_doublesize_core_I0 = 0.2283
TXS_20120206_doublesize_core_sigma_I0 = 0.0427
TXS_20120206_doublesize_C1_I0 = 0.0309
TXS_20120206_doublesize_C1_sigma_I0 = 0.0148
TXS_20120206_doublesize_C2_I0 = 0.0493
TXS_20120206_doublesize_C2_sigma_I0 = 0.0096
TXS_20120206_doublesize_C3_I0 = 0.0300
TXS_20120206_doublesize_C3_sigma_I0 = 0.0087

TXS_20120206_cropped_core_I0 = 0.2306
TXS_20120206_cropped_core_sigma_I0 = 0.0397
TXS_20120206_cropped_C1_I0 = 0.0289
TXS_20120206_cropped_C1_sigma_I0 = 0.0064
TXS_20120206_cropped_C2_I0 = 0.0489
TXS_20120206_cropped_C2_sigma_I0 = 0.0086
TXS_20120206_cropped_C3_I0 = 0.0302
TXS_20120206_cropped_C3_sigma_I0 = 0.0067

graph23 = fig.add_subplot(6, 4, 23)
ponto_inicial = [-2, 10]
ponto_final = [-2, 10]
graph23.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph23.set_title('I', fontsize=15, fontweight='bold')
#graph23.set_ylabel('Peak intensity', fontsize=9, labelpad=-1, fontweight="bold")
graph23.set_xlabel('Peak intensity', fontsize=9, labelpad=0, fontweight="bold")
graph23.plot(TXS_20120206_doublesize_core_I0, TXS_20120206_cropped_core_I0,  'o', linestyle='none', markersize=5, color='red',label='Core')
graph23.errorbar(TXS_20120206_doublesize_core_I0, TXS_20120206_cropped_core_I0, xerr=TXS_20120206_doublesize_core_sigma_I0, yerr=TXS_20120206_cropped_core_sigma_I0, linestyle='none', markersize=9, color='red')
graph23.plot(TXS_20120206_doublesize_C1_I0, TXS_20120206_cropped_C1_I0,  'o', linestyle='none', markersize=5, color='black',label='C4')
graph23.errorbar(TXS_20120206_doublesize_C1_I0, TXS_20120206_cropped_C1_I0, xerr=TXS_20120206_doublesize_C1_sigma_I0, yerr=TXS_20120206_cropped_C1_sigma_I0, linestyle='none', markersize=9, color='black')
graph23.plot(TXS_20120206_doublesize_C2_I0, TXS_20120206_cropped_C2_I0,'o', linestyle='none', markersize=5, color='blue',label='C3')
graph23.errorbar(TXS_20120206_doublesize_C2_I0, TXS_20120206_cropped_C2_I0, xerr=TXS_20120206_doublesize_C2_sigma_I0, yerr=TXS_20120206_cropped_C2_sigma_I0, linestyle='none', markersize=9, color='blue')
graph23.plot(TXS_20120206_doublesize_C3_I0, TXS_20120206_cropped_C3_I0,'o', linestyle='none', markersize=5, color='green',label='C2')
graph23.errorbar(TXS_20120206_doublesize_C3_I0, TXS_20120206_cropped_C3_I0, xerr=TXS_20120206_doublesize_C3_sigma_I0, yerr=TXS_20120206_cropped_C3_sigma_I0, linestyle='none', markersize=9, color='green')
graph23.legend(loc='upper left', fontsize=6)

graph23.set_xscale('log', nonpositive='clip')
graph23.set_yscale('log', nonpositive='clip')
graph23.set_xlim(0.01, 3)
graph23.set_ylim(bottom=0.01, top=3)
graph23.tick_params(axis="x", direction="in", which='both', labelsize=9)
graph23.tick_params(axis="y", direction="in", which='both', labelsize=9)

########################################################################################################
TXS_20200409_doublesize_core_I0 = 1.7064
TXS_20200409_doublesize_core_sigma_I0 = 0.2950
TXS_20200409_doublesize_C1_I0 = 0.3081
TXS_20200409_doublesize_C1_sigma_I0 = 0.0643
TXS_20200409_doublesize_C2_I0 = 0.0675
TXS_20200409_doublesize_C2_sigma_I0 = 0.0139

TXS_20200409_cropped_core_I0 = 1.7094
TXS_20200409_cropped_core_sigma_I0 = 0.2955
TXS_20200409_cropped_C1_I0 = 0.3069
TXS_20200409_cropped_C1_sigma_I0 = 0.0643
TXS_20200409_cropped_C2_I0 = 0.0663
TXS_20200409_cropped_C2_sigma_I0 = 0.0126

graph24 = fig.add_subplot(6, 4, 24)
ponto_inicial = [-10, 10]
ponto_final = [-10, 10]
graph24.plot(ponto_inicial, ponto_final,  linestyle='-', color='grey')
#graph24.set_title('$\psi$', fontsize=15, fontweight='bold')
#graph24.set_ylabel('Peak intensity', fontsize=9, labelpad=-1, fontweight="bold")
graph24.set_xlabel('Peak intensity', fontsize=9, labelpad=0, fontweight="bold")
graph24.plot(TXS_20200409_doublesize_core_I0, TXS_20200409_cropped_core_I0,  'o', linestyle='none', markersize=5, color='red',label='Core')
graph24.errorbar(TXS_20200409_doublesize_core_I0, TXS_20200409_cropped_core_I0, xerr=TXS_20200409_doublesize_core_sigma_I0, yerr=TXS_20200409_cropped_core_sigma_I0, linestyle='none', markersize=9, color='red')
graph24.plot(TXS_20200409_doublesize_C1_I0, TXS_20200409_cropped_C1_I0,  'o', linestyle='none', markersize=5, color='black',label='C12')
graph24.errorbar(TXS_20200409_doublesize_C1_I0, TXS_20200409_cropped_C1_I0, xerr=TXS_20200409_doublesize_C1_sigma_I0, yerr=TXS_20200409_cropped_C1_sigma_I0, linestyle='none', markersize=9, color='black')
graph24.plot(TXS_20200409_doublesize_C2_I0, TXS_20200409_cropped_C2_I0,'o', linestyle='none', markersize=5, color='blue',label='C11')
graph24.errorbar(TXS_20200409_doublesize_C2_I0, TXS_20200409_cropped_C2_I0, xerr=TXS_20200409_doublesize_C2_sigma_I0, yerr=TXS_20200409_cropped_C2_sigma_I0, linestyle='none', markersize=9, color='blue')
graph24.legend(loc='upper left', fontsize=6)

graph24.set_xscale('log', nonpositive='clip')
graph24.set_yscale('log', nonpositive='clip')
graph24.set_xlim(0.01, 3)
graph24.set_ylim(bottom=0.01, top=3)
graph24.tick_params(axis="x", direction="in", which='both', labelsize=9)
graph24.tick_params(axis="y", direction="in", which='both', labelsize=9)


################################################################################################
fig.supxlabel('Double-size images', fontsize=15, fontweight='bold')
fig.supylabel('Original cropped images', fontsize=15, fontweight='bold')
#plt.legend(bbox_to_anchor=(0, -0.8, 1.3, .102), loc='lower center', ncol=3, mode="expand", borderaxespad=0.)

plt.show()