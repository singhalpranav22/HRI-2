import csv
import os

test_cases = 1
fields = ['S.no.', 'k', 'Success Rate', 'Collision Rate', 'Nav Time', 'Total Reward', 'Freq. Danger',
          'Avg. Min. Separation dist in Danger']

# rows.append(row)
filename = "results.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the data rows
    csvwriter.writerow(fields)

for i in range(test_cases):
    os.system("python3 test.py --policy sarl --model_dir data/output --phase test")