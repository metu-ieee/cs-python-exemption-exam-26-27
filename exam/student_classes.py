from read_only_base import Society, ActiveMember, BaseProjectTeam  # noqa


class SocietyTeam(BaseProjectTeam):
    """
    Represents a team under a certain METU IEEE Society.
    Inherits the base project team.
    """

    # TODO: You will init the class,
    # create the is_interdisciplinary flag and can_recruit function.


class CSTeam(SocietyTeam):
    """
    Represents a team under Computer Society.
    """

    # TODO: You will init the team as specified in the documentation


class ComSocTeam(SocietyTeam):
    """
    Represents a team under Communications Society.
    """

    # TODO: You will init the team as specified in the documentation


class RASTeam(SocietyTeam):
    """
    Represents a team under Robotics and Automation Society.
    """

    # TODO: You will init the team as specified in the documentation


class PESTeam(SocietyTeam):
    """
    Represents a team under Power and Energy Society.
    """

    # TODO: You will init the team as specified in the documentation


class AESSTeam(SocietyTeam):
    """
    Represents a team under Aerospace and Electronic Systems Society
    """

    # TODO: You will init the team as specified in the documentation
