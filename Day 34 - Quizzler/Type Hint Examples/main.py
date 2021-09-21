# age: int
# name: str
# height: int
# is_human: bool

# Type Hints

def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(19):
    print("You may pass")
else:
    print("Pay a fine")
