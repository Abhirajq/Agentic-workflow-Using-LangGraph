# README.md

# 🧠 Agentic Workflow using LangGraph

This project implements an **agentic AI workflow** using [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://www.langchain.com/), and OpenAI's GPT models. It features autonomous planning, tool execution, and self-reflection using LLM agents, all orchestrated in a graph-based system.

---

## 🚀 Features

- **🔧 PlanAgent** – Splits complex user queries into atomic sub-tasks.
- **⚙️ ToolAgent** – Executes sub-tasks using simple tools (math, explanation, etc.).
- **🔁 Reflection Agent** – Adds feedback and retry logic for failed or weak tasks.
- **🕸️ LangGraph** – Graph-based execution engine managing agent transitions.
- **🌐 Streamlit UI** – User-friendly web interface for interaction.

---

## 🗂️ Project Structure
```
agentic-workflow-langgraph/
├── agents/
│   ├── plan_agent.py         # Task decomposition logic
│   ├── tool_agent.py         # Sub-task execution logic
│   └── reflection_agent.py   # Task review and retry logic
├── utils/
│   └── helpers.py            # Simulated tools (math, explanation, etc.)
├── langgraph_workflow.py     # LangGraph workflow definition
├── app.py                    # Streamlit web interface
├── main.py                   # CLI runner (optional)
├── requirements.txt          # Python dependencies
├── .env                      # OpenAI API key (not committed)
└── README.md                 # Project guide (this file)
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/agentic-workflow-langgraph.git
cd agentic-workflow-langgraph
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Create a `.env` file:
```env
OPENAI_API_KEY=your_openai_key_here
```

---

## ▶️ Running the App

### Option 1: CLI
```bash
python main.py
```
You’ll be prompted to enter a query in the terminal.

### Option 2: Streamlit Web UI
```bash
streamlit run app.py
```

Then visit: [http://localhost:8501](http://localhost:8501)

---

## 🌍 Hosting (Optional)
You can deploy this app for free using [Streamlit Cloud](https://streamlit.io/cloud):
1. Push the repo to GitHub.
2. Go to Streamlit Cloud and link your repo.
3. Set `app.py` as the entry point.
4. Add your OpenAI key in the **Secrets** tab.

---

## 📹 Deliverables (For Evaluation)
- ✅ **GitHub Repo** (this)
- ✅ **Hosted Streamlit App**
- ✅ **Video Walkthrough** (5–10 mins showing workflow, code, and logic)

---

## 💡 Example Queries
Try these:
- `Explain LangGraph and calculate 5 * (2 + 3)`
- `What is RAG in AI and what is 20 * 4`  

---

## 📚 License
MIT License – free for personal and commercial use.

---

## 🙌 Acknowledgments
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://www.langchain.com/)
- [OpenAI](https://openai.com/)


