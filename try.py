import os
import pandas as pd

def get_file_names(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    # Filter out directories, keeping only file names
    file_names = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
    return file_names

def save_to_excel(file_names, output_file):
    # Create a DataFrame from the file names
    df = pd.DataFrame(file_names, columns=['File Names'])
    # Save the DataFrame to an Excel file
    df.to_excel(output_file, index=False, engine='openpyxl')

# Example usage
folder_path = r"C:\Users\Kamie.K\OneDrive\Documents\IT STUFF\IT DEFENSE PPTs"  # Replace with your folder path
output_file = r"C:\Users\Kamie.K\OneDrive\Documents\IT STUFF\PROJECT_PURSE.xlsx"  # Replace with your desired output path

file_names = get_file_names(folder_path)
save_to_excel(file_names, output_file)

print("File names have been successfully saved to Excel.")
