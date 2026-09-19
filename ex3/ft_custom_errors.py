#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def raise_errors(operation_number: int) -> None:
    if operation_number == 0:
        raise PlantError("The tomato plant is wilting!")
    if operation_number == 1:
        raise WaterError("Not enough water in the tank!")


def error_handling() -> None:
    print("Testing PlantError...")
    try:
        raise_errors(0)
    except PlantError as error:
        print(f"Caught PlantError: {error}\n")
    print("Testing WaterError...")
    try:
        raise_errors(1)
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")
    print("Testing catching all garden errors...")
    for i in range(2):
        try:
            raise_errors(i)
        except GardenError as error:
            print(f"Caught GardenError: {error}")
#    try:
#        raise GardenError()
#    except GardenError as error:
#        print(f"Caught GardenError: {error}")


if __name__ == "__main__":
    print('=== Custom Garden Errors Demo ===\n')
    error_handling()
    print("\nAll custom error types work correctly!")
