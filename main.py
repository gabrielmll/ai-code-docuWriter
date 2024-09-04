from utils.file import read_file, write_to_file
from utils.performance import timelapse
from code_extractor.main import get_relevant_code

from datetime import datetime
import time

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

start_time = time.time()

try:
    get_relevant_code(
        repository_path='/home/marihoffmann/projetos/hermes',
        endpoint_file_path='/hermes/api/v3/v3.py',
        route='/follow_group',
        method='POST'
    )
except TypeError as e:
    print(f'Houve um erro na extração do código relevante para este endpoint: {e}')
    raise

code = read_file("./combined_code_output.py")
template = read_file("./prompt_software_engineer.txt")

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.1")

chain = prompt | model

response = chain.invoke({"code": code})

timelapse(start_time)
print(response)

write_to_file(f"response-{datetime.now()}.txt", response)
