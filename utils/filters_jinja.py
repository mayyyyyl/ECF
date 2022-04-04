import pendulum


def dateformat(datestr):

    try:
        datetime = pendulum.instance(datestr, 'Europe/Paris')
        date = datetime.date()

    except Exception:
        return 'ce n\'est pas une date'

    return date.format('dddd DD MMMM', locale='fr')
