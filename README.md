# CSV Question Answering & Visualization App

A Gradio-based web application that allows users to:
1. Upload CSV files
2. Ask questions about the data using an LLM
3. Generate visualizations from the data

## Features

- **CSV Upload**: Easily upload and load CSV files
- **Question Answering**: Ask questions in natural language about your data
- **Data Visualization**: Generate graphs by selecting X and Y axis columns
- **User-friendly Interface**: Clean, intuitive interface with light theme

## Requirements

- Python 3.x
- Required packages (install using `pip install -r requirement.txt`):
  - gradio
  - pandas
  - matplotlib
  - pillow
  - ollama (for LLM integration)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/csv-qa-visualization-app.git
   cd csv-qa-visualization-app
   ```

2. Install required packages:
   ```
   pip install -r requirement.txt
   ```

3. Run the application:
   ```
   python Main.py
   ```

4. Open the URL displayed in the terminal (typically http://127.0.0.1:7860)

## Usage

1. Upload a CSV file using the file upload section.
2. Ask questions about your data in the question section.
3. Generate graphs by entering column names for X and Y axes.

## Project Structure

- `Main.py`: The main application file
- `models/`: Contains the LLM integration
- `utils/`: Utility functions for file handling and graph plotting
- `static/`: Static assets for the application

## License

MIT 