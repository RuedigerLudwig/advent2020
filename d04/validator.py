from .passport import Passport
from typing import Optional
import re


class PassportValidator:
    @staticmethod
    def is_valid(passport: Passport):
        return (passport.get("byr") is not None
                and passport.get("iyr") is not None
                and passport.get("eyr") is not None
                and passport.get("hgt") is not None
                and passport.get("ecl") is not None
                and passport.get("hcl") is not None
                and passport.get("pid") is not None)

    @staticmethod
    def _check_between(val: Optional[str], min: int, max: int) -> bool:
        try:
            return val is not None and min <= int(val) <= max
        except ValueError:
            return False

    @staticmethod
    def check_byr(byr: Optional[str]) -> bool:
        return PassportValidator._check_between(byr, 1920, 2002)

    @staticmethod
    def check_iyr(iyr: Optional[str]) -> bool:
        return PassportValidator._check_between(iyr, 2010, 2020)

    @staticmethod
    def check_eyr(eyr: Optional[str]) -> bool:
        return PassportValidator._check_between(eyr, 2020, 2030)

    _hgt_re = re.compile(r"^(?P<val>\d+)(?P<unit>cm|in)$")

    @staticmethod
    def check_hgt(hgt: Optional[str]) -> bool:
        if hgt is None:
            return False
        match = PassportValidator._hgt_re.match(hgt)
        if match is None:
            return False
        if match["unit"] == "cm":
            return 150 <= int(match["val"]) <= 193
        else:
            return 59 <= int(match["val"]) <= 76

    @staticmethod
    def _check_match(val: Optional[str], pattern: re.Pattern[str]) -> bool:
        return val is not None and pattern.match(val) is not None

    _hcl_re = re.compile(r"^#[0-9a-f]{6}$")

    @staticmethod
    def check_hcl(hcl: Optional[str]) -> bool:
        return PassportValidator._check_match(hcl, PassportValidator._hcl_re)

    _pid_re = re.compile(r"^\d{9}$")

    @staticmethod
    def check_pid(pid: Optional[str]) -> bool:
        return PassportValidator._check_match(pid, PassportValidator._pid_re)

    @staticmethod
    def check_ecl(ecl: Optional[str]) -> bool:
        return ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

    @staticmethod
    def is_strictly_valid(passport: Passport) -> bool:
        return (PassportValidator.check_byr(passport.get("byr"))
                and PassportValidator.check_iyr(passport.get("iyr"))
                and PassportValidator.check_eyr(passport.get("eyr"))
                and PassportValidator.check_hgt(passport.get("hgt"))
                and PassportValidator.check_ecl(passport.get("ecl"))
                and PassportValidator.check_hcl(passport.get("hcl"))
                and PassportValidator.check_pid(passport.get("pid")))
