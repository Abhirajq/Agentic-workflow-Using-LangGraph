# agents/reflection_agent.py
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a reflection agent. Review the task result and provide feedback. If the result is bad or incomplete, suggest how to fix or retry."),
    ("human", "Task: {task}\nResult: {result}\nShould we retry or revise?")
])

def reflect_agent(state):
    tasks = state.get("tasks", [])
    revised_tasks = []

    for task in tasks:
        if task["status"] == "complete":
            # Assume okay, but reflect anyway
            revised_tasks.append(task)
        elif task["status"] == "failed" or task["result"] == "This sub-task was executed. No specific tool matched, so a placeholder result is returned.":
            # Ask the reflection agent
            chain = prompt | llm
            feedback = chain.invoke({
                "task": task["description"],
                "result": task["result"]
            })
            suggestion = feedback.content.strip()

            # Add retry with modified task
            new_description = suggestion.replace("Revised Task:", "").strip()
            revised_tasks.append({
                "id": task["id"] + "-r",
                "step": task["step"],
                "description": new_description,
                "status": "pending",
                "result": None
            })
        else:
            revised_tasks.append(task)

    return {
        **state,
        "tasks": revised_tasks
    }
