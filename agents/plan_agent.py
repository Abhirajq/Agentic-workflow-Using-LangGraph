from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import uuid

llm = ChatOpenAI(model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a planning agent. Break down the user's query into atomic sub-tasks for another agent to solve."),
    ("human", "{query}")
])

def plan_agent(state):
    query = state["user_query"]
    chain = prompt | llm
    response = chain.invoke({"query": query})
    
    lines = response.content.strip().split("\n")
    
    # Create structured tasks
    structured_tasks = []
    for i, line in enumerate(lines):
        task_text = line.strip("- ").strip()
        if task_text:
            structured_tasks.append({
                "id": str(uuid.uuid4())[:8],
                "step": i + 1,
                "description": task_text,
                "status": "pending",
                "result": None
            })

    return {
        **state,
        "tasks": structured_tasks
    }

