from datetime import datetime
import locale


def setDateTime(dateText, dateSourceFormat="%d %b %Y %H:%M"):
    locale.setlocale(locale.LC_ALL, 'id_ID')
    try:
        retData = datetime.strptime(
            dateText, dateSourceFormat)

    except:
        retData = datetime.now()
    finally:
        return retData.strftime("%d-%m-%Y %H:%M:00")
