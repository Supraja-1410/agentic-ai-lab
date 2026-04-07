# logger.py

def log(input_text, tool, output):
    with open("logs.txt", "a") as f:
        f.write(f"INPUT: {input_text}\n")
        f.write(f"TOOL: {tool}\n")
        f.write(f"OUTPUT: {output}\n")
        f.write("-" * 40 + "\n")