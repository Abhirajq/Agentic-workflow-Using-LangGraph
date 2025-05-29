from langgraph.graph import StateGraph
from agents.plan_agent import plan_agent
from agents.tool_agent import tool_agent
from agents.reflection_agent import reflect_agent

class AgentState(dict):
    pass

def run_workflow(query: str):
    state = AgentState()
    state["user_query"] = query

    builder = StateGraph(AgentState)

    # Add nodes
    builder.add_node("planner", plan_agent)
    builder.add_node("executor", tool_agent)
    builder.add_node("reflector", reflect_agent)

    # Define flow
    builder.set_entry_point("planner")
    builder.add_edge("planner", "executor")
    builder.add_edge("executor", "reflector")
    builder.set_finish_point("reflector")

    graph = builder.compile()
    return graph.invoke(state)

