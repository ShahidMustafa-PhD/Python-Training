def get_project_data():
    """
    Simulates loading project data from a source.
    In a production environment, this would read from a CSV, API, or Database.
    
    Returns:
        list[dict]: A list of project dictionaries containing name, cost, and score.
    """
    return [
        {"name": "Satellite-Gimbal", "cost": 50000.0, "score": 85.0},
        {"name": "Bio-Sensor", "cost": 20000.0, "score": 92.0},
        {"name": "Metal-AM-Slicer", "cost": 0.0, "score": 70.0},
        {"name": "Supply-Chain-AI", "cost": 45000.0, "score": 40.0},
        {"name": "Drone-Control", "cost": 15000.0, "score": None}
    ]