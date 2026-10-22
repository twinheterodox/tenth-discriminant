"""Check the printed finite certificate, independently of its construction.

The input is the exact table text in proof.tex. All arithmetic
is integer arithmetic. This is a certificate checker, not formal verification
of the mathematical or historical argument.
"""

from math import gcd, isqrt
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
SMALL_PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
SURVIVORS = (11, 19, 43, 67, 163)
NINE = (3, 4, 7, 8) + SURVIVORS


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def rows(filename, columns):
    result = []
    stem = Path(filename).stem
    tex = (HERE / "proof.tex").read_text()
    section = tex.split("% BEGIN " + stem + "\n")[1].split("% END " + stem)[0]
    for line in section.splitlines():
        if not line.strip() or line.lstrip().startswith("%"):
            continue
        assert line.endswith(r"\\"), (filename, line)
        fields = [part.strip() for part in line[:-2].split("&")]
        assert len(fields) == columns, (filename, line)
        result.append(fields)
    return result


def witness(q, entry):
    p, a = map(int, entry.split(":"))
    assert prime(p) and 3 <= p <= 31 and 0 <= a <= p // 2
    assert 4 * p < q, (q, entry)
    assert (q + a * a) % p == 0, (q, entry)
    return p, a


def reduced_forms(q):
    result = []
    for a in range(1, isqrt(q // 3) + 1):
        for b in range(-a, a + 1):
            if (b * b + q) % (4 * a):
                continue
            c = (b * b + q) // (4 * a)
            if c < a or gcd(gcd(a, b), c) != 1:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            result.append((a, b, c))
    return result


def main():
    assert all(prime(p) for p in SMALL_PRIMES)
    allowed = {3: {1}, 5: {2, 3}, 7: {1, 2, 4}, 11: {1, 3, 4, 5, 9}}
    for p, residues in allowed.items():
        # Derive the permissible q residues directly from the squares mod p.
        squares = {a * a % p for a in range(p)}
        assert residues == {r for r in range(p) if (-r) % p not in squares}

    table = rows("certificate_table.tex", 5)
    residues = [int(row[0]) for row in table]
    assert len(residues) == len(set(residues)) == 30
    assert 8 * 3 * 5 * 7 * 11 == 9240
    excluded = set()
    for row in table:
        r = int(row[0])
        assert 0 <= r < 9240 and r % 8 == 3
        assert all(r % p in keep for p, keep in allowed.items())
        for t, entry in enumerate(row[1:]):
            q = r + 9240 * t
            if not 163 < q < 32768:
                assert entry == "-", (q, entry)
            else:
                assert entry != "-", (q, entry)
                p, _ = witness(q, entry)
                assert 13 <= p <= 31
                excluded.add(q)
    assert len(excluded) == 104
    assert excluded == {
        q for q in range(171, 32768, 8)
        if all(q % p in keep for p, keep in allowed.items())
    }
    print("PASS: all 30 CRT rows and 104 printed large-range witnesses.")

    small = rows("small_certificate.tex", 2)
    small_q = [int(row[0]) for row in small]
    assert len(small_q) == len(set(small_q)) == 15
    assert set(small_q) == set(range(11, 164, 8)) - set(SURVIVORS)
    for q, entry in small:
        witness(int(q), entry)
    print("PASS: all 15 small-range witnesses; five survivors up to 163.")

    # A separate exhaustive sieve uses Euler's criterion rather than the
    # printed square roots or the CRT reduction.
    candidates = list(range(11, 32768, 8))
    assert len(candidates) == 4095
    direct = [q for q in candidates
              if all(4 * p >= q or pow((-q) % p, (p - 1) // 2, p) == p - 1
                     for p in SMALL_PRIMES)]
    assert direct == list(SURVIVORS)
    print("PASS: independent Euler-criterion sieve of all 4095 candidates.")

    # Parse the triples actually printed in the paper, not a parallel list.
    tex = (HERE / "proof.tex").read_text()
    printed = re.findall(
        r"^(\d+) & (\d+) & \\\(\((\d+),(\d+),(\d+)\)\\\)",
        tex, flags=re.MULTILINE,
    )
    assert [int(row[0]) for row in printed] == list(NINE)
    for q, bound, a, b, c in printed:
        q, bound = int(q), int(bound)
        triple = (int(a), int(b), int(c))
        assert bound == isqrt(q // 3)
        assert reduced_forms(q) == [triple]
        print(f"q={q}: all reduced forms = {[triple]}")
    print("PASS: all nine reduced-form lists; checked tables come directly from proof.tex.")
    print("PASS: complete finite certificate. No independent audit is claimed.")


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run without Python -O or -OO.")
    main()
