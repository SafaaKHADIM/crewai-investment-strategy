from __future__ import annotations

from travel_crew_app.crew import run_travel_crew
from travel_crew_app.ui import ask_user_preferences, print_result


def main() -> None:
    prefs = ask_user_preferences()
    result = run_travel_crew(prefs)
    print_result(result)


if __name__ == "__main__":
    main()
