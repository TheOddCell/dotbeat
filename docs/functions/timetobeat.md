# timeToBeat
Converts a unix time or gmtime object to an .beat time.
## Arguments
- `unixtime` (`int`): Unix time to convert to .beat time.
- `gmtimeobj` (time.struct_time): gmtime object to convert to .beat time.
- `og` (`bool`): Whether to use the original .beat time format.
- `number` (`bool`): Whether to return the .beat time as a number.
## Returns
`str` or `float`: String or float representation of the time object.