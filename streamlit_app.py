from __future__ import annotations

import streamlit as st

from travel_crew_app.models.schemas import UserInvestmentProfile
from travel_crew_app.crew import run_investment_crew


def build_profile_from_ui() -> UserInvestmentProfile:
    goal = st.text_input(
        "Investment goal",
        value="Save for retirement",
        help="Example: retirement, buy a house, general long-term wealth, etc.",
    )

    horizon_years = st.number_input(
        "Investment horizon (years)",
        min_value=1,
        max_value=50,
        value=10,
        step=1,
        help="How long you plan to invest before needing the money.",
    )

    risk_level = st.selectbox(
        "Risk tolerance",
        options=["low", "medium", "high"],
        index=1,
        help="Low = more stable, high = more volatility but higher potential returns.",
    )

    monthly_contribution = st.number_input(
        "Monthly amount you can invest",
        min_value=50.0,
        max_value=100000.0,
        value=200.0,
        step=50.0,
    )

    knowledge_level = st.selectbox(
        "Investment knowledge level",
        options=["beginner", "intermediate", "advanced"],
        index=0,
    )

    return UserInvestmentProfile(
        goal=goal,
        horizon_years=int(horizon_years),
        risk_level=risk_level,
        monthly_contribution=float(monthly_contribution),
        knowledge_level=knowledge_level,
    )


def main() -> None:
    st.set_page_config(
        page_title="Investment Crew Demo",
        page_icon="📈",
        layout="centered",
    )

    st.title("📈 Investment Strategy Crew (Educational)")
    st.markdown(
        """
This app uses a **multi-agent CrewAI setup** with a local LLM (via Ollama)
to generate an **educational investment profile and example portfolio**.

> ⚠️ **Disclaimer**: This is **not** financial advice.  
> It’s only an educational example to understand how such a system could work.
"""
    )

    st.sidebar.header("Your investment profile")
    profile = build_profile_from_ui()

    if st.button("✨ Generate my investment plan"):
        if not profile.goal.strip():
            st.error("Please enter an investment goal.")
            return

        with st.spinner("Agents are analyzing your profile... ⏳"):
            try:
                result = run_investment_crew(profile)
            except Exception as e:
                st.error(f"An error occurred while running the crew: {e}")
                return

        st.success("Done! 🎉")
        st.markdown("---")
        st.subheader("Your Educational Investment Plan")
        st.markdown(result)
    else:
        st.info(
            "Fill in your investment profile on the left, then click "
            "**Generate my investment plan**."
        )


if __name__ == "__main__":
    main()
