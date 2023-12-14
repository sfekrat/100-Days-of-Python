import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray = len(data[data['Primary Fur Color'] == 'Gray'])
red = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {'Fur Color': ['Gray', 'Red', 'Black'], 'Count': [gray, red, black]}

analyzed_data = pandas.DataFrame(data_dict)
analyzed_data.to_csv('analyzed_data.csv')

