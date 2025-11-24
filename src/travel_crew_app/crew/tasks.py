from __future__ import annotations

from crewai import Task
from crewai import Agent

from travel_crew_app.models.schemas import UserInvestmentProfile


def create_profile_task(profile_agent: Agent, profile: UserInvestmentProfile) -> Task:
    description = (
        "Analyze the user's investment information and produce a clear, structured profile.\n\n"
        f"Goal: {profile.goal}\n"
        f"Horizon (years): {profile.horizon_years}\n"
        f"Risk level: {profile.risk_level}\n"
        f"Monthly contribution: {profile.monthly_contribution}\n"
        f"Knowledge level: {profile.knowledge_level}\n\n"
        "You must:\n"
        "- Identify the user's main objective (capital preservation vs growth).\n"
        "- Interpret the risk level and horizon.\n"
        "- Summarize their constraints and opportunities.\n"
        "- Present the result as a short, structured profile with headings."
    )

    expected_output = (
        "A markdown section titled 'Investment Profile' with bullet points summarizing "
        "goal, horizon, risk tolerance, and contribution capacity."
    )

    return Task(
        description=description,
        agent=profile_agent,
        expected_output=expected_output,
        markdown=True,
    )


def create_research_task(
    research_agent: Agent, profile: UserInvestmentProfile, profile_task: Task
) -> Task:
    description = (
        "Read the investment profile from the context.\n\n"
        f"Risk level: {profile.risk_level}\n"
        f"Horizon (years): {profile.horizon_years}\n"
        f"Knowledge level: {profile.knowledge_level}\n\n"
        "👉 You MUST call the investment_product_search tool EXACTLY ONCE using:\n"
        "       investment_product_search(risk_level='<low|medium|high>')\n\n"
        "After calling the tool and receiving the result:\n"
        "👉 You MUST return a normal MARKDOWN ANSWER.\n"
        "👉 DO NOT call any tool as the final answer.\n"
        "👉 DO NOT wrap your final answer in a tool call.\n"
        "👉 Your final output must be ONLY human-readable markdown.\n\n"
        "Your task:\n"
        "- List 2–4 asset classes appropriate for the profile\n"
        "- Choose 3–5 example products from the tool output\n"
        "- Explain each product simply\n"
        "- Add a disclaimer: 'Educational only, not financial advice.'"
    )

    expected_output = (
        "A markdown section with headings:\n"
        "## Suggested Asset Classes\n"
        "## Example Products\n"
        "And a short explanation paragraph.\n\n"
        "NO tool call in the final answer."
    )

    return Task(
        description=description,
        agent=research_agent,
        expected_output=expected_output,
        context=[profile_task],
        markdown=True,
        allow_code_execution=False,   # important: stops weird behaviors
    )



def create_portfolio_task(
    portfolio_agent: Agent,
    profile: UserInvestmentProfile,
    profile_task: Task,
    research_task: Task,
) -> Task:
    description = (
        "Build an example portfolio allocation and monthly plan.\n\n"
        f"Goal: {profile.goal}\n"
        f"Horizon (years): {profile.horizon_years}\n"
        f"Risk level: {profile.risk_level}\n"
        f"Monthly contribution: {profile.monthly_contribution}\n\n"
        "Use the investment profile and product suggestions in the context.\n"
        "You must:\n"
        "- Propose a simple allocation by percentage (e.g. 70% global equity, 30% bonds).\n"
        "- Suggest how the monthly contribution could be split across 2–4 products.\n"
        "- Include a short explanation of the strategy (diversification, long-term view, etc.).\n"
        "- Add a clear disclaimer that this is NOT financial advice, only an educational example."
    )

    expected_output = (
        "A markdown section titled 'Example Portfolio & Plan' with:\n"
        "- A bullet list of asset classes with percentages.\n"
        "- A bullet list of products with approximate monthly amounts.\n"
        "- A short paragraph explaining the rationale and a disclaimer."
    )

    return Task(
        description=description,
        agent=portfolio_agent,
        expected_output=expected_output,
        context=[profile_task, research_task],
        markdown=True,
    )
