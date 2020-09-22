"""
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.

Example 1:
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Example 3:
Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true

Example 4:
Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true

"""


class Solution(object):

    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        if not trips:
            return True

        N = len(trips)

        # sort trips by start time
        trips_start = [[t[0], t[1]] for t in trips]
        # sort trips by end time
        trips_end = [[t[0], t[2]] for t in trips]

        trips = None

        # Sort trips by start end end time
        trips_start.sort(key=lambda x: x[1])
        trips_end.sort(key=lambda x: x[1])

        # Loop on the trips and update current occupied capacity
        current_capacity, start_index, end_index = 0, 0, 0
        while start_index < N and end_index < N:
            if trips_start[start_index][1] < trips_end[end_index][1]:
                current_capacity += trips_start[start_index][0]
                start_index += 1
            else:
                current_capacity -= trips_end[end_index][0]
                end_index += 1
            if current_capacity > capacity:
                return False
        return True

s = Solution()
print(s.carPooling([[2,1,5],[3,3,7]], 4), False)
print(s.carPooling([[2,1,5],[3,3,7]], 5), True)
print(s.carPooling([[2,1,5],[3,5,7]], 3), True)
print(s.carPooling([[3,2,7],[3,7,9],[8,3,9]], 11), True)
print(s.carPooling([[3,2,7],[12,7,9],[8,3,9]], 11), False)
print(s.carPooling([[12,7,9]], 11), False)
print(s.carPooling([], 11), True)