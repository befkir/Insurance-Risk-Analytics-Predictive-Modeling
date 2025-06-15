import os
import pandas as pd

# Define paths
input_path = 'data/MachineLearningRating_v3.txt'
output_path = 'data/insurance_data.csv'

# Ensure the data directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

def convert_txt_to_csv(input_file, output_file):
    try:
        # Read the text file using '|' as delimiter
        df = pd.read_csv(input_file, delimiter='|')
        
        # Save to CSV
        df.to_csv(output_file, index=False)
        print(f"✅ Successfully converted to: {output_file}")
    except Exception as e:
        print(f"❌ Error during conversion: {e}")

if __name__ == "__main__":
    convert_txt_to_csv(input_path, output_path)
