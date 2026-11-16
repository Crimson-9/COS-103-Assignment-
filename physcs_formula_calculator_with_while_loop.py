"""
Five Common Physics Formulas (Interactive Console App)
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


def main():
    while True:
        print("\n" + "=" * 40)
        print("    PHYSICS FORMULA CALCULATOR")
        print("=" * 40)
        print("1. Kinetic Energy (KE = 1/2 * m * v^2)")
        print("2. Newton's Second Law (F = m * a)")
        print("3. Gravitational Force (F = G * m1 * m2 / r^2)")
        print("4. Ohm's Law (V = I * R)")
        print("5. Final Velocity (v = u + a * t)")
        print("6. Exit")
        
        choice = input("\nSelect a formula (1-6): ").strip()

        if choice == "1":
            print("\n--- Kinetic Energy ---")
            m = float(input("Enter mass (kg): "))
            v = float(input("Enter velocity (m/s): "))
            result = kinetic_energy(m, v)
            print(f"Kinetic Energy = {result} J")

        elif choice == "2":
            print("\n--- Newton's Second Law ---")
            m = float(input("Enter mass (kg): "))
            a = float(input("Enter acceleration (m/s^2): "))
            result = newtons_second_law(m, a)
            print(f"Force = {result} N")

        elif choice == "3":
            print("\n--- Gravitational Force ---")
            m1 = float(input("Enter mass 1 (kg): "))
            m2 = float(input("Enter mass 2 (kg): "))
            r = float(input("Enter distance between centers (m): "))
            result = gravitational_force(m1, m2, r)
            print(f"Gravitational Force = {result} N")

        elif choice == "4":
            print("\n--- Ohm's Law ---")
            print("Select what you want to calculate:")
            print("  a. Voltage (V = I * R)")
            print("  b. Current (I = V / R)")
            print("  c. Resistance (R = V / I)")
            sub_choice = input("Choice (a/b/c): ").strip().lower()

            if sub_choice == "a":
                i = float(input("Enter current (A): "))
                r = float(input("Enter resistance (ohms): "))
                print(f"Voltage = {ohms_law(current=i, resistance=r)} V")
            elif sub_choice == "b":
                v = float(input("Enter voltage (V): "))
                r = float(input("Enter resistance (ohms): "))
                print(f"Current = {ohms_law(voltage=v, resistance=r)} A")
            elif sub_choice == "c":
                v = float(input("Enter voltage (V): "))
                i = float(input("Enter current (A): "))
                print(f"Resistance = {ohms_law(voltage=v, current=i)} ohms")
            else:
                print("Invalid Ohm's law choice!")

        elif choice == "5":
            print("\n--- Final Velocity ---")
            u = float(input("Enter initial velocity (m/s): "))
            a = float(input("Enter acceleration (m/s^2): "))
            t = float(input("Enter time (s): "))
            result = final_velocity(u, a, t)
            print(f"Final Velocity = {result} m/s")

        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()