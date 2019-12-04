# This file generate the delay and ontime rates as percantage of each airline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

font = {'size':20}

plt.rc('font', **font)
file='delay_rate.csv'
delay_freq=pd.read_csv(file,index_col=0,header=0)
delay_freq = delay_freq.drop(labels=['AS','EV','F9','G4','HA','NK','VX','YV'])

airlines=list(delay_freq.index)
airlines_name={'F9':'Frontier Airlines', '9E':'Endeavor Air', 'EV':'ExpressJet Airlines', 'YX':'Midwest Airlines', 'UA':'United Airlines', 'VX':'Virgin America', 'MQ':'Envoy Air',
               'DL':'Delta Air Lines', 'AA':'American Airlines', 'OO':'SkyWest Airlines', 'YV':'Mesa Airlines', 'HA':'Hawaiian Airlines',
               'AS':'Alaska Airlines', 'OH':'PSA Airlines', 'G4':'Allegiant Air', 'WN':'Southwest Airlines', 'NK':'Spirit Airlines', 'B6':'JetBlue Airways'}
delay_freq=delay_freq.rename(index=airlines_name)
airlines=list(delay_freq.index)
# visualization
width=0.7
plt.figure(figsize=(9,7))

p1 = plt.barh(delay_freq.index,delay_freq['delay'],width,label='Delay')
p2 = plt.barh(delay_freq.index,delay_freq['on-time_and_adv'],width,left=delay_freq['delay'],label='On-time/Early')
plt.xticks(np.arange(0, 1.1, 0.1))
plt.legend(bbox_to_anchor=(1,-0.3),loc='lower right')
plt.xlabel('Rate')
plt.ylabel('Airlines')
plt.show()