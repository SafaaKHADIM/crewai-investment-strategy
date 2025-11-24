from __future__ import annotations

from pydantic import BaseModel, Field


class UserInvestmentProfile(BaseModel):
    goal: str = Field(
        ...,
        description="Main investment goal, e.g. retirement, buy a house, general wealth."
    )
    horizon_years: int = Field(
        ...,
        gt=0,
        le=50,
        description="Investment horizon in years.",
    )
    risk_level: str = Field(
        ...,
        description="Risk tolerance: low, medium, or high.",
    )
    monthly_contribution: float = Field(
        ...,
        gt=0,
        description="Approximate amount user can invest per month.",
    )
    knowledge_level: str = Field(
        default="beginner",
        description="Investment knowledge level: beginner, intermediate, advanced.",
    )
