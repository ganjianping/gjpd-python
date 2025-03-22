from openai import OpenAI

client = OpenAI()

def get_openai_image_response(text_prompt, image_url, model="gpt-4o-mini"):
    response = client.responses.create(
        model=model,
        input=[
            {"role": "user", "content": text_prompt},
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_image",
                        "image_url": image_url,
                    }
                ],
            },
        ],
    )
    return response.output_text

# Example usage
text_prompt = "Describe the general scene or elements in the image in exactly 20 words, focusing on objects, colors, and actions."
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Steve_Jobs_WWDC07.jpg/1024px-Steve_Jobs_WWDC07.jpg"
# image_response = get_openai_image_response(text_prompt, image_url)
# print(image_response) # A man wearing a black turtleneck gestures actively, standing on stage with blue curtains, engaging an audience with enthusiasm.