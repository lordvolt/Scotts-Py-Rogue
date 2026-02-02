import random
import re
from typing import List, Tuple

# Common dice rolling functions
def roll_d4(num_dice=1, modifier=0):
    """Roll num_dice d4 dice and add modifier."""
    rolls = [random.randint(1, 4) for _ in range(num_dice)]
    return sum(rolls) + modifier

def roll_d6(num_dice=1, modifier=0):
    """Roll num_dice d6 dice and add modifier."""
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    return sum(rolls) + modifier

def roll_d8(num_dice=1, modifier=0):
    """Roll num_dice d8 dice and add modifier."""
    rolls = [random.randint(1, 8) for _ in range(num_dice)]
    return sum(rolls) + modifier

def roll_d10(num_dice=1, modifier=0):
    """Roll num_dice d10 dice and add modifier."""
    rolls = [random.randint(1, 10) for _ in range(num_dice)]
    return sum(rolls) + modifier

def roll_d12(num_dice=1, modifier=0):
    """Roll num_dice d12 dice and add modifier."""
    rolls = [random.randint(1, 12) for _ in range(num_dice)]
    return sum(rolls) + modifier

def roll_d20(num_dice=1, modifier=0):
    """Roll num_dice d20 dice and add modifier."""
    rolls = [random.randint(1, 20) for _ in range(num_dice)]
    return sum(rolls) + modifier

def roll_d100(num_dice=1, modifier=0):
    """Roll num_dice d100 dice and add modifier."""
    rolls = [random.randint(1, 100) for _ in range(num_dice)]
    return sum(rolls) + modifier

# General roll function
def roll_dice(num_dice, sides, modifier=0):
    """Roll num_dice dice with given sides and add modifier."""
    if num_dice < 1 or sides < 2:
        raise ValueError("Number of dice must be at least 1 and sides at least 2.")
    rolls = [random.randint(1, sides) for _ in range(num_dice)]
    return sum(rolls) + modifier

def roll_single(term: str) -> int:
    """
    Roll a single dice term like '2d6', 'd20', '1d100', or a flat number like '+3' / '-4'
    Returns the integer result of that term.
    """
    term = term.strip()
    if not term:
        return 0

    # Flat modifier (e.g. +3 or -2)
    if re.match(r'^[+-]?\d+$', term):
        return int(term)

    # Dice term: [num]d[sides]
    match = re.match(r'^(\d*)d(\d+)$', term)
    if not match:
        raise ValueError(f"Invalid dice term: {term}")

    num_str, sides_str = match.groups()
    num_dice = int(num_str) if num_str else 1
    sides = int(sides_str)

    if num_dice < 1 or sides < 2:
        raise ValueError(f"Invalid dice: {num_dice}d{sides}")

    return sum(random.randint(1, sides) for _ in range(num_dice))


def Roll(expression: str) -> int:
    """
    Parse and roll complex dice expressions like:
        "2d6 + 1d10 + 2"
        "3d8-1d4+5"
        "d20"
        "2d6 + d8 - 3"

    Returns the total integer result.
    """
    # Normalize: remove spaces, make sure operators are surrounded by spaces for splitting
    expr = re.sub(r'\s+', '', expression)           # remove all whitespace
    expr = re.sub(r'([+-])', r' \1 ', expr)         # add spaces around + and -
    expr = expr.strip()

    # Split on spaces → should give terms like ['2d6', '+', '1d10', '+', '2']
    tokens = expr.split()

    if not tokens:
        raise ValueError("Empty dice expression")

    total = 0
    sign = 1  # +1 or -1

    # First term is always positive (implicit +)
    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token in ('+', '-'):
            sign = 1 if token == '+' else -1
            i += 1
            continue

        # Should be a dice term or number
        value = roll_single(token)
        total += sign * value

        # After a number/dice, next should be operator or end
        i += 1
        if i < len(tokens) and tokens[i] not in ('+', '-'):
            raise ValueError(f"Expected operator after {token}, got {tokens[i]}")

    return total


# Optional: helper to show individual rolls (for debugging / fun)
def Roll_verbose(expression: str) -> Tuple[int, List[str]]:
    """
    Same as Roll(), but also returns a list of strings showing each rolled term.
    Example output: (17, ['2d6 → 4+5', '+1d10 → +8', '+2 → +2'])
    """
    expr = re.sub(r'\s+', '', expression)
    expr = re.sub(r'([+-])', r' \1 ', expr).strip()
    tokens = expr.split()

    total = 0
    sign = 1
    breakdown = []
    i = 0

    while i < len(tokens):
        token = tokens[i]

        if token in ('+', '-'):
            sign = 1 if token == '+' else -1
            i += 1
            continue

        # Roll the term
        if re.match(r'^[+-]?\d+$', token):
            value = int(token)
            rolled_str = token
        else:
            match = re.match(r'^(\d*)d(\d+)$', token)
            if not match:
                raise ValueError(f"Invalid term: {token}")
            num_str, sides_str = match.groups()
            num_dice = int(num_str) if num_str else 1
            sides = int(sides_str)
            rolls = [random.randint(1, sides) for _ in range(num_dice)]
            value = sum(rolls)
            rolled_str = f"{num_dice}d{sides} → {'+'.join(map(str, rolls))}"

        total += sign * value
        breakdown.append(f"{token if sign > 0 else '-' + token.lstrip('-')} → {rolled_str}")

        i += 1

    return total, breakdown

# Example usage (commented out)
# if __name__ == "__main__":
#     print(Roll("2d6+1"))  # Example: rolls 2d6 +1
#     print(roll_d20())     # Example: rolls 1d20
#     print(Roll("2d6+1d10+2"))