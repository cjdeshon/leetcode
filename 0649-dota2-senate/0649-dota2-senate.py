class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        
        #fill queues with senators index
        r_queue = deque()
        d_queue = deque()
        
        #populate queues
        for i,s in enumerate(senate):
            if s == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)
                
        #while both parties have senator
        while r_queue and d_queue:
            #pop next turn from both and compare
            r_turn = r_queue.popleft()
            d_turn = d_queue.popleft()
            #add leftmost back into queue
            if d_turn < r_turn:
                d_queue.append(d_turn + n)
            else:
                r_queue.append(r_turn + n)
                
        return "Radiant" if r_queue else "Dire"
        