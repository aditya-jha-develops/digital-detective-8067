# Mission 5 — Numbers and data

## 1. Task / objective

Convert numbers by hand, verify them in Python, build a decimal integer converter and investigate character encoding.

## 2. Work completed

### Manual conversions and Python checks

| Conversion | Manual working | Python expression | Observed result | Match |
| --- | --- | --- | --- | --- |
| Decimal 13 to binary | 13 = 8 + 4 + 1. The coefficients for 8, 4, 2, 1 are 1, 1, 0, 1, giving `1101₂`. | `bin(13)` | `'0b1101'` | Yes |
| Decimal 25 to binary | 25 = 16 + 8 + 1. The coefficients for 16, 8, 4, 2, 1 are 1, 1, 0, 0, 1, giving `11001₂`. | `bin(25)` | `'0b11001'` | Yes |
| Binary 1010 to decimal | 1×8 + 0×4 + 1×2 + 0×1 = 10. | `int("1010", 2)` | `10` | Yes |
| Binary 1101 to decimal | 1×8 + 1×4 + 0×2 + 1×1 = 13. | `int("1101", 2)` | `13` | Yes |
| Hexadecimal A to decimal | A has digit value 10. In the units position, 10×16⁰ = 10. | `int("A", 16)` | `10` | Yes |
| Hexadecimal 1F to decimal | F has digit value 15, so 1×16 + 15×1 = 31. | `int("1F", 16)` | `31` | Yes |
| Binary 1111 to hexadecimal | 8 + 4 + 2 + 1 = 15. The single hexadecimal digit for 15 is F. | `hex(int("1111", 2))`, also `hex(15)` | `'0xf'` | Yes |

### Converter tests

| Decimal input | Binary output | Hexadecimal output |
| --- | --- | --- |
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 31 | `0b11111` | `0x1f` |
| 0 | `0b0` | `0x0` |
| -8 | `-0b1000` | `-0x8` |

The input `abc` produced the validation message `Please enter a whole number in decimal.`

## 3. Commands / tools used

- `python3 -q -i` started an interactive Python session for the conversion checks.
- `python3 number_converter.py` ran the program from the mission folder.
- `input()` collected a line of text. `int(text, 10)` interpreted it as a base-10 integer. The other `int()` calls parsed strings in base 2 or base 16.
- `bin()` and `hex()` returned strings with `0b` and `0x` prefixes. For negative integers, Python places the minus sign before the prefix.
- `ord()` showed the numeric code points for the ASCII letters. `.encode("utf-8")` produced the bytes for the rupee symbol.

## 4. My understanding

A digit's position determines the power of the base it multiplies. The value 15 can be written `1111` in binary and `F` in hexadecimal. Python's prefixes describe the representation and are useful when reading a result out of context.

The ASCII decimal codes are **65** for uppercase **A** and **97** for lowercase **a**. A character encoding defines the mapping from characters to bytes so another program can read the same text back. The rupee symbol **₹** is outside basic ASCII and is represented by the three bytes `e2 82 b9` in UTF-8.

## 5. Difficulties faced

The manual notation uses uppercase hexadecimal digits, while Python returned lowercase hexadecimal strings.

## 6. How I resolved them

Compared the digit values and base. `F` and `f` both represent 15, and the `0x` prefix identifies the string as hexadecimal.

## 7. Evidence / files

[number_converter.py](number_converter.py) contains the converter. The interactive verification and run results are recorded above.

## 8. Commit details

**Build number converter and practise data representation** is the Mission 5 checkpoint on GitHub's `main` branch.
