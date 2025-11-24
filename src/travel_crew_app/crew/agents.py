from __future__ import annotations

from crewai import Agent

from travel_crew_app.config.settings import get_llm
from travel_crew_app.crew.tools import InvestmentProductSearchTool


def create_profile_agent() -> Agent:
    llm = get_llm()

    return Agent(
        role="Investment Profile Analyst",
        goal=(
            "Understand the user's investment goal, horizon, risk level, monthly contribution "
            "and knowledge level, then summarize a clear investment profile."
        ),
        backstory=(
            "You are a patient, educational-focused investment analyst. "
            "You translate raw user information into a structured, easy-to-understand profile."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )


def create_research_agent() -> Agent:
    llm = get_llm()

    return Agent(
        role="Investment Product Researcher",
        goal=(
            "Given the user's investment profile, suggest example asset classes and simple "
            "funds/ETFs that match the risk level and horizon for educational purposes."
        ),
        backstory=(
            "You are familiar with common asset classes (bonds, stocks, index funds, ETFs) "
            "and you explain them simply without giving personalized financial advice."
        ),
        verbose=True,
        allow_delegation=False,
        tools=[InvestmentProductSearchTool()],
        llm=llm,
    )


def create_portfolio_agent() -> Agent:
    llm = get_llm()

    return Agent(
        role="Portfolio Builder (Educational)",
        goal=(
            "Build an example high-level portfolio allocation (percentages by asset class) "
            "and a simple monthly investment plan, based on the user's profile and the "
            "suggested products. Emphasize that this is educational, not financial advice."
        ),
        backstory=(
            "You like to create simple model portfolios like 80/20 or 60/40 allocations and "
            "explain them in a friendly way, focusing on long-term investing principles."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )
