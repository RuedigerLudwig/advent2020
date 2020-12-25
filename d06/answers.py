from typing import Callable, Generator, Iterable, Optional


class AnswerEval:
    @staticmethod
    def _operate(
        all_answers: Iterable[str], op: Callable[[set[str], set[str]],
                                                 set[str]]
    ) -> Generator[set[str], None, None]:

        result: Optional[set[str]] = None
        for answer in all_answers:
            if answer != "":
                if result is not None:
                    result = op(result, set(answer))
                else:
                    result = set(answer)
            else:
                if result is not None:
                    yield result
                    result = None

        if result is not None:
            yield result

    @staticmethod
    def by_anyone(
            all_answers: Iterable[str]) -> Generator[set[str], None, None]:
        return AnswerEval._operate(all_answers, lambda a, b: a | b)

    @staticmethod
    def by_everyone(
            all_answers: Iterable[str]) -> Generator[set[str], None, None]:
        return AnswerEval._operate(all_answers, lambda a, b: a & b)
