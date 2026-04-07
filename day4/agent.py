# agent.py

from tools import (
    extract_numbers,
    calculate_sum,
    calculate_average,
    find_max,
    find_min,
    summarize_result
)

# Step planning
def plan_steps(query):
    query = query.lower()
    steps = []

    # Always extract numbers first if any math task
    if any(word in query for word in ["average", "sum", "max", "min"]):
        steps.append("extract_numbers")

    if "sum" in query:
        steps.append("sum")

    if "average" in query:
        steps.append("average")

    if "max" in query:
        steps.append("max")

    if "min" in query:
        steps.append("min")

    if "summarize" in query:
        steps.append("summarize")

    return steps


# Execution with intermediate steps
def run_agent(query):
    steps = plan_steps(query)

    data = None
    result = None
    outputs = []

    for step in steps:

        if step == "extract_numbers":
            data = extract_numbers(query)
            outputs.append(f"[Step 1] Extracted numbers: {data}")

        elif step == "sum":
            result = calculate_sum(data)
            outputs.append(f"[Step 2] Calculated sum: {result}")

        elif step == "average":
            result = calculate_average(data)
            outputs.append(f"[Step 3] Calculated average: {result}")

        elif step == "max":
            result = find_max(data)
            outputs.append(f"[Step 4] Maximum value: {result}")

        elif step == "min":
            result = find_min(data)
            outputs.append(f"[Step 5] Minimum value: {result}")

        elif step == "summarize":
            summary = summarize_result(result)
            outputs.append(f"[Step 6] Summary: {summary}")

    return steps, outputs