"""A tiny AI agent, in pure Python.

It thinks, uses a tool, looks at the result, and loops until the goal is
done. No API key, no cost, no setup. It runs with plain Python.

In a real agent, a language model makes the decisions inside decide_action().
Here we use simple rules instead, so you can see the loop clearly without
needing any account or key. Once you understand this loop, you understand
the heart of every AI agent.
"""

import re


# ---- The tools: the agent's "hands" ----

def calculator(expression):
    """Work out a simple math expression like '12 * 8'."""
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        return "I can only handle simple math."
    try:
        return str(eval(expression))
    except Exception:
        return "That calculation did not work."


WEATHER = {
    "accra": "31C and sunny",
    "london": "14C and rainy",
    "new york": "22C and cloudy",
}


def weather(city):
    """Look up the weather for a city we know about."""
    return WEATHER.get(city.lower(), "I do not have the weather for that city.")


# ---- The brain: decides the next step ----

def decide_action(task, memory):
    """Look at the goal and what we have already done, then pick one next
    step. Returns (tool, tool_input, thought).

    This is the part a language model would handle in a real agent.
    """
    done_tools = {step["tool"] for step in memory}

    # Is there a calculation we have not solved yet?
    math_match = re.search(r"(\d+\s*[-+*/]\s*\d+)", task)
    if math_match and "calculator" not in done_tools:
        expression = math_match.group(1)
        return "calculator", expression, f"There is a calculation here: {expression}. I will use the calculator."

    # Is there a city whose weather we have not checked yet?
    weather_match = re.search(r"weather in ([a-zA-Z ]+)", task.lower())
    if weather_match and "weather" not in done_tools:
        city = weather_match.group(1).strip()
        return "weather", city, f"The goal asks about the weather in {city}. I will use the weather tool."

    # Nothing left to do, so it is time to answer.
    return "final_answer", None, "I have everything I need. Time to answer."


# ---- The loop: think, act, look, repeat ----

def run_agent(task, max_steps=5):
    print(f"GOAL: {task}\n")
    memory = []

    for step in range(1, max_steps + 1):
        tool, tool_input, thought = decide_action(task, memory)
        print(f"Step {step}")
        print(f"  Thought: {thought}")

        if tool == "final_answer":
            pieces = []
            for item in memory:
                if item["tool"] == "calculator":
                    pieces.append(f"{item['input']} = {item['result']}")
                elif item["tool"] == "weather":
                    pieces.append(f"the weather in {item['input']} is {item['result']}")
            print("  Action : give the final answer\n")
            print("FINAL ANSWER: " + ", and ".join(pieces) + ".")
            return

        result = calculator(tool_input) if tool == "calculator" else weather(tool_input)
        print(f"  Action : {tool}('{tool_input}')")
        print(f"  Observation: {result}\n")
        memory.append({"tool": tool, "input": tool_input, "result": result})

    print("Reached the step limit without finishing.")


if __name__ == "__main__":
    run_agent("What is 12 * 8, and what is the weather in Accra?")
