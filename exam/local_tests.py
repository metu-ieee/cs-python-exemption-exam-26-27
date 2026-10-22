from read_only_base import Society, ActiveMember, BaseProjectTeam, EventProposal
from student_classes import SocietyTeam, CSTeam, ComSocTeam, RASTeam, PESTeam, AESSTeam
from student_functions import (
    draft_active_members,
    audit_branch_synergy,
    parse_event_proposals,
    build_weekly_calendar,
)


def test_q1_classes() -> None:
    # Creating the teams
    cs = CSTeam("Çip Tasarım Takımı")
    comsoc = ComSocTeam("TulWar")
    ras = RASTeam("Rover Takımı")
    pes = PESTeam("METU Ch-ARGE")
    aess = AESSTeam("Meturoid")

    # Inheritance check, already given as correct but we still need to check
    assert all(
        isinstance(society, SocietyTeam) and isinstance(society, BaseProjectTeam)
        for society in [cs, comsoc, ras, pes, aess]
    ), (
        "The Team classes are not inheriting SocietyTeam"
        " or BaseProjectTeam, please check your inheritances"
    )

    # Checking the Enums
    assert (
        cs.owner_society == Society.CS
        and comsoc.owner_society == Society.COMSOC
        and ras.owner_society == Society.RAS
        and pes.owner_society == Society.PES
        and aess.owner_society == Society.AESS
    ), "The Team ownerships are set wrong, please check your codes"

    # Checking the capacities
    assert (
        cs.max_capacity == 6
        and comsoc.max_capacity == 8
        and ras.max_capacity == 10
        and pes.max_capacity == 5
        and aess.max_capacity == 15
    ), "The Team capacities are set wrong, please check your codes"

    # Checking if the skills are defaulted or not
    cs_ = CSTeam(
        team_name="Open Source Ekibi",
        required_skills={"Python", "Git", "C++", "Docker"},
    )

    assert (
        cs.required_skills != cs_.required_skills
    ), "The Team skills are not set as default variable, please check your codes"

    # Creating test members
    m_valid = ActiveMember("e250001", "Nisa", Society.CS, {"Python", "AI"})
    m_low_skill = ActiveMember("e250002", "Damla", Society.CS, {"Python"})
    m_outsider = ActiveMember("e250003", "Erenalp", Society.AESS, {"Python", "Git"})

    # Can recruit checks
    assert cs.can_recruit(
        m_valid
    ), "Recruitment logic is incorrect, please check your codes"
    assert not cs.can_recruit(
        m_low_skill
    ), "Recruitment logic is incorrect, please check your codes"

    # Interdisciplinary checks
    cs.roster.append(m_valid)
    assert (
        not cs.is_interdisciplinary
    ), "Interdisciplinary logic is incorrect, please check your codes"

    cs.roster.append(m_outsider)
    assert (
        cs.is_interdisciplinary
    ), "Interdisciplinary logic is incorrect, please check your codes"


def test_q2_draft() -> None:
    # Creating the instances
    comsoc = ComSocTeam("TulWar vol.2")

    m1 = ActiveMember(
        "e260001", "Mert", Society.COMSOC, {"MATLAB", "Signal Processing"}
    )  # 2 Matching with ComSoc

    m2 = ActiveMember(
        "e260002", "İzzet", Society.AESS, {"MATLAB", "SDR", "Signal Processing"}
    )  # 3 Matching with ComSoc

    m3 = ActiveMember(
        "e260003", "Ayşenur", Society.RAS, {"ROS", "Arduino"}
    )  # No Matching with ComSoc

    # Getting the result from the function
    result = draft_active_members([m2, m1, m3], [comsoc])

    # Checking the return type
    assert isinstance(
        result, dict
    ), f"The result should be a dict, but you return {type(result).__name__}"

    # Checking the dict structure
    assert (
        comsoc.team_name in result.keys()
    ), "The Team name logic is wrong, please check your codes"

    # Checking the prioritization system
    assert result[comsoc.team_name] == [
        "e260002",
        "e260001",
    ], "Your prioritization and recruitment system is wrong, please check you codes"

    # Checking team count mutations
    assert (
        m1.team_count == 1 and m2.team_count == 1 and m3.team_count == 0
    ), "Your member update system is wrong, please check your codes"


