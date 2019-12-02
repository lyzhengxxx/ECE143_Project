import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# file='2018.csv'
# readlines=100000
# flights=pd.read_csv(file) #read file
# uncancelled_flights=flights.loc[flights['CANCELLED']==0] #data excluding cancelled flights
# airlines=set(flights['OP_CARRIER']) #set of names of airlines
#
# score_data=pd.DataFrame(index=airlines,columns=['op_sch','fl_sp','arr_delay_rate','arr_delay','score'])
# for name in airlines:
#     score_data.loc[name]['op_sch']=list(flights.loc[flights['OP_CARRIER']==name]['CANCELLED']).count(0)/list(flights['OP_CARRIER']).count(name)
#     score_data.loc[name]['fl_sp']=100
#     score_data.loc[name]['arr_delay_rate']=1-list(flights.loc[flights['OP_CARRIER']==name]['ARR_DELAY']).count(0)/list(flights['OP_CARRIER']).count(name)
#     score_data.loc[name]['arr_delay'] = uncancelled_flights.loc[uncancelled_flights['OP_CARRIER']==name]['ARR_DELAY'].mean()
#     score_data.loc[name]['score'] = score_data.loc[name]['op_sch']*score_data.loc[name]['fl_sp']/(1+score_data.loc[name]['arr_delay_rate']*score_data.loc[name]['arr_delay'])
# max_score=max(list(score_data['score']))
# for name in airlines:
#     score_data.loc[name]['score']=score_data.loc[name]['score']/max_score
# score_data=score_data.sort_values(by='score')
# score_data.to_csv('score_data.csv')
file='score_data.csv'
score_data=pd.read_csv(file,index_col=0,header=0)
airlines=list(score_data.index)
airlines_name={'F9':'Frontier Airlines', '9E':'Endeavor Air', 'EV':'ExpressJet Airlines', 'YX':'Midwest Airlines', 'UA':'United Airlines', 'VX':'Virgin America', 'MQ':'Envoy Air',
               'DL':'Delta Air Lines', 'AA':'American Airlines', 'OO':'SkyWest Airlines', 'YV':'Mesa Airlines', 'HA':'Hawaiian Airlines',
               'AS':'Alaska Airlines', 'OH':'PSA Airlines', 'G4':'Allegiant Air', 'WN':'Southwest Airlines', 'NK':'Spirit Airlines', 'B6':'JetBlue Airways'}
score_data=score_data.rename(index=airlines_name)
x=np.arange(len(airlines))
plt.barh(x,score_data['score'],ec='grey',fc='lightblue',tick_label=score_data.index)
for (i,j) in zip(score_data['score'],x):
    plt.text(i+0.02, j-0.2, '%.2f' % i )
plt.xlim(0,1.1)
plt.xticks(np.arange(0,1.1,step=0.2))
plt.xlabel('Scores')
plt.ylabel('Airlines')
plt.title('Score of airlines')
plt.show()