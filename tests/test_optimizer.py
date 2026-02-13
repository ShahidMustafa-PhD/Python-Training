#import pytest
from optimizer import calculate_efficiency, assess_risk

def test_calculate_efficiency_nominal():
    """Test standard valid input."""
    # Score 80, Cost 400 -> 80/400 = 0.2
    assert calculate_efficiency(80.0, 400.0) == 0.2

def test_calculate_efficiency_zero_division():
    """Test that zero cost returns 0.0 instead of crashing."""
    # This specifically addresses the bug in the legacy code
    assert calculate_efficiency(70.0, 0.0) == 0.0

def test_calculate_efficiency_missing_data():
    """Test that a None score returns 0.0."""
    assert calculate_efficiency(None, 15000.0) == 0.0

def test_assess_risk_critical():
    """Test the 'Critical' logic for high cost/low score."""
    # Cost > 40000 and Score < 50
    assert assess_risk(50000.0, 30.0) == "CRITICAL"

def test_assess_risk_acceptable():
    """Test standard acceptable project."""
    assert assess_risk(10000.0, 90.0) == "ACCEPTABLE"

def test_assess_risk_missing_score():
    """Test behavior when a score is not provided."""
    assert assess_risk(15000.0, None) == "DATA_MISSING"