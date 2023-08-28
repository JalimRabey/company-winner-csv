import csv

def get_formatter_csv_data():
  data = list()

  with open('db.csv', newline='') as csvfile:
    spamreader = list(csv.reader(csvfile))

    # remove a primeira linha do CSV, que são os nomes de cada coluna
    # e salva isso na variavel
    row_names = spamreader.pop(0)

    for row in spamreader:
      currentDict = dict()

      for index, item in enumerate(row):
        current_row = row_names[index]
        current_row_lower = current_row.lower()

        currentDict.update({current_row_lower: item})

      data.append(currentDict)

  return data