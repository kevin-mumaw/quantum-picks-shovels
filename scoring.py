"""
Second Layer Capital - Quantum Quantitative Scoring Engine
File: scoring.py (Root Directory)
"""

import os
import json
from universe import QUANTUM_UNIVERSE
from settings import DATA_FOLDER, SCORING_WEIGHTS

def calculate_scores(target_layer: str = None):
    """Computes quantitative scores with optional Ecosystem Layer bottleneck filtering."""
    if target_layer:
        print(f"Initializing Filtered Matrix Target Layer: {target_layer}\n")
    else:
        print("Initializing Global Quantum Screener Scoring Matrix...\n")
        
    final_rankings = []

    for ticker, meta in QUANTUM_UNIVERSE.items():
        # --- BOTTLENECK LAYER FILTERING OPTION ---
        if target_layer and meta["layer"] != target_layer:
            continue
            
        file_path = os.path.join(DATA_FOLDER, f"{ticker}_data.json")
        if not os.path.exists(file_path):
            continue
            
        with open(file_path, "r") as f:
            data = json.load(f)
            
        # Unified Factor Extractors
        revenue = data.get("revenue", 0)
        rd_expense = data.get("research_and_development", 0)
        
        rd_intensity = rd_expense / revenue if revenue > 0 else rd_expense / abs(data.get("annual_burn_rate", 1))

        burn_rate = data.get("annual_burn_rate", 0)
        total_cash = data.get("total_cash", 0)
        
        if burn_rate <= 0:
            cash_runway = 10.0
            is_profitable = True
        else:
            cash_runway = total_cash / burn_rate
            is_profitable = False

        gross_profit = data.get("gross_profit", 0)
        gross_margin = gross_profit / revenue if revenue > 0 else 0.0
        rev_growth = data.get("revenue_growth", 0.20)

        # Normalization Caps
        capped_rd = min(max(rd_intensity, 0.0), 1.0)
        capped_runway = min(max(cash_runway / 5.0, 0.0), 1.0)
        capped_margin = min(max(gross_margin, 0.0), 1.0)
        capped_growth = min(max(rev_growth, -1.0), 1.0)

        total_score = (
            (capped_rd * SCORING_WEIGHTS["RD_INTENSITY"]) +
            (capped_runway * SCORING_WEIGHTS["CASH_RUNWAY"]) +
            (capped_growth * SCORING_WEIGHTS["REVENUE_GROWTH"]) +
            (capped_margin * SCORING_WEIGHTS["MARGIN_DIRECTION"])
        )

        final_rankings.append({
            "ticker": ticker,
            "layer": meta["layer"],
            "final_score": round(total_score, 4),
            "rd_intensity": round(rd_intensity, 2),
            "runway": "Profitable" if is_profitable else f"{round(cash_runway, 1)} Yrs"
        })

    final_rankings.sort(key=lambda x: x["final_score"], reverse=True)

    # Output Display
    if not final_rankings:
        print(" [!] No companies found matching the specified layer filter.")
        return

    print(f"{'RANK':<5}{'TICKER':<8}{'ECOSYSTEM LAYER':<25}{'SCORE':<10}{'R&D INT':<10}{'CASH RUNWAY':<12}")
    print("-" * 70)
    for index, item in enumerate(final_rankings, 1):
        print(f"{index:<5}{item['ticker']:<8}{item['layer']:<25}{item['final_score']:<10}{item['rd_intensity']:<10}{item['runway']:<12}")

if __name__ == "__main__":
    calculate_scores(target_layer=None)

