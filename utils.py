import pandas as pd
import os
from models import Contact

def save_to_excel(contact_data: Contact):
    file_path = os.path.join('data', 'contacts.xlsx')

    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
    else:
        df = pd.DataFrame(columns=['name','email','age','phone_number'])

    new_data_dict = contact_data.model_dump() # Use .model_dump() for modern Pydantic
    
    new_row_df = pd.DataFrame([new_data_dict])

    df = pd.concat([df, new_row_df], ignore_index=True) # Pass the variables, not strings

    os.makedirs('data', exist_ok=True)

    df.to_excel(file_path, index=False) # Set index to False

