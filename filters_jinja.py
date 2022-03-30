import pendulum


def dateformat(datestr):

    try:
        datetime = pendulum.instance(datestr, 'Europe/Paris')
        date = datetime.date()

    except Exception:
        return 'ce n\'est pas une date'

    tomorrow = pendulum.tomorrow().date()
    today = pendulum.today().date()
    yesterday = pendulum.yesterday().date()
    dayBeforeYesterday = pendulum.now().subtract(days=2).date()

    if date == today:
        return "Aujourd'hui"

    elif date == yesterday:
        return "Hier"

    elif date == dayBeforeYesterday:
        return "Avant-Hier"

    elif date == tomorrow:
        return "Demain"

    else:
        return date.format('dddd DD MMMM', locale='fr')
