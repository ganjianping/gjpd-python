from openai import OpenAI

client = OpenAI()

"""
https://platform.openai.com/docs/guides/conversation-state?api-mode=responses
"""

def get_response_with_manual_history(conversation_history=None, model="gpt-4o-mini"):
    if conversation_history is None:
        # Default example history
        conversation_history = [
            {"role": "user", "content": "knock knock."},
            {"role": "assistant", "content": "Who's there?"},
            {"role": "user", "content": "Orange."},
        ]
    
    response = client.responses.create(
        model=model,
        input=conversation_history,
    )
    return response.output_text

def get_response_with_dynamic_history(prompts, model="gpt-4o-mini"):
    if not prompts or not isinstance(prompts, list):
        raise ValueError("prompts must be a non-empty list")
    
    # Initialize conversation history with the first prompt
    history = [{"role": "user", "content": prompts[0]}]
    responses = []
    
    # Process each prompt and maintain conversation history
    for i, prompt in enumerate(prompts):
        # For the first prompt, we've already added it to history
        if i > 0:
            history.append({"role": "user", "content": prompt})
        
        # Get response from model
        response = client.responses.create(model=model, input=history, store=False)
        responses.append(response.output_text)
        
        # Add the response to conversation history
        history += [
            {"role": output.role, "content": output.content} for output in response.output
        ]
    
    return responses

def get_response_with_server_state(initial_prompt, follow_up_prompt, model="gpt-4o-mini"):
    # Get first response
    response = client.responses.create(
        model=model,
        input=initial_prompt,
    )
    first_response = response.output_text
    
    # Get second response using previous_response_id
    second_response = client.responses.create(
        model=model,
        previous_response_id=response.id,
        input=[{"role": "user", "content": follow_up_prompt}],
    )
    
    return first_response, second_response.output_text

# Example usage
if __name__ == "__main__":
    # Manual conversation state example
    print("=== Manual Conversation State ===")
    complex_history = [
        {"role": "user", "content": "Hello, I'm planning a trip to Japan."},
        {"role": "assistant", "content": "That sounds exciting! What kind of information would you like about Japan?"},
        {"role": "user", "content": "I'm interested in the best time to visit Tokyo."},
        {"role": "assistant", "content": "Tokyo is generally pleasant to visit in spring (March to May) and autumn (September to November). Cherry blossom season in late March to early April is especially popular, while autumn offers beautiful foliage. Summer can be hot and humid, and winter is generally mild but can be cold."},
        {"role": "user", "content": "What about traditional foods I should try?"}
    ]
    manual_response = get_response_with_manual_history(complex_history)
    print(manual_response)
    
    # Dynamic conversation state example
    print("\n=== Dynamic Conversation State ===")
    # Example usage in main:
    prompt_list = [
        "tell me a joke", 
        "tell me another one", 
        "explain the last joke",
        "now tell me a fact about space"
    ]
    responses = get_response_with_dynamic_history(prompt_list)
    for i, response in enumerate(responses):
        print(f"\nPrompt {i+1}: {prompt_list[i]}")
        print(f"Response {i+1}: {response}")
    
    # Server-managed conversation state example
    print("\n=== Server-Managed Conversation State ===")
    joke, explanation = get_response_with_server_state(
        "tell me a joke", "explain why this is funny."
    )
    print(f"Joke: {joke}")
    print(f"Explanation: {explanation}")