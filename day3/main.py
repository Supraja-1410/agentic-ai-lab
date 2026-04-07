# main.py

from agent import run_agent
from logger import log

while True:
    query = input("Enter query (type 'exit' to quit): ")

    # Exit condition
    if query.lower() == "exit":
        print("Exiting program...")
        break

    tool, output = run_agent(query)

    print("Tool used:", tool)
    print("Output:", output)

    log(query, tool, output)