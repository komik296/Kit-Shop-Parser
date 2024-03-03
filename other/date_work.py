import datetime
import calendar

def get_first_and_last_day_of_month(input_date):
    """
    Takes a date and returns the first and last day of that month.

    Parameters:
    - input_date (datetime.date): The input date.

    Returns:
    - tuple: A tuple containing the first and last day of the month as datetime.date objects.
    """
    # Extract year and month from the input date
    year = input_date.year
    month = input_date.month

    # Calculate the first day of the month
    start_date = datetime.date(year, month, 1)

    first_day = start_date.strftime('%d.%m.%Y')

    # Find the last day of the month
    last_day = datetime.date(year, month, calendar.monthrange(year, month)[1]).strftime('%d.%m.%Y')

    date_to_mysql = start_date.strftime('%Y-%m-%d')

    return first_day, last_day, date_to_mysql

