#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    test_inputs = ['25', 'abc']
    for temp_str in test_inputs:
        print(f"Input data is '{temp_str}'")
        try:
            print(f"Temperature is now {input_temperature(temp_str)}°C\n")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}\n")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
