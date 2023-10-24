# ics-daily-event-adapter

A tiny python program that takes a local .ics file, like a trash collection calendar, and presents the "events" for today or tomorrow via JSON.
It's purpose is to work with [OpenEPaperLink](https://github.com/jjwbruijn/OpenEPaperLink). 

Change the docker-compose.yml to reflect your locale (right now __en__ and __de__ are implemented), point it to your .ics file and to change the port if necessary. 

Within EPaperLink choose `Json Template` and point it to `http://docker-host:5000/events`

## Licence
MIT