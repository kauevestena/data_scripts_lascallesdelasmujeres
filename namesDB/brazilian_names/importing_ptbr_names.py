import os
import pandas as pd

from os.path import expanduser
homepath = expanduser("~")

# # loading IBGE data, source: https://brasil.io/dataset/genero-nomes/files/
ptbr_names_path = os.path.join(homepath,'/data_scripts_lascallesdelasmujeres/namesDB/nomes.csv') # considering that you cloned at homefolder

names_dataframe = pd.read_csv(ptbr_names_path)

# splitting M and F names
F_NAMES = names_dataframe.loc[names_dataframe['classification'] == 'F']

M_NAMES = names_dataframe.loc[names_dataframe['classification'] == 'M']

# loading from original data from @lascallesdelasmujeres 
list_mujeres_path = os.path.join(homepath,'/data_scripts_lascallesdelasmujeres/namesDB/list_mujeres.csv')

list_hombres_path = os.path.join(homepath,'/data_scripts_lascallesdelasmujeres/namesDB/list_hombres.csv')

mujeres_df = pd.read_csv(list_mujeres_path,header=None,names=['name'])

hombres_df = pd.read_csv(list_hombres_path,header=None,names=['name'])

list_mujeres = list(mujeres_df['name'])
list_hombres = list(hombres_df['name'])

# adding br names:

print('list_mujeres before: ',len(list_mujeres))
print('F at IBGE data: ',len(list(F_NAMES['first_name'])))


print('list_hombres before: ',len(list_hombres))
print('M at IBGE data: ',len(list(M_NAMES['first_name'])))



for i,name in enumerate(list(F_NAMES['first_name'])):
    if i % 10000 == 0:
        print(i)

    if (not name in list_mujeres) and (not name in list_hombres):
        list_mujeres.append(name)

for i,name in enumerate(list(M_NAMES['first_name'])):
    if i % 10000 == 0:
        print(i)

    if (not name in list_hombres) and (not name in list_mujeres):
        list_hombres.append(name)


print('list_mujeres after: ',len(list_mujeres))
print('list_hombres after: ',len(list_hombres))

with open(list_mujeres_path,'w+') as writer:
    for name in list_mujeres:
        writer.write(str(name)+'\n')

        if type(name) == float:
            print(name)


with open(list_hombres_path,'w+') as writer:
    for name in list_hombres:
        writer.write(str(name)+'\n')

        if type(name) == float:
            print(name)


