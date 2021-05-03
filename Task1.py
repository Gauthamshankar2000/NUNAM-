import pandas as pd
import os

func = pd.DataFrame()
for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        func = func.append(pd.read_csv(file))

func.to_csv('detail.csv')

import pandas as pd
import os

func = pd.DataFrame()
for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        func = func.append(pd.read_csv(file))

func.to_csv('detailVol.csv')

import pandas as pd
import os

func = pd.DataFrame()
for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        func = func.append(pd.read_csv(file))

func.to_csv('detailTemp.csv')