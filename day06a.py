class SpaceObject:
    def __init__(self, name):
        self.name = name
        self.orbits = None
        self.orbited_by = []
        self.depth = 0


space_objects = {'COM': SpaceObject('COM')}


def main():
    with open('day06_input.txt') as file:
        for line in file:
            process_orbit(line.strip())

    # traverse starting from the COM object
    orbit_count = 0
    traversal_list = [space_objects['COM']]
    while traversal_list:
        obj = traversal_list.pop()

        curr_depth = obj.depth
        orbit_count += curr_depth

        for so in obj.orbited_by:
            so.depth = curr_depth + 1

        traversal_list += obj.orbited_by

    print(orbit_count)


def process_orbit(orbit):
    orbited_name = orbit[:3]
    orbiting_name = orbit[4:]

    # Lookup or add from dictionary
    orbited = space_objects.setdefault(orbited_name, SpaceObject(orbited_name))
    orbiting = space_objects.setdefault(orbiting_name, SpaceObject(orbiting_name))

    # Update the relationships
    orbited.orbited_by.append(orbiting)
    orbiting.orbits = orbited


if __name__ == '__main__':
    main()
