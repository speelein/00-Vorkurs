import csv
with open('alle.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(someiterable)