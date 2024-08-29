from utils.file import read_file, write_to_file
from utils.performance import timelapse

from datetime import datetime
import time

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

start_time = time.time()

code = read_file("./code_to_document.py")

template = read_file("./prompt_software_engineer.txt")

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.1")

chain = prompt | model

response = chain.invoke({"code": code})

timelapse(start_time)
print(response)

write_to_file(f"response-{datetime.now()}.txt", response)
