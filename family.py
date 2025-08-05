# =============================================
# Family Class with Inheritance
# =============================================

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def add_member(self, name, age, role):
        """Add a new member to the family"""
        self.members.append({"name": name, "age": age, "role": role})

    def get_members(self):
        """Return all family members"""
        return self.members

    def describe(self):
        """Print family description"""
        print(f"\nThe {self.last_name} Family:")
        for member in self.members:
            print(f"- {member['name']} ({member['role']}, {member['age']} years old)")


class ModernFamily(Family):
    def __init__(self, last_name, hometown):
        super().__init__(last_name)
        self.hometown = hometown

    def describe(self):
        """Override describe() to include hometown"""
        print(f"\nThe {self.last_name} Family from {self.hometown}:")
        for member in self.members:
            print(f"- {member['name']} ({member['role']}, {member['age']} years old)")


# =============================================
# Polymorphism Challenge (Vehicles)
# =============================================

class Vehicle:
    def move(self):
        pass  # Abstract method


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


# =============================================
# Demonstration Code
# =============================================

if __name__ == "__main__":
    print("=== Family Class Demonstration ===")
    
    # Traditional family
    smiths = Family("Smith")
    smiths.add_member("John", 40, "Father")
    smiths.add_member("Jane", 38, "Mother")
    smiths.describe()

    # Modern family
    gomez_family = ModernFamily("Gomez", "Miami")
    gomez_family.add_member("Alex", 30, "Son")
    gomez_family.add_member("Eva", 28, "Daughter")
    gomez_family.describe()

    print("\n=== Polymorphism Challenge ===")
    vehicles = [Car(), Plane()]
    for vehicle in vehicles:
        vehicle.move()
