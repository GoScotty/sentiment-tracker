import pandas as pd
from io import StringIO

class DataProcessor:
    def process_file(self, uploaded_file):
        try:
            df = pd.read_csv(uploaded_file)
            if "text" not in df.columns:
                raise ValueError("CSV file must contain a 'text' column")
            return df
        except Exception as e:
            raise ValueError(f"Error processing file: {str(e)}")
