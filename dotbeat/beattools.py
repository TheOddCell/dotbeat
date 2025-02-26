import time
from .beattime import BeatTime

class BeatTimer:
    """
    A stopwatch using .beat time.

    Features:
    - Start, stop, and reset the timer.
    - Track elapsed .beats since start.
    - Supports pausing and resuming.
    """

    def __init__(self):
        self.start_time = None
        self.elapsed = 0
        self.running = False

    def start(self):
        """Start or resume the timer."""
        if not self.running:
            self.start_time = time.time() - self.elapsed
            self.running = True

    def stop(self):
        """Pause the timer."""
        if self.running:
            self.elapsed = time.time() - self.start_time
            self.running = False

    def reset(self):
        """Reset the timer."""
        self.start_time = None
        self.elapsed = 0
        self.running = False

    def get_beats(self):
        """Get elapsed time in .beats.
        Returns:
            float: Elapsed time in .beats."""
        if self.running:
            self.elapsed = time.time() - self.start_time
        return round((self.elapsed / 86.4) % 1000, 2)
    
    def get_beattime(self):
        """Get elapsed time as a BeatTime object.
        Returns:
            BeatTime: Elapsed time as a BeatTime object."""
        return BeatTime(beatTime=self.get_beats())

    def __str__(self):
        return f"@{self.get_beats():06.2f}"
    
class BeatSchedule:
    """
    A simple scheduler using .beat time.

    Features:
    - Schedule functions to run at specific .beat times.
    - Automatically checks the current .beat time.
    """

    def __init__(self, tasks={}):
        """Initialize the scheduler with a dictionary of tasks.
        Args:
            tasks (dict): Dictionary of tasks to run at specific .beat times."""
        self.tasks = tasks

    def add_task(self, beat_time, func):
        """Schedule a function to run at a specific .beat time.
        Args:
            beat_time (str): .beat time to run the function.
            func (function): Function to run at the specified .beat time."""
        self.tasks[round(beat_time, 2)] = func

    def run(self, execute_if_passed=True):
        """Check if any task should run based on the current .beat time.
        
        Args:
            execute_if_passed (bool): If True, execute tasks even if the current beat time has passed.
        """
        current_beat = BeatTime().beat
        tolerance = 0.01  # Define a small tolerance range
        if execute_if_passed:
            tasks_to_run = [beat for beat in self.tasks if current_beat >= beat]
        else:
            tasks_to_run = [beat for beat in self.tasks if abs(current_beat - beat) <= tolerance]
        for beat in tasks_to_run:
            if callable(self.tasks[beat]):
                self.tasks[beat]()
            del self.tasks[beat]  # Remove executed task

def timeToBeat(unixtime=None, gmtimeobj=None, og=False, number=False):
    """
    Convert a time to Swatch Internet Time. If no format is provided, the current time is used.

    Args:
        unixtime (int): Unix time to convert to .beat time.
        gmtimeobj (time.struct_time): gmtime object to convert to .beat time.
        og (bool): Whether to use the original .beat time format.
        number (bool): Whether to return the .beat time as a number.

    Returns:
        str: String representation of the time object.
    """
    if number:
        return float(BeatTime(unixtime, gmtimeobj, og))
    return str(BeatTime(unixtime, gmtimeobj, og))

def beatToTime(beatTime="@123.56", og=False):
    """
    Convert a Swatch Internet Time to a time object.

    Args:
        beatTime (str): .beat time to convert to Unix time.
        og (bool): Whether to use the original .beat time format.

    Returns:
        time.struct_time: gmtime object of the .beat time.
    """
    return BeatTime(beatTime=beatTime, og=og).time

def beatFormatString(input="@b-pr"):
    """
    Format a string with the current .beat time.
    Replaces @b-og with the original .beat time and @b-pr with the precise .beat time.

    Args:
        input (str): String to format.

    Returns:
        str: Formatted string.
    """
    return input.replace("@b-og", beatTime=str(BeatTime(og=True)))\
        .replace("@b-pr",beatTime=str(BeatTime()))
