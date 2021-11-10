
with open("/path/to/your/file", mode="r", encoding="utf-8") as file_handler:
  lines = file_handler.readlines()
  for line in lines:
    print(line)


with open('foobar', mode ='r') as file:
  # reading the CSV file
  csvFile = csv.DictReader(file)

  # displaying the contents of the CSV file
  for lines in csvFile:
    print(lines)


bla