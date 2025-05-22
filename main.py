# main.py
from langgraph_workflow import run_workflow
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    query = input("Enter your query: ")
    result = run_workflow(query)
    print("\nFinal Output:")
    print(result)
