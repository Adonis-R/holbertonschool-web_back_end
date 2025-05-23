#!/usr/bin/env python3
"""Module for filtering sensitive data from log messages."""

import logging
import re
from typing import List
import mysql.connector
from os import getenv


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """Redacts specified fields in a log message.

    Args:
        fields (list): List of field names to be redacted.
        redaction (str): The string to replace the field values with.
        message (str): The log line to be filtered.
        separator (str): The separator used in the log line.

    Returns:
        str: The filtered log line with the field values redacted.
    """
    pattern = r'({})=([^{}]*)'.format('|'.join(fields), separator)
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class that obfuscates specified
    fields in log messages."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initializes the RedactingFormatter.

        Args:
            fields (List[str]): List of fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats the log record by redacting sensitive fields.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record with redacted fields.
        """
        original_message = super().format(record)
        return filter_datum(
            self.fields,
            self.REDACTION,
            original_message,
            self.SEPARATOR
        )


def get_logger() -> logging.Logger:
    """Creates a logger with the RedactingFormatter.

    Returns:
        logging.Logger: The configured logger.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(handler)
    logger.propagate = False
    return logger


PII_FIELDS = (
    "name",
    "email",
    "phone",
    "ssn",
    "password",
)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connector to the MySQL database."""
    return mysql.connector.connect(
        host=getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=getenv("PERSONAL_DATA_DB_NAME", "personal_data"),
        user=getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=getenv("PERSONAL_DATA_DB_PASSWORD", ""),
    )


def main():
    """main function that takes no arguments and returns nothing."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()
    logger = get_logger()

    for row in rows:
        name, email, phone, ssn, password, ip, last_login, user_agent = row

        log_message = (
            f"name={name}; email={email}; phone={phone}; ssn={ssn}; "
            f"password={password}; ip={ip}; last_login={last_login}; "
            f"user_agent={user_agent};"
        )

        logger.info(log_message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
