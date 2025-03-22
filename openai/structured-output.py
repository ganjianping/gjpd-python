import json
from typing import List

from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()

# --------------------------------------------------------------
# Using a Pydantic model (and simple response format)
# --------------------------------------------------------------

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: List[str]


response = client.responses.parse(
    model="gpt-4o",
    input="Alice and Bob are going to a science fair on Friday",
    instructions="Extract the event information",
    text_format=CalendarEvent,
)

print(response.output_text)

response_model = response.output[0].content[0].parsed
print(type(response_model)) # <class '__main__.CalendarEvent'>
print(response_model.model_dump_json(indent=2))