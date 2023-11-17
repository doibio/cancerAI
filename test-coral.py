import cohere

import os
import codecs

directory_path = 'edirect0'

documents = []

for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):  
        filepath = os.path.join(directory_path, filename)
        try:
            with codecs.open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                
                document = {
                    "title": filename.replace('.txt', ''),  
                    "snippet": content
                }
                documents.append(document)
        except Exception as e:
            print(f"Error reading {filename}: {e}")



co = cohere.Client('66YEjoukazKyL1bOOuIdD3K2Kqe401gddkG4nbSj')
response = co.chat(
    message="Please do a business analysis of the company Immuncore with relation to Tebentafusp with regard to TAM and other indicators. Please write it to fit on a slide",
    #documents=documents,
    connectors=[{"id": "web-search"}],
    prompt_truncation="AUTO"
)
print(response)
