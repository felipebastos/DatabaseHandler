import logging
from databasehandler.handler import DataBaseHandler

def test_record_emit():
    logger = logging.getLogger('tests')
    dbh = DataBaseHandler(level=logging.INFO)
    logger.addHandler(dbh)

    
    logger.error('Record emit test.')
