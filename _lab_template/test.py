# test.py — Mission XX: Lab Title
# -------------------------------------------------------
# Run: python test.py
# -------------------------------------------------------

from starter import your_function_name


def check(condition: bool, label: str):
    if condition:
        print(f"  ✅ {label}")
    else:
        print(f"  ❌ {label}")


def run_tests():
    print("\n🧪 Running tests for Mission XX: Lab Title\n")
    passed = 0
    total = 0

    # --- Test 1: Returns the correct type ---
    total += 1
    result = your_function_name("example_input_1", "example_input_2")
    ok = isinstance(result, str)  # Change type to match your function's return type
    check(ok, "Test 1: Function returns the expected type")
    if ok:
        passed += 1

    # --- Test 2: Basic happy path ---
    total += 1
    result = your_function_name("input_a", "input_b")
    ok = result == "expected_output"  # Replace with actual expected output
    check(ok, "Test 2: Returns correct output for basic input")
    if ok:
        passed += 1

    # --- Test 3: Edge case ---
    total += 1
    result = your_function_name("", "")
    ok = result is not None  # Replace with appropriate edge case check
    check(ok, "Test 3: Handles edge case gracefully")
    if ok:
        passed += 1

    # Add more tests as needed...

    print(f"\n{'🎉 All tests passed!' if passed == total else f'Result: {passed}/{total} tests passed.'}\n")


if __name__ == "__main__":
    run_tests()
