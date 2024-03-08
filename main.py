import os
import chainlit as cl
from ctransformers import AutoModelForCausalLM
from langchain_community.llms import CTransformers

start_instruct = "<s>[INST] "
end_instruct = "[/INST]"
end_sentence = "</s>"


# Runs when the chat starts
@cl.on_chat_start
def main():
    # Create the llm
    MODEL_PATH = 'models/mistral-7b-instruct-v0.1.Q5_K_S.gguf'
    config = {
    "max_new_tokens": 2048,
    "context_length": 4096,
    "repetition_penalty": 1.1,
    "temperature": 0.5,
    "top_k": 50,
    "top_p": 0.9,
    "stream": True,
    "threads": int(os.cpu_count() / 2)
}
    llm = CTransformers(model=MODEL_PATH, config=config, verbose=True)

    chat_history = []
    
    # Store the llm and chat history in the user session
    cl.user_session.set("llm", llm)
    cl.user_session.set("chat_history", chat_history)


# Runs when a message is sent
@cl.on_message
async def main(message: cl.Message):
    # Retrieve the chain from the user session
    llm = cl.user_session.get("llm")
    chat_history = cl.user_session.get("chat_history")
    chat_history.append({"role": "user", "content": message.content})

    msg = cl.Message(
        content="",
    )
    prompt = ""
    for entry in chat_history[-20:]:  # Adjust based on your context_length and average message size
        prompt += f"{entry['role']}: {entry['content']}\n"

    prompt = start_instruct + prompt + end_instruct
    for text in llm(prompt=prompt):
        await msg.stream_token(text)

    await msg.send()