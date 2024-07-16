import pandas as pd

class ENoseIO:
    def read_patient_data(filepath):
        with open(filepath, 'r') as file:
            lines = file.readlines()
            patient_id = int(lines[0].split(':')[1].strip())
            result = lines[1].split(':')[1].strip()
            data = pd.read_csv(filepath, sep='\t', skiprows=3)
            data['Patient_ID'] = patient_id
            data['Result'] = result
        return data