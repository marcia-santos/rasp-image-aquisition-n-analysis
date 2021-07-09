import os
import pandas as pd
list_of_files=os.listdir()
list_of_files.append('files.csv')

pd.DataFrame({'files':list_of_files}).to_csv('files.csv')