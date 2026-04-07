# tools.py

def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Error in calculation"

def weather(city):
    return f"Weather in {city} is sunny (mock data)"

def summarize(text):
    return text[:50] + "..."