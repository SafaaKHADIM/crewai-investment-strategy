from __future__ import annotations

from crewai import Crew, Process

from travel_crew_app.models.schemas import UserInvestmentProfile
from travel_crew_app.crew.agents import (
    create_profile_agent,
    create_research_agent,
    create_portfolio_agent,
)
from travel_crew_app.crew.tasks import (
    create_profile_task,
    create_research_task,
    create_portfolio_task,
)


def run_investment_crew(profile: UserInvestmentProfile) -> str:
    """Build agents + tasks, run the investment crew, and return full markdown text."""

    profile_agent = create_profile_agent()
    research_agent = create_research_agent()
    portfolio_agent = create_portfolio_agent()

    profile_task = create_profile_task(profile_agent, profile)
    research_task = create_research_task(research_agent, profile, profile_task)
    portfolio_task = create_portfolio_task(
        portfolio_agent, profile, profile_task, research_task
    )

    crew = Crew(
        agents=[profile_agent, research_agent, portfolio_agent],
        tasks=[profile_task, research_task, portfolio_task],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()
    return str(result)
