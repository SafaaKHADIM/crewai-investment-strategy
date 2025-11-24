from __future__ import annotations

from rich.console import Console
from rich.panel import Panel

from travel_crew_app.models.schemas import UserTravelPreferences

console = Console()


def ask_user_preferences() -> UserTravelPreferences:
    console.print("[bold cyan]Welcome to the Travel Crew demo![/bold cyan]\n")

    destination = input("Where do you want to go? (city / place): ").strip()
    days_raw = input("How many days? (e.g. 3): ").strip() or "3"
    budget_level = (
        input("What is your budget? (low / medium / high): ").strip().lower() or "medium"
    )
    interests = (
        input("What are your interests? (e.g. food, museums, nightlife): ").strip()
        or "food, culture"
    )
    travel_style = (
        input("Travel style? (relaxed / busy / family / adventure...): ").strip()
        or "relaxed"
    )

    try:
        days = int(days_raw)
    except ValueError:
        days = 3

    prefs = UserTravelPreferences(
        destination=destination,
        days=days,
        budget_level=budget_level,
        interests=interests,
        travel_style=travel_style,
    )

    console.print("\n[bold green]Got it! Generating your plan...[/bold green]\n")
    return prefs


def print_result(result: str) -> None:
    """Pretty-print the final text result returned by the crew."""
    console.print(Panel.fit(result, title="Your Travel Plan", border_style="magenta"))
