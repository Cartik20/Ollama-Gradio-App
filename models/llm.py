'''import ollama
import pandas as pd

# Global dataframe
df = None

def ask_llm(question):
    global df
    if df is None:
        return "⚠️ Please upload a CSV first."

    # Convert a sample of the dataset to a string for context
    data_sample = df.head(10).to_string()

    # Create a prompt for Mistral AI
    prompt = f"""
    You are an AI that analyzes structured CSV data.
    Here is a preview of the dataset:
    {data_sample}

    Answer the following question based on the dataset:
    {question}
    """

    # Call Ollama Mistral model
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']'''



import ollama
import pandas as pd

def ask_llm(question, df):
    """Queries the LLM using a given DataFrame."""
    if df is None:
        return " Please upload a CSV first."

    # Convert a sample of the dataset to a string for context
    data_sample = df.head(10).to_string()

    # Create a prompt for Mistral AI
    prompt = f"""
    You are an AI that analyzes structured CSV data.
    Here is a preview of the dataset:
    {data_sample}

    Answer the following question based on the dataset:
    {question}
    """

    # Call Ollama Mistral model
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

