class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        st = [0]
        
        while st:
            node = st.pop()
            for nei in rooms[node]:
                if not seen[nei]:
                    seen[nei] = True
                    st.append(nei)
        return all(seen) #returns True iff we've visited every room