from sap import *
import pandas as pd
import csv

# dictionary of data
element = []
for i in range(len(data())):
    for j in range(len(data()[i])):
        auth = data()[i]['Author name']
        head = data()[i]['Heading']
        cont = data()[i]['Content']
        link = data()[i]['Link']
        dict = {"Name": auth, "Heading": head, "Text": cont, "Link":link}
        element.append(dict)

df = pd.DataFrame(element)
# print(df)
df.to_csv('SAP.csv',index=False)

# with open('SAP.csv', 'w', newline='') as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(to_csv)
# saving the dataframe
