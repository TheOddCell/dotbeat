# BeatTime
Class to handle beattime.
## Init Options
- `unixtime` (`int`): Unix time to convert to .beat time.
- `gmtimeobj` (`time.struct_time`): gmtime object to convert to .beat time.
- `og` (`bool`): Whether to use the original .beat time format.
- `auto_update` (`bool`): Whether to automatically update the .beat time if no time is provided.
- `beatTime` (`str`): .beat time to convert to Unix time.
## Arithmatic
Add or subtract the time!
## If
==, >, <, etc comparasions available
## Conversion
str, int, float, iter conversion available.
## `update_time()`
Manually update the time if you are grabbing the values directly.
Options:
- `forceprecise` (`bool`) Force non-og mode.