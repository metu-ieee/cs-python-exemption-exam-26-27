# Calculates the base grants needed for a team
def calculate_base_grant(member_count: int, unique_skill_count: int) -> float:
    if member_count <= 0:
        return 0.0
    return (member_count * 500.0) + (unique_skill_count * 250.0)


# Calculates if two events overlap in the same day
def is_overlapping(
    event_a_start: int, event_a_finish: int, event_b_start: int, event_b_finish: int
) -> bool:
    return event_a_start < event_b_finish and event_b_start < event_a_finish
