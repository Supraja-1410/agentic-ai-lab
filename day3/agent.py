# agent.py

from tools import calculator, weather, summarize

# Simulated LLM decision-making
def decide_tool(query):
    query = query.lower()

    # Simulating "intelligent" decision
    if "calculate" in query or "+" in query or "-" in query or "*" in query or "/" in query:
        return "calculator"

    elif "weather" in query:
        return "weather"

    elif "summarize" in query:
        return "summarize"

    else:
        return "unknown"


# Agent execution
def run_agent(query):
    tool = decide_tool(query)

    if tool == "calculator":
        expression = query.replace("calculate", "").strip()
        output = calculator(expression)

    elif tool == "weather":
        output = weather(query)

    elif tool == "summarize":
        output = summarize(query)

    else:
        output = "I don't understand"

    return tool, output