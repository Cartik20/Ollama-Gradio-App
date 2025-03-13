import matplotlib.pyplot as plt
import io
import pandas as pd
import numpy as np
from PIL import Image

def plot_graph(x_column, y_column, df):
    """Plots a graph from the dataset and returns an image that Gradio can display."""
    # Validate inputs
    if df is None:
        return "⚠️ No CSV file loaded."

    if x_column not in df.columns or y_column not in df.columns:
        return f" Invalid column names! Available: {', '.join(df.columns)}"

    # Create a clean copy of the DataFrame to avoid modifying the original
    temp_df = df.copy()
    
    # Convert columns to numeric
    try:
        temp_df[x_column] = pd.to_numeric(temp_df[x_column], errors='coerce')
        temp_df[y_column] = pd.to_numeric(temp_df[y_column], errors='coerce')
        
        # Remove NaN values
        temp_df = temp_df.dropna(subset=[x_column, y_column])
        
        print(f" Data points for plotting: {len(temp_df)}")
    except Exception as e:
        print(f"Error preparing data: {str(e)}")
        return f" Error preparing data: {str(e)}"

    # Check if we have data to plot
    if len(temp_df) == 0:
        return " Not enough valid numeric data to plot!"

    try:
        # Method 1: Directly generate a file path for the graph
        # Create a temporary file path for the plot
        import tempfile
        import os
        
        # Create a temporary file with .png extension
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        temp_path = temp_file.name
        temp_file.close()
        
        # Generate the plot and save it to the file
        plt.figure(figsize=(10, 6))
        plt.plot(temp_df[x_column], temp_df[y_column], marker='o', linestyle='-')
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"{x_column} vs {y_column}")
        plt.grid(True)
        plt.tight_layout()
        
        # Save the figure to the temp file
        plt.savefig(temp_path, format='png', dpi=100)
        plt.close('all')
        
        print(f" Graph saved to temporary file: {temp_path}")
        
        # Return the file path which Gradio can load
        return temp_path
        
    except Exception as e:
        print(f"Error generating plot: {str(e)}")
        # Return error message with detailed information
        return f" Error generating plot: {str(e)}"



