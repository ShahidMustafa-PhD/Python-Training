# Project Optimus-Academic Legacy Version 1.0
# Warning: Do not touch the math logic. It is fragile.

import math

# --- HARDCODED DATA ---
# In a professional app, this should be in a CSV or Database
p_names = ["Satellite-Gimbal", "Bio-Sensor", "Metal-AM-Slicer", "Supply-Chain-AI", "Drone-Control"]
p_costs = [50000, 20000, 0, 45000, 15000] # Note: Project 3 cost is 0 (Crash point)
p_scores = [85, 92, 70, 40, None] # Note: Project 5 has no score (Missing data bug)

total_budget = 100000
spent = 0
allocated_projects = []

print("--- STARTING ALLOCATION PROCESS ---")

# --- THE MONOLITHIC LOOP ---
# This block mixes data validation, math, and reporting
for i in range(len(p_names)):
    name = p_names[i]
    cost = p_costs[i]
    score = p_scores[i]

    # Math Calculation for Efficiency
    # BUG: This will cause a ZeroDivisionError on Project 3
    # BUG: This will cause a TypeError on Project 5 (NoneType)
    efficiency = score / cost 

    # Assessment Logic
    if cost > 40000 and score < 50:
        risk_level = "CRITICAL"
    elif cost == 0:
        risk_level = "UNKNOWN"
    else:
        risk_level = "ACCEPTABLE"

    # Decision Logic
    if spent + cost <= total_budget:
        if risk_level != "CRITICAL":
            spent = spent + cost
            allocated_projects.append(name)
            print("SUCCESS: Allocated " + name + " with efficiency " + str(efficiency))
        else:
            print("REJECTED: " + name + " is too risky.")
    else:
        print("REJECTED: " + name + " exceeds remaining budget.")

# --- FINAL SUMMARY ---
print("-----------------------------------")
print("TOTAL SPENT: " + str(spent))
print("PROJECTS: " + str(allocated_projects))
print("REMAINING: " + str(total_budget - spent))