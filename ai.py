# from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(model="phi3", temperature=0.9, top_p= 0.9)
# response = llm.predict("what is langchain")
# print(response)


prompt = """  
List an advantage and disadvantage of {topic}.
"""

prompt_template = PromptTemplate(template=prompt, input_variables=["topic"])
chain = prompt_template | llm

while True:
    topic = input("User: List the advantages and disadvantages of: ")
    if topic.lower() == "exit" or topic.lower() == "quit":
        break
    formatted_prompt = prompt_template.format(topic=topic)  # Format the prompt
    output = llm.invoke(formatted_prompt)  # Invoke LLM with the formatted prompt
    print(f"Bot: {output}")