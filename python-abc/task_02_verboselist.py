#!/usr/bin/python3


class VerboseList(list):
    def append(self, element):
        print(f"Added {element} to the list.")
        super().append(element)

    def extend(self, element):
        print(f"Extended the list with {element} items.")
        super().extend(element)

    def remove(self, element):
        print(f"Removed {element} from the list")
        super().remove(element)

    def pop(self, index=None):
        if index is None:
            index = len(self) - 1
        print(f"Popped {self[index]} from the list.")
        super().pop(index)
