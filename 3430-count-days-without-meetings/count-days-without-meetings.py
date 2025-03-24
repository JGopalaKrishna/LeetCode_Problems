class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        kaliDays=0
        presentDay=0
        meetings.sort()
        for l in meetings:
            if(presentDay<l[0]):
                kaliDays+=(l[0]-(presentDay+1))
            if presentDay<l[1]:
                presentDay=l[1]
        return kaliDays+(days-presentDay)