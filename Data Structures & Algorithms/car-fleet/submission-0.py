class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = dict(zip(position, speed))

        pos_desc = sorted(position, reverse=True)

        speed_as_pos = []
        for i in pos_desc:
            speed_as_pos.append(pos_speed[i])
        
        time_as_pos = [(target - pos_desc[i]) / speed_as_pos[i] for i in range(len(position))]


        n_fleets = 0
        slowest_time = 0
        for time in time_as_pos:
            if time > slowest_time:
                n_fleets += 1
                slowest_time = time
        
        return n_fleets




        
        
        


        
        