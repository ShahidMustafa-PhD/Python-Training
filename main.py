from data_loader import get_project_data
from optimizer import calculate_efficiency, assess_risk

def run_allocation_pipeline(budget: float):
    projects = get_project_data()
    total_spent = 0.0
    approved_list = []

    print(f"{'PROJECT NAME':<20} | {'EFFICIENCY':<10} | {'RISK':<12} | {'STATUS'}")
    print("-" * 60)

    for p in projects:
        name = p['name']
        cost = p['cost']
        score = p['score']

        # Logic 1: Determine Efficiency and Risk
        eff = calculate_efficiency(score, cost)
        risk = assess_risk(cost, score)

        # Logic 2: Selection Criteria
        status = "REJECTED"
        if total_spent + cost <= budget and risk != "CRITICAL" and risk != "DATA_MISSING":
            total_spent += cost
            approved_list.append(name)
            status = "APPROVED"

        print(f"{name:<20} | {eff:<10} | {risk:<12} | {status}")

    print("-" * 60)
    print(f"TOTAL BUDGET UTILIZED: {total_spent} / {budget}")
    print(f"APPROVED PROJECTS: {', '.join(approved_list)}")

if __name__ == "__main__":
    CONSTRAINED_BUDGET = 100000.0
    run_allocation_pipeline(CONSTRAINED_BUDGET)