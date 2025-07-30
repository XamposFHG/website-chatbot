# app.py
from llama_index import GPTSimpleVectorIndex
import gradio as gr

# Load the index we built
index = GPTSimpleVectorIndex.load_from_disk("index.json")

# Define a simple chat function
def chat(query: str) -> str:
    response = index.query(query)
    return str(response)

# Build the Gradio UI
iface = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(lines=2, placeholder="Ask me anything about my site..."),
    outputs="text",
    title="Website Chatbot"
)

if __name__ == "__main__":
    iface.launch()
