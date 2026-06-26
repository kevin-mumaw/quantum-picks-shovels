"""
Second Layer Capital - Quantum Screener Configuration
File: settings.py (Root Directory)
"""

import os
from pathlib import Path

# File System Paths
BASE_DIR = Path(__file__).resolve().parent
DATA_FOLDER = os.path.join(str(BASE_DIR), "data_storage")

# API Configuration Connection Settings
# Defaulting to Financial Modeling Prep (FMP) endpoint structures
API_KEY = os.getenv("FMP_API_KEY", "demo")  # Falls back to "demo" mode if no key is found
BASE_URL = "https://financialmodelingprep.com"

# Operational Rate Limiting Safeguards
TIMEOUT_SECONDS = 15
RATE_LIMIT_DELAY = 1.0  # Safe 1-second delay execution between HTTP requests

# Strategic operational metrics weighting (Must equal 1.0)
SCORING_WEIGHTS = {
    "RD_INTENSITY": 0.40,      # R&D Expense / Total Revenue
    "CASH_RUNWAY": 0.30,       # Total Cash / Annual Net Burn Rate
    "REVENUE_GROWTH": 0.15,    # Year-over-Year Revenue Growth
    "MARGIN_DIRECTION": 0.15   # Gross Margin optimization
}

if __name__ == "__main__":
    print(f"[✓] Settings loaded.")
    print(f"Target local cache path: {DATA_FOLDER}")
