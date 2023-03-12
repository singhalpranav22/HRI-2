import cv2
import numpy as np
import PySimpleGUI as sg
import os
import pandas as pd

choices = []

# column1
col1 = [  
    [sg.Text('Select csv file to run:'), sg.In(size=(25,1), enable_events=True ,key='-FILE-'), sg.FileBrowse()],
    [sg.Text('CSV file headers:')],

            [sg.Listbox(choices, size=(40, len(choices)), key='-FILE_NAME-')],[sg.Button('Start visualisation from csv config', key='-START_VISUALISATION-')] ]
# column2
col2 = [[sg.T("Functions:")],
    [sg.Text('Enter number of iterations:'), sg.InputText(key='-ITERATIONS-')],
[sg.Button('Start making failed CSVs', key='-START_CSV_GEN-'),sg.Button('Exit', key='-EXIT-')]
]
# final layout
layout = [
    [sg.Column(col1),
     sg.VSeperator(pad=(0, 0)),
     sg.Column(col2),

     ]
]

# creating the window
window = sg.Window('Warehouse config GUI', layout,auto_size_text=True,
                   auto_size_buttons=True, resizable=True, grab_anywhere=False, border_depth=5,
                   default_element_size=(15, 1), finalize=True, element_justification='l')

# GUI event loop
while True:
    event, values = window.read()
    # if the event is to close the window
    if event in (sg.WIN_CLOSED, '-EXIT-'):
        break
    # if the event is to browse the folder
    if event == '-FILE-':
        # find the path of file selected
        file = values['-FILE-']
        # check if file is csv
        if file.endswith(('.csv')):
            # if yes then read the csv file
            df = pd.read_csv(file)
            # get the column names
            columns = df.columns
            # get the column names as list
            columns = columns.tolist()
            window['-FILE_NAME-'].update(values=columns)
        pass
    # if the event is to start the watermarking
    if event == '-START_CSV_GEN-':
        iterations = values['-ITERATIONS-']
        iterations = int(iterations)
        for i in range(iterations):
            os.system("python3 ../crowd_nav/test.py --policy orca --phase test --test_case 0")
        sg.popup('Done')
    if event == '-START_VISUALISATION-':
        # open the file
        file = values['-FILE-']
        # check if file is csv
        if file.endswith(('.csv')) == False:
            sg.popup('Please select a csv file')
            pass 
        # if yes then write the file in the text file current directory+configs/csvLocation.csv
        with open('configs/csvLocation.txt', 'w') as f:
            f.write(file)
        # run the visualisation
        os.system("python3 test.py --policy orca --phase test --visualize --test_case 0")
        # empty the contents of the file
        with open('configs/csvLocation.txt', 'w') as f:
            f.write('')
        sg.popup('Done')
