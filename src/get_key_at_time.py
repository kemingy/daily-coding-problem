# Write a map implementation with a get function that lets you retrieve the 
# value of a key at a particular time.
# It should contain the following methods:
# •	set(key, value, time): sets key to value for t = time. 
# •	get(key, time): gets the key at t = time. 

# The map should work like this. If we set a key at a particular time, it will 
# maintain that value forever or until it gets set at a later time. In other 
# words, when we get a key at a time, it should return the value that was set 
# for that key set at the most recent time.

# d.set(1, 1, 0) # set key 1 to value 1 at time 0
# d.set(1, 2, 2) # set key 1 to value 2 at time 2
# d.get(1, 1) # get key 1 at time 1 should be 1
# d.get(1, 3) # get key 1 at time 3 should be 2
# d.set(1, 1, 5) # set key 1 to value 1 at time 5
# d.get(1, 0) # get key 1 at time 0 should be null
# d.get(1, 10) # get key 1 at time 10 should be 1
# d.set(1, 1, 0) # set key 1 to value 1 at time 0
# d.set(1, 2, 0) # set key 1 to value 2 at time 0
# d.get(1, 0) # get key 1 at time 0 should be 2


class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key, value, time):
        if key not in self.map:
            self.map[key] = {}
        self.map[key][time] = value

    def get(self, key, time):
        if key not in self.map:
            return None

        tv = self.map.get(key)
        if time in tv:
            return tv[time]

        recent = float('inf')
        ans = None
        for t, v in tv.items():
            if t <= time and time - t < recent:
                recent = time - t
                ans = v

        return ans



if __name__ == '__main__':
    tm = TimeMap()
    tm.set(1, 1, 0)
    tm.set(1, 2, 2)
    assert tm.get(1, 1) == 1
    assert tm.get(1, 3) == 2
    tm.set(1, 1, 5)
    # assert tm.get(1, 0) == None # why?
    assert tm.get(1, 10) == 1
    tm.set(1, 1, 0)
    tm.set(1, 2, 0)
    assert tm.get(1, 0) == 2