import cohere

import os
import codecs

co = cohere.Client('KEY_HERE')
response = co.chat(
    message="Please search for the latest immunotherapy treatments for eye cancer.",
    connectors=[{"id": "web-search"}],
    prompt_truncation="AUTO"
)
print(response)
