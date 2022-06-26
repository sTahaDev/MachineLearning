
from statistics import mean
import numpy as np
import pandas as pd
import time
from sklearn.impute import SimpleImputer

veri = pd.read_csv('eksikveriler.csv')

imputer = SimpleImputer(missing_values=np.nan,strategy= "mean")
Yas = veri.iloc[:,1:4].values
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)

time.sleep(30)
