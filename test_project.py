#March 21, 2024
#Final Project Test

from project import calculate_area_circle, solve_quadratic, calculate_volume_sphere

def test_calculate_area_circle():
    assert calculate_area_circle(10) == 314.1592653589793

def test_solve_quadratic():
    assert solve_quadratic(1, -3, 2) == (2.0, 1.0)
    assert solve_quadratic(1, 2, 1) == -1.0
    assert solve_quadratic(1, 0, 1) == "No real roots"

def test_calculate_volume_sphere():
    assert calculate_volume_sphere(10) == 4188.790204786391

