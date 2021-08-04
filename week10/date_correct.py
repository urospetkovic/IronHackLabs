
def autocorrect(text):
    import datetime as dt
    from datetime import timedelta
    today = dt.datetime.now()
    text_sp = text.split()
    num = int(text_sp[0])
    t = text_sp[1][0]
    abs_date = 0
    if t.lower() == 'm':       
        if num > today.minute & today.hour < 1:
            abs_date = today.replace(day = today.day-1)
        else:
            abs_date = today
    elif t.lower() == 'h':
        if num > today.hour:
            abs_date = today.replace(day = today.day-1)
    elif t.lower() == 'd':
        abs_date = today - timedelta(days=num)
    elif t.lower() == 'w':
        days = num * 7
        if days > today.day:
            abs_date = today - timedelta(days=days)
        else:
            abs_date = today.replace(day = today.day-days)
    return str(abs_date.strftime('%d/%m/%Y'))

text = '365 day ago'

print(autocorrect(text))

