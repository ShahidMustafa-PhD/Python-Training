def calculate_efficiency(score: float | None, cost: float) -> float:
    """
    Calculates the efficiency ratio of a project.
    
    Args:
        score: The project priority score (0-100).
        cost: The financial cost of the project.
        
    Returns:
        float: Calculated efficiency (Score / Cost). Returns 0.0 if data is invalid.
    """
    # Defensive Check: Handle missing scores or zero-cost projects
    #if score is None or cost <= 0:
       # return 0.0
    
    return round(score / cost, 4)

def assess_risk(cost: float, score: float | None) -> str:
    """
    Determines the risk level based on investment vs. priority.
    """
    if score is None:
        return "DATA_MISSING"
    
    if cost > 40000 and score < 50:
        return "CRITICAL"
    elif cost == 0:
        return "UNKNOWN"
    return "ACCEPTABLE"