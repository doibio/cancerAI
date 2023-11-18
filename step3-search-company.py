import cohere

import os
import codecs

co = cohere.Client('KEY_HERE')
response = co.chat(
    message="Please write a business analysis of Immunocore",
    connectors=[{"id": "web-search"}],
    prompt_truncation="AUTO"
)
print(response)
