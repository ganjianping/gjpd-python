from openai import OpenAI

client = OpenAI()

"""
https://platform.openai.com/docs/api-reference/responses
"""

# --------------------------------------------------------------
# Basic text example with the Responses API
# --------------------------------------------------------------

response = client.responses.create(
    model="gpt-4o", input="Using 30 words or less, describe the purpose of the OpenAI API.",
)

# The OpenAI API provides developers access to advanced language models, enabling integration of natural language understanding, generation, and AI-driven functionalities into applications for various tasks and industries.
print(response.output_text)