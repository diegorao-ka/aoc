def _cp_wo_idx(l: list, i: int) -> list:
    n = l[:i]
    if i+1 < len(l):
        n.extend(l[i+1:])
    return n

def _is_safe(report: list[int], dampen: bool=True) -> bool:
    # Check every item's successor is acceptable in sign and magnitude.
    sign = report[1] - report[0]
    for i in range(len(report) - 1):
        diff = report[i+1] - report[i]
        if (
            # Conditions for a safe level change
            abs(diff) >= 1 and
            abs(diff) <= 3 and
            ((diff < 0) == (sign < 0))
        ):
            continue
        else:
            # If we're allowed to dampen a problematic level, check safety
            # with different deltas around current level (removing current or
            # either neighbor), not allowing further dampening.
            if dampen:
                return _is_safe(_cp_wo_idx(report, i), dampen=False) \
                    or _is_safe(_cp_wo_idx(report, i+1), dampen=False) \
                    or _is_safe(_cp_wo_idx(report, i-1), dampen=False)
            # Otherwise return False immediately.
            else:
                return False
    return True


def main():
    with open("02/input.txt") as f:
        reports = f.readlines()
    safe = 0
    for r in reports:
        if _is_safe([int(v) for v in r.split()], dampen=True):
            safe += 1
    
    print(safe)

if __name__ == '__main__':
    main()
