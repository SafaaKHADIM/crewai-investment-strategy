# LangGraph vs CrewAI  
**Differences, Tools Integration, and When to Use Each**

---

## 1. Summary

| Aspect                      | LangGraph                                           | CrewAI                                                     |
|-----------------------------|----------------------------------------------------|------------------------------------------------------------|
| Primary mental model        | **Stateful workflow / graph**                      | **Team of agents + tasks (crew)**                          |
| Core abstraction            | State + Nodes + Edges                              | Agents + Tasks + (optionally) Flows                        |
| Control flow                | Sequential, branching, loops, parallel, retries    | Mainly sequential, some hierarchical flows                 |
| Short-term memory           | **Explicit state fields**                          | Agent-level memory + task context                          |
| Tools integration           | **Direct, flexible, explicit node-level tools**    | Simple but less granular; tool calls go through agents     |
| Best for                    | Complex, tool-heavy, long-running workflows        | Multi-agent pipelines, content workflows, demos            |
| Difficulty / learning curve | Higher                                              | Lower                                                      |
| Typical usage               | Backend orchestration systems                      | Rapid prototypes, agent demos, simpler internal tools      |

---

## 2. Mental Models

### 2.1 LangGraph: “Workflow / Orchestration Engine”

LangGraph treats your application like a **graph of states and nodes**:

- Each node can be a tool, agent, function, API call, or model.
- The **state** flows between nodes.
- You decide how nodes connect (sequential, branches, loops, merges).

> Think: *Airflow + LLMs*, but interactive and stateful.

---

### 2.2 CrewAI: “Team of Agents Working Through Tasks”

CrewAI focuses on **agents** with roles (**Researcher**, **Writer**, **Reviewer**) executing **tasks** in order.

- Simple sequential flow.
- Context passed automatically.
- Great for content pipelines and agent-style workflows.

> Think: *a team of AI co-workers*.

---

## 3. State, Memory & Context

### 3.1 LangGraph: State = the Only Memory (Explicit)

LangGraph’s short-term memory = the `state`:

```python
class WorkflowState(TypedDict):
    messages: list
    results: dict
    errors: list
