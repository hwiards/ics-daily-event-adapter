import os
from flask import Flask, jsonify
import gettext
import datetime
import icalendar

APP_NAME = 'lokalise'
LOCALE_DIR = './locales'

LANG = os.getenv("LANG")
LANG = "en" if not LANG else LANG[:2]

translations = gettext.translation(APP_NAME, LOCALE_DIR, fallback=False, languages=[LANG])
translations.install()

app = Flask(__name__)

def prepare_ics(filename):
    with open(filename, "rb") as cal_file:
        return icalendar.Calendar.from_ical(cal_file.read())

cal = prepare_ics("calendar.ics")

def create_json(Abfall, when, color):
    return jsonify([
        {"text": [148, 11, when, "fonts/asap-sc-sb.ttf", 1, 1, 30]},
        {"text": [148, 40, Abfall, "fonts/asap-sc-sb.ttf", color, 1, 45]}
    ])

@app.route('/events')
def abfall():
    now = datetime.datetime.now()
    check_date = (now.replace(hour=6, minute=30) if now.time() < datetime.time(11)
                  else (now + datetime.timedelta(days=1)).replace(hour=6, minute=30))

    abfaelle = [component for component in cal.walk("VEVENT") if
                component.decoded("dtstart") < check_date < component.decoded("dtend")]

    if abfaelle:
        title = "\n".join([abfall.get("summary") for abfall in abfaelle])
        if abfaelle[0].decoded("dtstart").date() == now.date():
            # TODAY Red
            return create_json(Abfall=title, when=_("TODAY"), color=2)
        else:
            # Tomorrow Black
            return create_json(Abfall=title, when=_("TOMORROW"), color=1)
    else:
        return create_json(Abfall=_("No collection"), when=" ", color=1)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1234)
