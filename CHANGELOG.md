# Changelog
All notable changes to the Second Layer Capital Quantum Ecosystem Screener will be documented in this file.

## - 2026-06-25
### Added
* **Universe Registry (`universe.py`)**: Initialized a 5-ticker pure-play tracking registry covering core hardware, control system RF, and cryogenic infrastructure enablers.
* **Screener Configurations (`settings.py`)**: Established baseline multi-factor scoring weights emphasizing R&D Intensity (40%) and Cash Runway (30%).
* **Ingestion Pipeline (`ingestion.py`)**: Implemented a localized file storage data builder creating raw JSON assets inside a dedicated directory.
* **Scoring Matrix (`scoring.py`)**: Built a flat quantitative ranking engine running standalone dictionary sorts to generate leaderboard output tables.
* **Corporate Licensing (`LICENSE`)**: Applied an official corporate MIT license attributing complete project ownership to Second Layer Capital.
* **Repository Documentation (`README.md`)**: Drafted an institutional-grade codebase blueprint and operational execution guide.

### Security
* **Git Version Control**: Cleaned environment paths and configured explicit local `.gitignore` rules to completely lock out background caching (`__pycache__/`) and local financial storage files (`data_storage/`) from cloud tracking.
