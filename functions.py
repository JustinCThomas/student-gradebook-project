import sqllite3


gradebook = sqlite3.connect('database.db')

gradebook.execute('CREATE TABLE')

## search each object

for i in search_features:
    if i == inputType:
        searchType = i
        break


for i in objects:
    if i.searchType == input:
        return i




    