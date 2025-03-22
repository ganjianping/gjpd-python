from openai import OpenAI

client = OpenAI()

def get_basic_response(prompt, model="gpt-4o-mini"):
    """Get a basic response with just a prompt."""
    response = client.responses.create(
        model=model,
        input=prompt,
    )
    return response.output_text

prompt = "Explain the purpose of the OpenAI API in 20 words or less, focusing on its core functionality and benefits."
# response_text = get_basic_response(prompt)
# print(response_text) # The OpenAI API provides access to advanced AI models for natural language processing, enabling developers to build intelligent applications.


def get_response_with_instructions(prompt, instructions, model="gpt-4o"):
    """Get a response with dedicated instructions parameter."""
    response = client.responses.create(
        model=model,
        instructions=instructions,
        input=prompt,
    )
    return response.output_text

def get_response_with_roles(prompt, instructions, model="gpt-4o"):
    """Get a response using role-based input format."""
    response = client.responses.create(
        model=model,
        input=[
            {"role": "developer", "content": instructions},
            {"role": "user", "content": prompt},
        ],
    )
    return response.output_text

# Example usage
prompt = "Are semicolons optional in JavaScript?"
instructions = "Talk like a pirate."
styled_response = get_response_with_roles(prompt, instructions)
print(styled_response) # Arrr, indeed they be! In JavaScript, semicolons be often optional thanks to automatic semicolon insertion. But beware, matey! Sometimes it be cause fer unexpected troubles if ye rely on that too much. When in doubt, stick a semicolon to avoid any treacherous errors!
