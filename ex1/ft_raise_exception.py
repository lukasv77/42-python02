#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    elif temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    return temp_int


def test_temperature() -> None:
    test_inputs = ['25', 'abc', '100', '-50']
    for temp_str in test_inputs:
        print(f"Input data is '{temp_str}'")
        try:
            print(f"Temperature is now {input_temperature(temp_str)}°C\n")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
