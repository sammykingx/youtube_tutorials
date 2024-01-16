import io
import pandas as pd

def read_file(file_data):
    """reads a file"""

    file_object = io.BytesIO(file_data)
    df = pd.read_csv(file_object)

    print(df)

    return df.to_dict()
