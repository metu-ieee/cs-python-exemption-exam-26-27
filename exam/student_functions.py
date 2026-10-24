from read_only_base import Society, ActiveMember, EventProposal  # noqa
from read_only_helpers import calculate_base_grant, is_overlapping  # noqa
from student_classes import SocietyTeam


def draft_active_members(
    candidates: list[ActiveMember], teams: list[SocietyTeam]
) -> dict[str, list[str]]:

    # TODO: Draft active members given a list of members and teams

    draft_results = {}

    return draft_results


def audit_branch_synergy(teams: list[SocietyTeam]) -> dict:
    # TODO: Calculate grants for each team, and determine the interdisciplinary ones,
    # and eventually count the members for each society

    # Dont forget to fix the return statement
    return {
        "Total Budget": 0,
        "Huge Mixed Teams": [],
        "Society Members Count": {},
    }


def parse_event_proposals(raw_lines: list[str]) -> list[EventProposal]:

    # TODO: Given lines of event proposals, parse and propose them,
    # dont forget to raise errors!

    event_list = []

    return event_list


def build_weekly_calendar(proposals: list[EventProposal]) -> dict[str, list[str]]:

    # TODO: Given the proposals, curate the event calendar
    calendar = {}

    return calendar
