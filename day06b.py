class SpaceObject:
    def __init__(self, name):
        self.name = name
        self.orbits = None
        self.orbited_by = []


space_objects = {'COM': SpaceObject('COM')}


def main():
    with open('day06_input.txt') as file:
        for line in file:
            process_orbit(line.strip())

    # Start from the object YOU is orbiting
    curr = space_objects['YOU'].orbits
    steps = 0

    while curr.name != 'SAN':
        if contains_san(curr):
            for child in curr.orbited_by:
                if contains_san(child):
                    curr = child
                    steps += 1
                    break
        else:
            curr = curr.orbits
            steps += 1

    print(steps - 1)


def contains_san(space_object):
    # Fully traverse space_object and orbiting objects searching for SAN
    traversal_list = [space_object]
    while traversal_list:
        obj = traversal_list.pop()

        if obj.name == 'SAN':
            return True
        else:
            traversal_list += obj.orbited_by
    else:
        return False


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
