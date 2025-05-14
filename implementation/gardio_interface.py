import gradio as gr

def start_gradio_interface(conversation_chain):
    def chat(question, history):
        result = conversation_chain.invoke({"question": question})
        return result["answer"]

    gr.ChatInterface(chat, type="messages").launch(inbrowser=True)
