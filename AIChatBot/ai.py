import ollama
import subprocess

# Pull the model using the CLI
subprocess.run(["ollama", "pull", "deepseek-r1"], check=True)

# Your code that you want help with
code_snippet = """
def add(a, b):
    return a + b
"""

# The prompt asking for help
prompt = "Can you help me optimize this function?"

# Debugging statement to check if the request is being made
print("Sending request to ollama.chat...")

response = ollama.chat(
    model="deepseek-r1",
    messages=[
        {"role": "user", "content": f"Here is my code:\n{code_snippet}\n{prompt}"},
    ],
)

# Debugging statement to check if the response is received
print("Response received from ollama.chat")

# Check if the response contains the expected content
if "message" in response and "content" in response["message"]:
    print(response["message"]["content"])
else:
    print("No content found in the response")