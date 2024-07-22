import pandas as pd
import os

class ENoseIO:
    @staticmethod
    def read_patient_data(filepath, is_labeled=True):
        with open(filepath, 'r') as file:
            lines = file.readlines()
            patient_id = int(lines[0].split(':')[1].strip())

            data = pd.read_csv(filepath, sep='\t', skiprows=3 if is_labeled else 2)
            data['Patient_ID'] = patient_id
            
            if is_labeled:
                result = lines[1].split(':')[1].strip()
                data['Result'] = result
        
        return data
    
    def save_predictions_to_csv(predictions, folder='submissions'):
        if not os.path.exists(folder):
            os.makedirs(folder)

        existing_files = [f for f in os.listdir(folder) if f.startswith('submission_') and f.endswith('.csv')]
        if existing_files:
            indices = [int(f.split('_')[1].split('.')[0]) for f in existing_files]
            next_index = max(indices) + 1
        else:
            next_index = 1
        
        filename = f'submission_{next_index}.csv'
        filepath = os.path.join(folder, filename)
        df = pd.DataFrame({'Index': range(len(predictions)), 'Prediction': predictions})
        df.to_csv(filepath, index=False)
        print(f'Saved predictions to {filepath}')