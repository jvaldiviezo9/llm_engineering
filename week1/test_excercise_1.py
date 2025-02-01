import openai
import os

api_key = os.environ.get('OPENAI_API_KEY')

client = openai.OpenAI(
        api_key=api_key,
        base_url="https://router.requesty.ai/v1"
    )

# Define model
model = "deepseek/deepseek-chat"

# Send request
response = client.chat.completions.create(
    model=model,
    max_tokens=150,
    stream=True,
    messages=[
        {"role": "user", "content": "test"}
    ]
)

# Print streamed response
output_text = ""

for chunk in response:
    if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
        content = chunk.choices[0].delta.content
        output_text += content
        print(content, end="", flush=True)

print() # Print a newline at the end