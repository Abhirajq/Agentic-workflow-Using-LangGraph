import math

def run_tool(task: str) -> str:
    task_lower = task.lower()

    # Math solver
    if "calculate" in task_lower or any(char.isdigit() for char in task):
        try:
            expression = task_lower.replace("calculate", "").strip()
            result = eval(expression)
            return f"Math Result: {result}"
        except:
            return "Could not solve math expression."

    # Keyword explanation
    elif "explain" in task_lower:
        keyword = task_lower.replace("explain", "").strip()
        return f"{keyword.title()} is a concept that you'd usually describe in detail. This is a placeholder explanation."

    # Default fallback
    return "This sub-task was executed. No specific tool matched, so a placeholder result is returned."


