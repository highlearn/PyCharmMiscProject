# simple_agent_gemma3.py
from langchain.agents import Tool, initialize_agent
from langchain.chat_models import ChatOllama  # Use the Ollama wrapper
from ollama import chat  # Ensure Ollama is installed and Gemma3 model is pulled

# --- Define a simple tool ---
def calculator_tool(input_text: str) -> str:
    try:
        # WARNING: eval is unsafe for untrusted input
        return str(eval(input_text))
    except Exception as e:
        return f"Error: {e}"

calc_tool = Tool(
    name="Calculator",
    func=calculator_tool,
    description="Useful for answering math questions"
)

# --- Initialize Gemma3 model ---
chat_model = ChatOllama(model_name="gemma3:1b")  # Make sure this model is pulled locally

# --- Initialize agent ---
agent = initialize_agent(
    tools=[calc_tool],
    llm=chat_model,
    agent="zero-shot-react-description",
    verbose=True
)

# --- Run the agent ---
query = "What is 25 * 4?"
response = agent.run(query)
print("Agent Response:", response)
