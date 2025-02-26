[Return to my main wobsite](https://oddcell.ca)
# dotbeat
Swatch internet time is cool.

## What is a .beat?
One .beat is 1/1000th of a day. It could reasonably be called millidays.

A time formatted in @xxx means number of .beats since midnight in Switzerland.
Some implimentations of .beats use the format @xxx.xx to make .beats more precise.

## How to install
`pip install dotbeat`

that's it really

## Table of Code
You should be safe to just look at the docstrings really.

### Classes
- [`BeatTime`](/classes/beattime): A time object with added .beat features 
- [`BeatTimer`](/classes/beattimer): A timer that operates in .beats. 
- [`BeatSchedule`](/classes/beatschedule): Schedules tasks to run at specific .beats.

### Functions
- [`beatToTime`](/functions/beattotime): Convert a .beat string to a time object.
- [`timeToBeat`](/functions/timetobeat): Convert a time object or unix time to a string with the .beat time in it.
- [`beatFormatString`](/functions/beatformatstring): Take a string and replace placeholders with the current .beat time.
