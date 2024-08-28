__version__ = "0.0.1"
import frappe
from frappe.utils.formatters import format_value as original_format_value
from frappe.utils import formatters
from frappe.utils import (
    formatdate
)
import datetime
from nepali_calendar.nepali.datetime import nepalidate

NPFORMATE_VALUES = {
    'mm-dd-yyyy': '%m-%d-%Y',
    'mm.dd.yyyy': '%m.%d.%Y',
    'mm/dd/yyyy': '%m/%d/%Y',
    'dd-mm-yyyy': '%d-%m-%Y',
    'dd.mm.yyyy': '%d.%m.%Y',
    'dd/mm/yyyy': '%d/%m/%Y',
    'yyyy-mm-dd': '%Y-%m-%d',
    'yyyy/mm/dd': '%Y/%m/%d',
    'yyyy.mm.dd': '%Y.%m.%d',
}

def custom_format_value(value, df=None, doc=None, currency=None, translated=False, format=None):
    if df and  df.get("fieldtype") == "Date":
        if isinstance(value, datetime.date):
            value = str(value)
        neplai_date_format = frappe.db.get_single_value("Nepali Date Settings", "nepali_date_format")
        date = datetime.datetime.strptime(value, NPFORMATE_VALUES[neplai_date_format])
        nepali_date = nepalidate.from_date(date)
        fnpdate = nepali_date.strftime_ne(NPFORMATE_VALUES[neplai_date_format])
        return f"{fnpdate} <br/> {formatdate(value)}"
    return original_format_value(value, df, doc, currency, translated, format)


# Monkey patching the original method
formatters.format_value = custom_format_value
