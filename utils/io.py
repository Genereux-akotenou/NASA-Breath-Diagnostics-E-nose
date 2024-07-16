import pandas as pd

class ENoseIO:
    def read_patient_data(filepath, is_labeled=True):
        with open(filepath, 'r') as file:
            lines = file.readlines()
            patient_id = int(lines[0].split(':')[1].strip())

            data = pd.read_csv(filepath, sep='\t', skiprows=3)
            if is_labeled:
                result = lines[1].split(':')[1].strip()
                data['Result'] = result
            
            data['Patient_ID'] = patient_id

        return data