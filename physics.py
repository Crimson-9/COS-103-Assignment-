"""
Five Common Physics Formulas
"""

def kinetic_energy(mass, velocity):
    """KE = 1/2 * m * v^2  (Joules)"""
    return 0.5 * mass * velocity ** 2


def newtons_second_law(mass, acceleration):
    """F = m * a  (Newtons)"""
    return mass * acceleration


def gravitational_force(m1, m2, distance, G=6.674e-11):
    """F = G * (m1 * m2) / r^2  (Newtons)"""
    return G * (m1 * m2) / distance ** 2


def ohms_law(voltage=None, current=None, resistance=None):
    """V = I * R  -- pass any two values, get the third."""
    if voltage is None:
        return current * resistance
    elif current is None:
        return voltage / resistance
    elif resistance is None:
        return voltage / current
    else:
        raise ValueError("Provide exactly two known values, leave one as None.")


def final_velocity(initial_velocity, acceleration, time):
    """v = u + a * t  (m/s)"""
    return initial_velocity + acceleration * time


if __name__ == "__main__":
    print("Kinetic Energy (2 kg, 3 m/s):", kinetic_energy(2, 3), "J")
    print("Force (5 kg, 2 m/s^2):", newtons_second_law(5, 2), "N")
    print("Gravitational Force (5.97e24 kg, 70 kg, 6.37e6 m):",
          gravitational_force(5.97e24, 70, 6.37e6), "N")
    print("Ohm's Law - Current (12 V, 4 ohm):", ohms_law(voltage=12, resistance=4), "A")
    print("Final Velocity (0 m/s, 9.8 m/s^2, 5 s):", final_velocity(0, 9.8, 5), "m/s")

    input("\nPress Enter to exit...")