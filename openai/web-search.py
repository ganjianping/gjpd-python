from openai import OpenAI

client = OpenAI()


# --------------------------------------------------------------
# Basic web search
# --------------------------------------------------------------

response = client.responses.create(
    model="gpt-4o",
    tools=[
        {
            "type": "web_search_preview",
        }
    ],
    input="What are the best restaurants in Singapore?",
)

print(response.output_text)

# --------------------------------------------------------------
# Basic web search with location
# --------------------------------------------------------------

response = client.responses.create(
    model="gpt-4o",
    tools=[
        {
            "type": "web_search_preview",
            "user_location": {
                "type": "approximate",
                "country": "SG",
                "city": "Singapore",
            },
        }
    ],
    input="What are the best restaurants ?",
)

print(response.output_text)