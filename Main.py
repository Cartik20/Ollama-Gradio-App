import gradio as gr
import pandas as pd
from utils.file_handler import load_csv
from utils.graph_plot import plot_graph
from models.llm import ask_llm

# Global variable to store the uploaded CSV
df = None

# Function to handle file upload
def upload_and_display(file):
    global df
    result, df = load_csv(file)  # Load CSV and store in memory
    return result

# Function to query LLM
def query_llm(question):
    global df
    if df is None:
        return " Please upload a CSV first."
    return ask_llm(question, df)  # Pass df to LLM function

# Function to plot a graph
def generate_graph(x_column, y_column):
    global df
    if df is None:
        return " Please upload a CSV file first."
    
    # Debug print to verify df exists
    print(f" DataFrame shape: {df.shape}")
    print(f" DataFrame columns: {df.columns.tolist()}")
    print(f" Requested columns: X={x_column}, Y={y_column}")
    
    # Check if columns exist before plotting
    if x_column not in df.columns or y_column not in df.columns:
        return f" Column not found. Available columns: {', '.join(df.columns)}"
    
    try:
        # Return the result from plot_graph
        result = plot_graph(x_column, y_column, df)
        
        # If result is a string starting with a warning or error symbol, it's an error message
        if isinstance(result, str) and (result.startswith("⚠️") or result.startswith("❌")):
            return result
        
        print(f" Graph successfully generated: {result}")
        return result
    except Exception as e:
        print(f" Exception in generate_graph: {str(e)}")
        return f" Error generating graph: {str(e)}"

# Create Gradio interface
with gr.Blocks() as app:
    gr.Markdown("<h1 style='text-align: center;'>CSV Question Answering & Visualization App </h1>")

    # File upload section
    with gr.Row():
        file_input = gr.File(label="Upload CSV", file_types=[".csv"])
        file_output = gr.Textbox(label="File Status", interactive=False)

    file_input.change(fn=upload_and_display, inputs=file_input, outputs=file_output)

    # Question answering section
    with gr.Row():
        question_input = gr.Textbox(label="Ask a question about the data")
        answer_output = gr.Textbox(label="LLM Answer", interactive=False)

    ask_button = gr.Button("Ask question")
    ask_button.click(fn=query_llm, inputs=question_input, outputs=answer_output)

    # Graph section
    with gr.Row():
        x_col = gr.Textbox(label="X-axis Column", placeholder="Enter X-axis column name")
        y_col = gr.Textbox(label="Y-axis Column", placeholder="Enter Y-axis column name")
    
    with gr.Row():    
        # Use type="filepath" to ensure Gradio knows to load the file from disk
        graph_output = gr.Image(label="Generated Graph", type="filepath")

    plot_button = gr.Button("Generate Graph")
    plot_button.click(fn=generate_graph, inputs=[x_col, y_col], outputs=graph_output)

# Run the app
if __name__ == "__main__":
    app.launch(share=True)