def test_q3_synergy() -> None:
    # Creating the instances
    pes = PESTeam("Nükleer Takımı")

    m1 = ActiveMember("e270001", "Mine", Society.PES, {"Power Systems", "BMS"})

    m2 = ActiveMember("e270002", "Utku", Society.RAS, {"BMS", "Simulink"})

    # Adding them to the roster
    pes.roster.append(m1)
    pes.roster.append(m2)

    # Getting the audit from the function
    audit = audit_branch_synergy([pes])

    # Checking the return type
    assert isinstance(
        audit, dict
    ), f"The result should be a dict, but you return {type(audit).__name__}"

    # Checking the format of the dict
    expected = {"Total Budget", "Huge Mixed Teams", "Society Members Count"}
    audit_set = set(audit.keys())

    assert (
        expected == audit_set
    ), "Keys are set wrong in the dict, please check what you return"

    # Checking the math of the budget
    assert (
        audit["Total Budget"] == 2187.5
    ), "Budget calculation is wrong, please check your codes"

    # Checking the logic for huge teams
    assert (
        audit["Huge Mixed Teams"] == []
    ), "Huge Mixed Team calculation is wrong, please check your codes"

    # Checking the member counting logic
    assert audit["Society Members Count"] == {
        "CS": 0,
        "ComSoc": 0,
        "RAS": 1,
        "PES": 1,
        "AESS": 0,
    }, "Member counting system is wrong, please check your codes"


def test_q4_parser() -> None:
    # Creating the raw lines
    raw_lines = [
        "EVT-101 | CS, AESS | WED | 17:30-19:00 | QT Yer İstasyonu Workshop",
        "EVT-102 | ComSoc | MON | 18:00-19:00 | MATLAB Eğitim - 2",
    ]

    # Getting the events from the function
    events = parse_event_proposals(raw_lines)

    # Checking the format of the events
    assert isinstance(
        events, list
    ), f"The result should be a list, but you return {type(events).__name__}"

    # Checking the format of an event
    assert isinstance(events[0], EventProposal), (
        "The result should be an EventProposal,"
        f" but you return {type(events[0]).__name__}"
    )

    # Checking the length of the events
    assert (
        len(events) == 2
    ), "All lines haven't been parsed properly, please check your codes"

    # Checking the EventProposal parsing
    assert (
        events[0].event_id == "EVT-101"
        and events[0].day == "WED"
        and events[0].title == "QT Yer İstasyonu Workshop"
    ), "ID, day or title parsing is wrong, please check your codes"

    # Checking the min calculations
    assert (
        events[0].start_min == 1050 and events[0].end_min == 1140
    ), "Start and end min calculations are wrong, please check your codes"

    # Checking the society parsing
    assert events[0].hosting_societies == {
        Society.CS,
        Society.AESS,
    }, "Hosting Society parsing is wrong, please check your codes"

    # Checking if the code yields errors
    try:
        long_event = parse_event_proposals(  # noqa
            ["EVT-999 | CS | MON | 17:00-19:00 | Too Long Workshop"]
        )
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for >90 min event")


def test_q5_calendar() -> None:
    # Creating the event proposals for thursday
    p1 = EventProposal("EVT-11", "Tea-Talk", "THU", 1080, 1140, {Society.CS})
    p2 = EventProposal(
        "EVT-12", "KiCAD Workshop", "THU", 1050, 1110, {Society.RAS, Society.AESS}
    )
    p3 = EventProposal("EVT-13", "A-Research", "THU", 1110, 1170, {Society.PES})

    # Getting the calendar from the function
    calendar = build_weekly_calendar([p1, p2, p3])

    # Checking the return type
    assert isinstance(
        calendar, dict
    ), f"The result should be a dict, but you return {type(calendar).__name__}"

    {"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"}

    # Checking the format of the dict
    expected = {"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"}
    calendar_set = set(calendar.keys())

    assert (
        expected == calendar_set
    ), "Keys are set wrong in the dict, please check what you return"

    # Checking the calendar logic
    assert (
        calendar["THU"] == ["EVT-02", "EVT-03"] and calendar["MON"] == []
    ), "Event scheduling logic is wrong, please check your codes"


if __name__ == "__main__":
    passed_count = 0

    # Q1 test
    try:
        print("Testing the classes...")
        test_q1_classes()
    except Exception as e:
        print(f"FAIL: Q1 -> {type(e).__name__}: {e}")
    else:
        print("PASS: Q1 has passed successfully!")
        passed_count += 1

    # Q2 test
    try:
        print("Testing the drafting system...")
        test_q2_draft()
    except Exception as e:
        print(f"FAIL: Q2 -> {type(e).__name__}: {e}")
    else:
        print("PASS: Q2 has passed successfully!")
        passed_count += 1

    # Q3 test
    try:
        print("Testing the synergy calculations...")
        test_q3_synergy()
    except Exception as e:
        print(f"FAIL: Q3 -> {type(e).__name__}: {e}")
    else:
        print("PASS: Q3 has passed successfully!")
        passed_count += 1

    # Q4 test
    try:
        print("Testing the event parsing...")
        test_q4_parser()
    except Exception as e:
        print(f"FAIL: Q4 -> {type(e).__name__}: {e}")
    else:
        print("PASS: Q4 has passed successfully!")
        passed_count += 1

    # Q5 test
    try:
        print("Testing the scheduling system...")
        test_q5_calendar()
    except Exception as e:
        print(f"FAIL: Q5 -> {type(e).__name__}: {e}")
    else:
        print("PASS: Q5 has passed successfully!")
        passed_count += 1

    # summary
    print(f"Result: {passed_count}/5 Baseline Checks Passed")
