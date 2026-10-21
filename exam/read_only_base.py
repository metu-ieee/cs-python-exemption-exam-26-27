from enum import Enum


class Society(Enum):
    """
    Enumaration class for the technical societies under
    the METU IEEE Student Branch
    """

    CS = "CS"
    COMSOC = "ComSoc"
    RAS = "RAS"
    PES = "PES"
    AESS = "AESS"


class ActiveMember:
    """
    Represents the METU IEEE Active Members.
    An active member under a technical society either passes an exemption exam,
    or completes an education programme provided.
    """

    def __init__(
        self, student_id: str, name: str, home_society: Society, skills: set[str]
    ):
        # I didn't use a UUID class here to make things much more deterministic
        self.student_id: str = student_id
        # Name of the student
        self.name: str = name
        # The technical society that the active member originally belongs to
        self._home_society: None | Society = None
        self.home_society: Society = home_society
        # The skillset of the member.
        # You can pass a list object, the set() function prevents any problems.
        self.skills: set[str] = set(skills)
        # The team count of the student
        # Starts as 0
        self._team_count: int = 0

    # Home society getter. You don't call it like a function though.
    # e.g. when you write print(instance.home_society), the getter is called.
    @property
    def home_society(self) -> Society:
        return self._home_society

    # Home society setter. You also don't call this one as a function too!
    # e.g. when you set instance.home_society = Society.CS, the setter is called.
    @home_society.setter
    def home_society(self, value):
        if not isinstance(value, Society):
            raise ValueError(
                f"Invalid society, must be one of {[e.value for e in Society]}"
            )
        self._home_society = value

    # The team count getter.
    # The mechanism is the same as above.
    @property
    def team_count(self) -> int:
        return self._team_count

    # The team count setter.
    # The mechanism is the same as above.
    @team_count.setter
    def team_count(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(
                f"The value can't be less than zero or non-int. You provided {value}"
            )
        self._team_count = value

    # This is what gets printed when you try to print the instance directly
    def __str__(self) -> str:
        return f"{self.name} ({self.student_id}) - {self.home_society.value}"


class BaseProjectTeam:
    """
    Standard base team class.
    Represents the project teams under societies.
    Will be inherited for each societies' team classes.
    """

    def __init__(
        self,
        team_name: str,
        owner_society: Society,
        max_capacity: int,
        required_skills: set[str],
    ):
        # The team's own name
        self.team_name: str = team_name
        # The team's bound society
        self._owner_society: None | Society = None
        self.owner_society: Society = owner_society
        # Allowed max capacity for the team
        self._max_capacity: None | int = None
        self.max_capacity: int = max_capacity
        # Required skillset for the team
        # You can pass a list object, the set() function prevents any problems.
        self.required_skills: set[str] = set(required_skills)
        # The list of the whole team
        self.roster: list[ActiveMember] = []

    # Owner society getter
    @property
    def owner_society(self) -> Society:
        return self._owner_society

    # Owner society setter
    @owner_society.setter
    def owner_society(self, value):
        if not isinstance(value, Society):
            raise ValueError(
                f"Invalid society, must be one of {[e.value for e in Society]}"
            )
        self._owner_society = value

    # The max capacity getter.
    @property
    def max_capacity(self) -> int:
        return self._max_capacity

    # The max capacity setter.
    @max_capacity.setter
    def max_capacity(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(
                f"The value can't be less than zero or non-int. You provided {value}"
            )
        self._max_capacity = value

    def __str__(self) -> str:
        return (
            f"{self.team_name} [{self.owner_society.value}] "
            f"({len(self.roster)}/{self.max_capacity})"
        )


class EventProposal:
    """
    Represents an activity held by a society.
    Will be placed inside a shared calendar.
    """

    def __init__(
        self,
        event_id: str,
        title: str,
        day: str,
        start_min: int,
        end_min: int,
        hosting_societies: set[Society],
    ):
        # I didn't use a UUID class here to make things much more deterministic
        self.event_id: str = event_id
        # Every even has a title
        self.title: str = title
        # 3-caharacter abbreviated uppercase days
        # e.g. MON, TUE, WED, THU, FRI, SAT, SUN
        self.day: str = day
        # Mins from midnight formatted start and end mins
        # e.g. 1080 -> 18.00, 1110 -> 18.30 etc.
        # This is a similar approach to unix timestamp (check it out)
        self.start_min: int = start_min
        self.end_min: int = end_min
        # Hosting societies of that event
        # Being a set implies that there may be collab's
        self.hosting_societies: set[Society] = set(hosting_societies)

    # Duration getter based on start and end
    # There is no setter needed for the duration
    @property
    def duration(self) -> int:
        return self.end_min - self.start_min

    def __str__(self) -> str:
        return (
            f"{self.event_id}: {self.title} "
            f"({self.day} {self.start_min}-{self.end_min})"
        )
