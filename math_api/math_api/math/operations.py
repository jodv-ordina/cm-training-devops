def add(t1: int, t2: int) -> int:
    """For two integers t1 and t2, returns t1+t2."""
    return t1 + t2


def sub(t1: int, t2: int) -> int:
    """For two integers t1 and t2, returns t1-t2."""
    return t1 - t2


def div(t1: int, t2: int) -> float:
    """For two integers t1 and t2, returns t1/t2."""
    if t2 == 0:
        raise ValueError("Division by 0")
    return t1 / t2


def mul(t1: int, t2: int) -> int:
    """For two integers t1 and t2, returns t1*t2."""
    return t1 * t2
