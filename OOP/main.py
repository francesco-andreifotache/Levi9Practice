from math import sqrt

class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if self.exist_contact(contact.phone_number):
            print("Phone number already exists")
        else:
            self.contacts.append(contact)

    def remove_contact(self, phone_number):
        for contact in self.contacts:
            if contact.phone_number == phone_number:
                self.contacts.remove(contact)
                return
        print("Contact does not exist")

    def exist_contact(self, phone_number):
        for contact in self.contacts:
            if contact.phone_number == phone_number:
                return True
        return False

    def display_contacts(self):
        print("Contacts:")
        for contact in self.contacts:
            print(contact)


class Friend:
    def __init__(self,name, phone_number, favorite_activity):
        self.favorite_activity = favorite_activity
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} => {self.phone_number} {self.favorite_activity}"

    def __eq__(self, other):
        return self.name == other.name and self.phone_number == other.phone_number

class Colleague:
    def __init__(self, name, phone_number, place_of_work):
        self.name = name
        self.phone_number = phone_number
        self.place_of_work = place_of_work

    def __str__(self):
        return f"{self.name} => {self.phone_number} {self.place_of_work}"

    def __eq__(self, other):
        return self.name == other.name and self.phone_number == other.phone_number

class Relative:
    def __init__(self, name, phone_number, type_of_relative):
        self.name = name
        self.phone_number = phone_number
        self.type_of_relative = type_of_relative

    def __str__(self):
        return f"{self.name} => {self.phone_number} {self.type_of_relative}"

    def __eq__(self, other):
        return self.name == other.name and self.phone_number == other.phone_number


p = PhoneBook()

f = Friend("Alex", "0764322212", "Football")
c = Colleague("Maria", "0764322213", "Google")
r = Relative("John", "0764322211", "Brother")

p.add_contact(f)
p.add_contact(c)
p.add_contact(r)

print(p.exist_contact("0764322211"))
print(f == c)

p.remove_contact("0764322212")

p.display_contacts()


# Problema 2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


class PointCollection:
    def __init__(self, points=None):
        self.points = points if points is not None else []

    def add_point(self, point):
        self.points.append(point)

    def remove_point(self, point):
        if point in self.points:
            self.points.remove(point)

    def __contains__(self, point):
        return point in self.points

    def __len__(self):
        return len(self.points)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __eq__(self, other):
        return len(self) == len(other)

    def __add__(self, other):
        result = PointCollection(self.points.copy())

        if isinstance(other, Point):
            for i in range(len(result.points)):
                result.points[i] = result.points[i] + other

        elif isinstance(other, PointCollection):
            result.points.extend(other.points)

        return result

    def __sub__(self, other):
        result = PointCollection(self.points.copy())

        if isinstance(other, Point):
            result.remove_point(other)

        elif isinstance(other, PointCollection):
            for p in other.points:
                result.remove_point(p)

        return result

    def __str__(self):
        return "[" + ", ".join(str(p) for p in self.points) + "]"

pc = PointCollection([Point(1,2), Point(3,4)])
pc2 = pc + PointCollection([(1,1)])

print(pc2)

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        if self.area() == 0:
            raise ValueError("Invalid triangle: points are collinear")

    def area(self):
        return abs(
            self.p1.x * (self.p2.y - self.p3.y) +
            self.p2.x * (self.p3.y - self.p1.y) +
            self.p3.x * (self.p1.y - self.p2.y)
        ) / 2

    def __len__(self):
        return int(self.area())

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __contains__(self, item):
        # point in triangle
        if isinstance(item, Point):
            return self._point_in_triangle(item)

        # triangle in triangle (area-based simple check)
        if isinstance(item, Triangle):
            return item.area() <= self.area()

        # collection in triangle
        if isinstance(item, PointCollection):
            return all(self._point_in_triangle(p) for p in item.points)

        return False

    def _point_in_triangle(self, p):
        t = Triangle(self.p1, self.p2, p).area()
        t2 = Triangle(self.p2, self.p3, p).area()
        t3 = Triangle(self.p3, self.p1, p).area()
        return abs((t + t2 + t3) - self.area()) < 1e-6

    def __str__(self):
        return f"Triangle({self.p1}, {self.p2}, {self.p3})"


