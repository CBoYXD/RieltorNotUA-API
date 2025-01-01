from abc import abstractmethod
from typing import Protocol


class Commiter(Protocol):
    """
    Committer is an UOW-compatible interface for committing changes to the data source.
    The actual implementation of UOW can be bundled with an ORM,
    like SQLAlchemy's session.

    Кароче  сесія яку потрібно буде реалізувати так як тут використовуємо протокол. А нижче
    можна побачити нашими чудовими оченятами метод, який має бути реалізовано в майбутніх комітерах.
    Ще головний прикол в тому, що нам навіть не треба робити наслідування а просто реалізувати той метод
    і все життя кафове

    Тому по факту у нас унікальний функціонал, який дає змогу потім у сетапі просто використовувати
    потрібну нам біблутипу для реаліційних бд у нас буде sqlalalchemy а для нереаліційних хз че але
    кароче суть ясна.

    Приклад:

    class SqlaCommitter(Committer):
        def __init__(self, session: AsyncSession):
            self._session = session

        async def commit(self) -> None:
            try:
                await self._session.commit()
                log.debug("Commit was done by session with info: '%s'.", self._session.info)

            except OSError as error:
                raise DataMapperError("Connection failed, commit failed.") from error
            except SQLAlchemyError as error:
                raise DataMapperError("Database query failed, commit failed.") from error

    І далі можно наприклад використовуати цей класс у метода або функціях, де очікується класс у
    якого повинен бути метод комміт бо буде THE END так як ми наклдаємо abstractmethod. А по
    дефолту люди просто пишуть функції або атрибути класса які повинні бути реалізовані але помилок
    не буде, тільки якщо ви не передасте реально щось де потрібно буде використати commit а його то нема
    і буде все одно THE END :(

    Всім гарного дня )

    """
    @abstractmethod
    async def commit(self) -> None:
        """
        :raise  DataMapperError:
        """
