from .row import Row
from .tile import Tile
from .picture import Picture
import re
from typing import Generator, Optional

tile_pattern = re.compile(r"^Tile (?P<num>\d+):$")


def parse(lines: list[str]) -> Picture:
    def get_pictures() -> Generator[Tile, None, None]:
        length: Optional[int] = None
        number: Optional[int] = None
        tile: Optional[list[Row]] = None

        try:
            it = iter(lines)
            while True:
                match = tile_pattern.match(next(it))
                if not match:
                    raise Exception
                number = int(match["num"])
                tile = list[Row]()
                while (line := next(it)) != "":
                    if length is None:
                        length = len(line)
                    elif length != len(line):
                        raise Exception
                    tile.append(Row.from_string(line))
                if len(tile) != length:
                    raise Exception
                yield Tile(number, tile)

                number = None
                tile = None
        except StopIteration:
            if number is not None and tile is not None:
                if len(tile) != length:
                    raise Exception
                yield Tile(number, tile)

    return Picture(get_pictures())
