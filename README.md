# Miniprocessor-Simulation

A Python script that compares three multiplication algorithms, modelled after the way classic microprocessors handle multiplication, and benchmarks how fast each one runs.

## Algorithms

| Name | Approach |
|------|----------|
| `multiplication_8085` | Shift-and-add loop that walks the bits of the multiplier until it reaches zero |
| `multiplication_6502` | Shift-and-add over a fixed 32 bits of the multiplier |
| `multiplication_nsc` | Recursive divide-and-conquer (Karatsuba-style) using decimal digit splitting |

## Run it

```bash
python main.py
```

Each algorithm multiplies the same two random numbers (1 to 10,000) 1,000 times, and the script prints the average time per run:

```
8085 Multiplication took 0.000001 seconds on average for 1000 iterations.
6502 Multiplication took 0.000001 seconds on average for 1000 iterations.
NSC Multiplication took 0.000002 seconds on average for 1000 iterations.
```

Timings depend on your machine and the random inputs.

Change `iterations`, `a` and `b` at the bottom of `main.py` to benchmark different inputs. No external packages are needed.

## Note

These are software models for learning and comparison, not cycle-accurate emulators of the real chips.

