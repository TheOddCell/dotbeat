# BeatSchedule
A function schedualer that uses .beat time.
- No arithmatic options.
- No comparasions.
- No conversions.
## Init options
- `tasks` (`dict`): Dictionary of tasks to run at specific .beat times. (dict must contain functions.)

## `add_task()`
Adds a task to the schedualer.
Options:
- `beat_time` (`str`): Time that the task should be done.
- `func` (`function`): The function to be run.
## `run()`
Check if there are any tasks to be run, and if so then run the task.
Options:
- `execute_if_passed` (`bool`): If True, execute tasks even if the current beat time has passed.

