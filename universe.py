"""
Second Layer Capital - Quantum Screener Universe Registry
File: universe.py (Root Directory)
"""

# Expanded structural supply chain universe registry
QUANTUM_UNIVERSE = {
    # --- HARDWARE MODALITY ---
    "RGTI": {"name": "Rigetti Computing", "layer": "HARDWARE_MODALITY"},
    "IONQ": {"name": "IonQ Inc.", "layer": "HARDWARE_MODALITY"},
    "QBTS": {"name": "D-Wave Quantum", "layer": "HARDWARE_MODALITY"},
    
    # --- CONTROL SYSTEMS & RF ELECTRONICS ---
    "KEYS": {"name": "Keysight Technologies", "layer": "CONTROL_SYSTEMS_RF"},
    "COHR": {"name": "Coherent Corp.", "layer": "CONTROL_SYSTEMS_RF"},  # Laser delivery networks
    
    # --- CRYOGENICS & ENVIRONMENT ---
    "FORM": {"name": "FormFactor", "layer": "CRYOGENICS_ENVIRONMENT"},
    "LNDB": {"name": "Linde plc", "layer": "CRYOGENICS_ENVIRONMENT"},    # Helium-3 & rare gas logistics
    
    # --- UPSTREAM ADVANCED MATERIALS & ISOTOPES ---
    "CCJ": {"name": "Cameco Corporation", "layer": "UPSTREAM_MATERIALS"}, # Specialized material exposure
    "ASMI": {"name": "ASM International", "layer": "UPSTREAM_MATERIALS"}, # Atomic layer deposition tools
    "LIN": {"name": "Linde plc Material Channel", "layer": "UPSTREAM_MATERIALS"} # High-purity gas deposition
}

if __name__ == "__main__":
    print(f"[✓] Universe file loaded successfully.")
    print(f"Tracking {len(QUANTUM_UNIVERSE)} specialized quantum infrastructure assets.")
