from dataclasses import dataclass, field
import itertools
import re
from typing import Tuple


@dataclass
class Vector:
    x: int
    y: int
    z: int

    @staticmethod
    def zero():
        return Vector(0, 0, 0)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __getitem__(self, axis):
        return getattr(self, axis)

    def __setitem__(self, axis, value):
        setattr(self, axis, value)


@dataclass
class Moon:
    position: Vector = field(default_factory=Vector.zero)
    velocity: Vector = field(default_factory=Vector.zero)
    axes: Tuple = ('x', 'y', 'z')

    def apply_gravity(self, other):
        for axis in self.axes:
            if self.position[axis] > other.position[axis]:
                self.velocity[axis] -= 1
                other.velocity[axis] += 1
            elif self.position[axis] < other.position[axis]:
                self.velocity[axis] += 1
                other.velocity[axis] -= 1

    def potential_energy(self):
        return sum(abs(self.position[axis]) for axis in self.axes)

    def kinetic_energy(self):
        return sum(abs(self.velocity[axis]) for axis in self.axes)


moons = []
with open('day12_input.txt') as file:
    for line in file:
        moon = Moon()
        m = re.match(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>', line)
        moon.position = Vector(*[int(n) for n in m.group(1, 2, 3)])
        moons.append(moon)

for step in range(1000):
    # update the velocities by applying gravity
    for moon1, moon2 in itertools.combinations(moons, 2):
        moon1.apply_gravity(moon2)

    # update the positions
    for moon in moons:
        moon.position = moon.position + moon.velocity

# calculate the total energy of the system
total_energy = sum(m.potential_energy() * m.kinetic_energy() for m in moons)
print(total_energy)
