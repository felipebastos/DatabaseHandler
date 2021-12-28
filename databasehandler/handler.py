from logging import Handler, LogRecord, NOTSET
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import Session, declarative_base

from datetime import datetime

Model = declarative_base()

class DataBaseLogRecord(Model):
    """
    There is some attributes we can bring here in future version
    'created', 'exc_info', 'exc_text', 'filename', 'funcName', 'getMessage', 'levelname', 'levelno', 'lineno', 'module', 'msecs', 'msg', 'name', 'pathname', 'process', 'processName', 'relativeCreated', 'stack_info', 'thread', 'threadName'
    """
    __tablename__ = 'databaselogrecord'
    id = Column(Integer, primary_key=True)
    message = Column(String)
    timeStamp = Column(DateTime, default=datetime.now)

    def __init__(self, logrecord: LogRecord):
        self.message = logrecord.getMessage()
        

class DataBaseHandler(Handler):
    """[summary]
    """
    def __init__(self, level=NOTSET, database_uri='sqlite:///logger.db'):
        Handler.__init__(self, level=level)
        
        self.engine = create_engine(database_uri)
        Model.metadata.create_all(self.engine)

    def emit(self, record):
        with Session(self.engine) as session:
            db_record = DataBaseLogRecord(record)

            session.add(db_record)
            session.commit()
