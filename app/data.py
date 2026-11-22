
from app.models import Case, Suspect, Clue, Investigation


# CASES
cases = [
    Case(
        case_id=101,
        title="The Midnight Murder",
        description="A wealthy businessman was found dead in his office at midnight. Four people had access to the building.",
        location="Baku, Azerbaijan",
        status="active"
    )
]


# SUSPECTS
suspects = [
    Suspect(
        suspect_id=1,
        case_id=101,
        name="Daniel Carter",
        occupation="Business Partner",
        description="The victim's business partner. They recently had a serious disagreement.",
        alibi="Claims he was attending a business meeting."
    ),
    Suspect(
        suspect_id=2,
        case_id=101,
        name="Sarah Mitchell",
        occupation="Personal Assistant",
        description="The victim's assistant who knew his daily schedule.",
        alibi="Claims she left the office at 9 PM."
    ),
    Suspect(
        suspect_id=3,
        case_id=101,
        name="James Wilson",
        occupation="Security Guard",
        description="Responsible for monitoring the building at night.",
        alibi="Claims he was watching the security cameras."
    ),
    Suspect(
        suspect_id=4,
        case_id=101,
        name="Emily Carter",
        occupation="Family Member",
        description="The victim's niece who recently argued with him about inheritance.",
        alibi="Claims she was at home."
    )
]


# CLUES
clues = [
    Clue(
        clue_id=1,
        case_id=101,
        title="Broken Watch",
        description="A broken watch was discovered near the victim's desk. It stopped at 11:30 PM.",
        found_at="Victim's office"
    ),
    Clue(
        clue_id=2,
        case_id=101,
        title="Security Footage",
        description="The security cameras stopped recording for 15 minutes before midnight.",
        found_at="Security room"
    ),
    Clue(
        clue_id=3,
        case_id=101,
        title="Missing Document",
        description="A document concerning the victim's company shares disappeared from his desk.",
        found_at="Victim's office"
    )
]


# SECRET SOLUTION
solutions = {
    101: {
        "culprit_id": 3,
        "motive": "The security guard was secretly involved in stealing company documents.",
        "explanation": "The security guard had access to the surveillance system and could manipulate the recordings."
    }
}


# ASSIGNMENT 2 - MOCK INVESTIGATIONS

investigations = [
    Investigation(
        id="investigation_101",
        title="The Midnight Murder",
        description="Investigate the mysterious death of a businessman.",
        status="active",
        ownerId="user-a"
    ),
    Investigation(
        id="investigation_102",
        title="The Missing Documents",
        description="Investigate the disappearance of confidential company documents.",
        status="active",
        ownerId="user-b"
    )
]
