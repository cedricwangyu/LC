class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        def find_distance(worker_loc, bike_loc):
            return abs(worker_loc[0] - bike_loc[0]) + abs(worker_loc[1] - bike_loc[1])
        
        # Calculate the distance between each worker and bike.
        all_triplets = []
        for worker, worker_loc in enumerate(workers):
            for bike, bike_loc in enumerate(bikes):
                distance = find_distance(worker_loc, bike_loc)
                all_triplets.append((distance, worker, bike))
        
        # Sort the triplets. By default, sorting will prioritize the
        # tuple's first value, then second value, and finally the third value
        all_triplets.sort()
        
        # Initialize all values to False, to signify no bikes have been taken
        bike_status = [False] * len(bikes)
        # Initialize all values to -1, to signify no worker has a bike
        worker_status = [-1] * len(workers)
        # Keep track of how many worker-bike pairs have been made
        pair_count = 0
        
        for distance, worker, bike in all_triplets:
            # If both worker and bike are free, assign the bike to
            # the worker and mark the bike as taken
            if worker_status[worker] == -1 and not bike_status[bike]:
                bike_status[bike] = True
                worker_status[worker] = bike
                pair_count += 1
                
                # If all the workers have the bike assigned, we can stop
                if pair_count == len(workers):
                    return worker_status
        
        return worker_status