import pandas as pd

def load_csv(file):
    """Loads a CSV file and returns a status message and DataFrame."""
    try:
        df = pd.read_csv(file.name)
        return f" CSV Loaded Successfully! \n📊 Columns: {', '.join(df.columns)}", df
    except Exception as e:
        return f" Error loading CSV: {str(e)}", None
