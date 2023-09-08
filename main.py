def count_batteries_by_health(present_capacities):
    counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }

    # Rated capacity of a new battery
    rated_capacity = 120

    # Loop through the present capacities of batteries
    for capacity in present_capacities:
        # Calculate the state-of-health (SoH) as a percentage
        soh = (capacity / rated_capacity) * 100

        # Classify the battery based on its SoH and update counts
        if soh > 80:
            counts["healthy"] += 1
        elif 65 <= soh <= 80:
            counts["exchange"] += 1
        else:
            counts["failed"] += 1

    return counts


def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [115, 118, 80, 95, 91, 77]
    counts = count_batteries_by_health(present_capacities)
    assert counts["healthy"] == 2
    assert counts["exchange"] == 3
    assert counts["failed"] == 1
    print("Done counting :)")


if __name__ == '__main__':
    test_bucketing_by_health()