class Rectangle:
    def __init__(self, p1, p2, p3, p4):
        self.points = [p1, p2, p3, p4]

        if not self._is_valid_rectangle():
            raise ValueError("Invalid rectangle")

    def _dist(self, a, b):
        return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

    def area(self):
        # assumes ordered rectangle
        return self._dist(self.points[0], self.points[1]) * \
               self._dist(self.points[1], self.points[2])

    def __len__(self):
        return int(self.area())

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __contains__(self, item):
        # point inside rectangle (bounding box check)
        if isinstance(item, Point):
            xs = [p.x for p in self.points]
            ys = [p.y for p in self.points]
            return min(xs) <= item.x <= max(xs) and min(ys) <= item.y <= max(ys)

        # collection inside rectangle
        if isinstance(item, PointCollection):
            return all(p in self for p in item.points)

        # rectangle inside rectangle (area check simplification)
        if isinstance(item, Rectangle):
            return item.area() <= self.area()

        return False

    def _is_valid_rectangle(self):
        # simple validation: 2 distinct side lengths + equal diagonals
        d = [self._dist(self.points[i], self.points[(i+1) % 4]) for i in range(4)]
        diag1 = self._dist(self.points[0], self.points[2])
        diag2 = self._dist(self.points[1], self.points[3])

        return (
            len(set(round(x, 5) for x in d)) <= 2 and
            abs(diag1 - diag2) < 1e-5
        )

    def __str__(self):
        return f"Rectangle({', '.join(str(p) for p in self.points)})"

t = Triangle(Point(0, 0), Point(4, 0), Point(0, 3))
print("Triangle area:", len(t))

r = Rectangle(
    Point(0, 0),
    Point(4, 0),
    Point(4, 2),
    Point(0, 2)
    )
print("Rectangle area:", len(r))

# Problema 3

class Contact:
    def __init__(self, unique_id, name, phone_number, online=False, blocked=False):
        self.unique_id = unique_id
        self.name = name
        self.phone_number = phone_number
        self.online = online
        self.blocked = blocked

    def __str__(self):
        status = "Online" if self.online else "Offline"
        block = "Blocked" if self.blocked else "Active"
        return f"{self.unique_id} | {self.name} | {self.phone_number} | {status} | {block}"


class ChatApp:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if self._phone_exists(contact.phone_number):
            print("Phone number already exists")
            return
        self.contacts.append(contact)

    def remove_contact(self, phone_number):
        for c in self.contacts:
            if c.phone_number == phone_number:
                self.contacts.remove(c)
                return
        print("Contact not found")

    def search_by_name(self, name):
        results = []
        for c in self.contacts:
            if name.lower() in c.name.lower():
                results.append(c)
        return results

    def update_contact(self, phone_number, name=None, new_phone=None, online=None, blocked=None):
        for c in self.contacts:
            if c.phone_number == phone_number:
                if name is not None:
                    c.name = name
                if new_phone is not None:
                    if self._phone_exists(new_phone):
                        print("New phone already exists")
                        return
                    c.phone_number = new_phone
                if online is not None:
                    c.online = online
                if blocked is not None:
                    c.blocked = blocked
                return
        print("Contact not found")

    def block_contact(self, phone_number):
        for c in self.contacts:
            if c.phone_number == phone_number:
                c.blocked = True
                return

    def unblock_contact(self, phone_number):
        for c in self.contacts:
            if c.phone_number == phone_number:
                c.blocked = False
                return

    def display_all(self):
        print("=== ALL CONTACTS ===")
        for c in self.contacts:
            print(c)

    def display_online(self):
        print("=== ONLINE CONTACTS ===")
        for c in self.contacts:
            if c.online:
                print(c)

    def _phone_exists(self, phone_number):
        return any(c.phone_number == phone_number for c in self.contacts)

app = ChatApp()

c1 = Contact("1", "Alex", "111", online=True)
c2 = Contact("2", "Maria", "222", online=False)
c3 = Contact("3", "John", "333", online=True)

app.add_contact(c1)
app.add_contact(c2)
app.add_contact(c3)

app.display_all()

print("\nSearch result:")
for c in app.search_by_name("al"):
    print(c)

app.block_contact("222")
app.update_contact("333", name="John Updated", online=False)

print("\nOnline contacts:")
app.display_online()









