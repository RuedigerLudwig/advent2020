import time
from typing import Any, Callable, ClassVar, Optional
from dataclasses import dataclass, field
from contextlib import ContextDecorator


class TimerError(Exception):
    """Exception for the Timer class """


@dataclass
class Timer(ContextDecorator):
    timers: ClassVar[dict[str, float]] = {}
    name: Optional[str] = None
    message: str = "Elapsed Time: {:0.4f}"
    logger: Callable[[str], None] = print
    _timer: Optional[float] = field(default=None, init=False, repr=False)

    def __post_init__(self):
        if self.name:
            self.timers.setdefault(self.name, 0)

    def start(self) -> None:
        if self._timer is not None:
            raise TimerError("Already started")
        self._timer = time.perf_counter()

    def stop(self) -> float:
        if self._timer is None:
            raise TimerError("Timer not started")

        elapsed = time.perf_counter() - self._timer
        self._timer = None

        if self.logger:
            print(self.message.format(elapsed))
        if self.name:
            self.timers[self.name] += elapsed

        return elapsed

    def __enter__(self) -> "Timer":
        self.start()
        return self

    def __exit__(self, *exc_info: Any) -> None:
        self.stop()
