import heapq as hp
class Solution:
    def MeetingRooms(self, meetings):
        empty_room = []
        room_id = 0
        res = []
        for meet_id, (start, end) in enumerate(meetings):
            if room_id > 0 and empty_room[0][0] <= start:
                _, curr_id = hp.heappop(empty_room)
            else:
                curr_id, room_id = room_id, room_id + 1
            
            res.append((meet_id, curr_id))
            hp.heappush(empty_room, (end, curr_id))
        
        return res
            