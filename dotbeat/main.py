from time import gmtime, time

class BeatTime:
    """
    Class to handle .beat time.
    If no time is provided, the current time is used.

    Attributes:
        unixtime (int): Unix time to convert to .beat time.
        gmtimeobj (time.struct_time): gmtime object to convert to .beat time.
        og (bool): Whether to use the original .beat time format.
        auto_update (bool): Whether to automatically update the .beat time if no time is provided.
        beatTime (str): .beat time to convert to Unix time.
    """
    def __init__(self, unixtime=None, gmtimeobj=None, og=False, auto_update=True, beatTime=None):
        """
        Initializes a BeatTime object.
        If no time is provided, the current time is used.

        Args:
            unixtime (int): Unix time to convert to .beat time.
            gmtimeobj (time.struct_time): gmtime object to convert to .beat time.
            og (bool): Whether to use the original .beat time format.
            auto_update (bool): Whether to automatically update the .beat time if no time is provided.
            beatTime (str): .beat time to convert to Unix time.
        """
        self.og = og
        self.auto_update = auto_update

        if unixtime is not None:
            self.unixtime = unixtime
        elif gmtimeobj is not None:
            self.unixtime = time.mktime(gmtimeobj)
        elif beatTime is not None:
            if isinstance(beatTime, str):
                beatTime = beatTime.lstrip('@')
            beatTime = float(beatTime)
            total_seconds = (beatTime * 86.4) % 86400
            self.unixtime = (total_seconds - ((gmtime(0).tm_hour + 1) % 24) * 3600) % 86400
        else:
            self.unixtime = time()

        self.time = gmtime(self.unixtime)
        self.update_time()
    
    def update_time(self, forceprecise=False):
        """
        Manually update the .beat time according to the time object or auto_update.
        Unnecessary as most ways to get the .beat time from this object automaticly update the time.

        Args:
            forceprecise (bool): Whether to force the .beat time to not be the orginal version. (without rounding)
        """
        if self.auto_update:
            self.unixtime = time()
            self.time = gmtime(self.unixtime)
        total_seconds = ((self.time.tm_hour + 1) % 24) * 3600 + (self.time.tm_min * 60) + self.time.tm_sec
        self.beat = (total_seconds / 86.4) % 1000
        self.beat = round(self.beat) if self.og and not forceprecise else round(self.beat, 2)
    
    def __add__(self, other):
        raise NotImplemented # Requests to add this should be sent to /dev/null. (jk, this will be done later, not rn)
    
    def __subtract__(self, other):
        raise NotImplemented # same as __add__
    
    def __eq__(self, other):
        self.update_time(True)
        if isinstance(other, BeatTime):
            return self.unixtime == other.unixtime
        return False

    def __lt__(self, other):
        self.update_time(True)
        if isinstance(other, BeatTime):
            return self.unixtime < other.unixtime
        return False

    def __le__(self, other):
        self.update_time(True)
        if isinstance(other, BeatTime):
            return self.unixtime <= other.unixtime
        return False

    def __gt__(self, other):
        self.update_time(True)
        if isinstance(other, BeatTime):
            return self.unixtime > other.unixtime
        return False

    def __ge__(self, other):
        self.update_time(True)
        if isinstance(other, BeatTime):
            return self.unixtime >= other.unixtime
        return False

    def __ne__(self, other):
        self.update_time(True)
        if isinstance(other, BeatTime):
            return self.unixtime != other.unixtime
        return False
    
    def __str__(self):
        self.update_time()
        return f"@{int(self.beat):03d}" if self.og else f"@{self.beat:06.2f}"

    def __int__(self):
        self.update_time()
        return int(self.beat)
    
    def __float__(self):
        self.update_time(True)
        return float(self.beat)
    
    def __repr__(self):
        return f"BeatTime({self.unixtime}, og={self.og}, auto_update={self.auto_update})"
    
    def __hash__(self):
        return hash(self.unixtime)
    
    def __bool__(self):
        raise Exception("Cannot convert BeatTime to boolean.")

    def __index__(self):
        return self.unixtime
    
    def __len__(self):
        if self.og:
            return 3
        return 6

    def __iter__(self):
        return iter([self.beat, self.time, self.unixtime])
    
