from databasehandler.handler import DataBaseLogRecord

def test_record_emit_really_puts_report_on_database_by_log_message(logger_for_sqlite_database, session):

    log_message = 'Record emit test.'
    
    logger_for_sqlite_database.error(log_message)

    logged_report = session.query(DataBaseLogRecord).all()[0]

    assert logged_report.message == log_message


def test_record_emit_really_puts_report_on_database_by_log_level(logger_for_sqlite_database, session):

    log_message = 'second_test.'
    
    logger_for_sqlite_database.error(log_message)

    logged_report = session.query(DataBaseLogRecord).filter_by(message=log_message)[0]

    assert logged_report.levelname == 'ERROR'

