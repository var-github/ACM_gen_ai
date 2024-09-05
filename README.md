## ACM Gen AI Project
In this project I have created a chatbot using GROQ and Hugging Face modules
As an additional feature the chatbots can also hold context across messages

#GROQ module
This module uses an API and gets responses from its own language model (groq llm)
It is extremely fast and has an efficient tokenizer inbuilt

#Hugging Face module
This module acts as an interface between the llm and python script
The app has been configured to work with the following llms :-
- Mistral-Nemo-Instruct-2407         CONTEXT LENGTH (128k tokens)
- Mistral-7B-Instruct-v0.3           CONTEXT LENGTH (k tokens)
- Mistral-7B-Instruct-v0.2           CONTEXT LENGTH (k tokens)
- gemma-1.1-7b-it                    CONTEXT LENGTH (8k tokens)
- Meta-Llama-3-8B-Instruct           CONTEXT LENGTH (8k tokens)
- Mixtral-8x7B-Instruct-v0.1         CONTEXT LENGTH (k tokens)
- Mistral-7B-Instruct-v0.1           CONTEXT LENGTH (k tokens)
- HuggingFaceH4/zephyr-7b-beta       CONTEXT LENGTH (k tokens)

