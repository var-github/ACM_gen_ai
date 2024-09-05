# <span style="text-color:blue">ACM Gen AI Project</span>
In this project I have created a chatbot using GROQ and Hugging Face modules.
As an additional feature the chatbots can also hold context across messages.

### GROQ module
This module uses an API and gets responses from its own language model (groq llm)
It is extremely fast and has an efficient tokenizer inbuilt.

### Hugging Face module
This module acts as an interface between the llm and python script
The app has been configured to work with the following llms :-
- Mistral-Nemo-Instruct-2407
- Mistral-7B-Instruct-v0.3
- Mistral-7B-Instruct-v0.2
- gemma-1.1-7b-it
- Meta-Llama-3-8B-Instruct
- Mixtral-8x7B-Instruct-v0.1
- Mistral-7B-Instruct-v0.1
- HuggingFaceH4/zephyr-7b-beta

The choice of model was done based on 3 conditions - size of model, context length, no. of parameters it has been trained on.

---

This app is currently hosted on streamlit at [https://varun-acm-gen-ai-project.streamlit.app/](https://varun-acm-gen-ai-project.streamlit.app/)
