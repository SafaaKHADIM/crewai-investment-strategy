from __future__ import annotations

from crewai.tools import BaseTool


# -----------------------------
# Simple fake investment product DB
# -----------------------------
FAKE_INVESTMENT_DB = {
    "low": {
        "asset_classes": ["government bonds", "investment-grade bond funds", "money market"],
        "products": [
            {
                "name": "Global Government Bond Index Fund",
                "type": "bond fund",
                "risk": "low",
                "description": "Broad exposure to global government bonds."
            },
            {
                "name": "Short-Term Treasury ETF",
                "type": "ETF",
                "risk": "low",
                "description": "Very short duration government bonds, low volatility."
            },
        ],
    },
    "medium": {
        "asset_classes": ["global equity index funds", "mixed bond/equity funds"],
        "products": [
            {
                "name": "Global Equity Index Fund",
                "type": "index fund",
                "risk": "medium",
                "description": "Diversified global stocks, long-term growth."
            },
            {
                "name": "Balanced 60/40 Fund",
                "type": "fund",
                "risk": "medium",
                "description": "60% stocks, 40% bonds, moderate risk."
            },
        ],
    },
    "high": {
        "asset_classes": ["global equity", "emerging markets", "thematic ETFs"],
        "products": [
            {
                "name": "Emerging Markets Equity ETF",
                "type": "ETF",
                "risk": "high",
                "description": "Higher volatility with higher potential returns."
            },
            {
                "name": "Tech Innovation ETF",
                "type": "ETF",
                "risk": "high",
                "description": "Concentrated in technology and innovation companies."
            },
        ],
    },
}


class InvestmentProductSearchTool(BaseTool):
    """
    Simple local tool that returns example products and asset classes
    for a given risk level.
    """
    name: str = "investment_product_search"
    description: str = (
        "Return example asset classes and products (funds/ETFs) for a given "
        "risk level: low, medium, or high. "
        "Call with: risk_level='low' or 'medium' or 'high'."
    )

    def _run(self, risk_level: str = "medium", **kwargs) -> dict:
        key = (risk_level or "medium").lower().strip()
        return FAKE_INVESTMENT_DB.get(
            key
        )
