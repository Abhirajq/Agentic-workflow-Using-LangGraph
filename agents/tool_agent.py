from utils.helpers import run_tool

def tool_agent(state):
    tasks = state.get("tasks", [])
    completed = []

    for task in tasks:
        try:
            task_result = run_tool(task["description"])
            task["status"] = "complete"
            task["result"] = task_result
        except Exception as e:
            task["status"] = "failed"
            task["result"] = f"Error: {str(e)}"
        completed.append(task)

    return {
        **state,
        "tasks": completed
    }

