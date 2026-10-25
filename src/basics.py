"""Lab 1 - Python fundamentals for biological calculations."""

#T3
def gc_percent(a: int, c: int, g: int, t: int) -> float:
    """Return the GC percentage from the four base counts.

    Raises:
        ValueError: if any count is negative or the total is zero.
    """
    #Check for negative counts
    if a<0 or c<0 or g<0 or t<0:
        raise ValueError("Base counts cannot be negative.")
    
    total = a+c+g+t

    #Prevent division by zero
    if total == 0:
        raise ValueError("Total base count cannot be zero.")

    #Calculate GC percentage using true division (/)
    return ((g+c)/total)*100.0

def format_report(sample: str, length: int, gc: float) -> str:
    """Return a one-line report with units, e.g. 'S1: 60 bases, GC 46.7%'."""
    return f"{sample}: {length} bases, GC {gc:.1f}%"


def parse_counts(text: str) -> tuple[int, int, int, int]:
    """Parse 'A C G T' counts separated by spaces or commas.

    Raises:
        ValueError: if there are not exactly four non-negative integers.
    """
    #Replace commas with spaces so split() handles both separators
    clean_text = text.replace(",", " ")
    parts = clean_text.split()

    #Must have exaclty 4 items
    if len(parts) != 4:
        raise ValueError("Input must contain exaclty four values.")

    #Convert each string piece into an integer
    try:
        counts = [int(p) for p in parts]
    except ValueError:
        raise ValueError("All base counts must be valid whole numbers.")

    #Check for negative numbers
    for count in counts:
        if count<0:
            raise ValueError("Base counts cannot be negative.")

    return (counts[0], counts[1], counts[2], counts[3])
