# Задача №44
# Создать новый столбец height_group в таблице с пингвинами, 
# который будет отвечать за показатель длины клюва пингвина. 
# high - высокий(от 42), middle - средний(от 35 до 42), low - низкий(до 35).
# Изобразить гистограмму по flipper_length_mm с оттенком height_group.

import seaborn as sns
peng = sns.load_dataset('penguins')
peng.head()

peng.loc[peng['bill_length_mm'] <= 35, 'height_group'] = 'low'
peng.loc[(peng['bill_length_mm'] > 35) & (peng['bill_length_mm'] <= 42),
'height_group'] = 'middle'
peng.loc[peng['bill_length_mm'] > 42, 'height_group'] = 'high'

peng.head()

sns.histplot(data=peng, x='flipper_length_mm', hue="height_group")

# Задача №44 (дополнительное)
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head()

import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)

data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value = 0).astype(int)
data.columns = data.columns.droplevel()
data.columns.name = None
print(data)