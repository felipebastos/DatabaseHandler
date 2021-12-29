import pytest

import os
import logging
from databasehandler.handler import DataBaseHandler

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


@pytest.fixture
def logger_for_sqlite_database():
    testing_directory = 'pytest_tests'
    os.makedirs(testing_directory)

    logger = logging.getLogger('tests')
    dbh = DataBaseHandler(database_uri=os.path.join(f'sqlite:///{testing_directory}', 'logger.db'), level=logging.INFO)
    logger.addHandler(dbh)

    yield logger

    os.remove(os.path.join(f'{testing_directory}', 'logger.db'))
    os.removedirs(testing_directory)


@pytest.fixture
def session():
    testing_directory = 'pytest_tests'
    engine = create_engine(os.path.join(f'sqlite:///{testing_directory}', 'logger.db'))
    with Session(engine) as session:
        yield session
