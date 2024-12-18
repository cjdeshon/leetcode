class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        st = []
        for asteroid in asteroids:
            if asteroid>0:
                st.append(asteroid)
            else:
                #check negative big collisions
                while len(st)>0 and st[-1]<abs(asteroid):
                    st.pop()
                    
                #check total annilation 
                if len(st)==0:
                    ans.append(asteroid)
                    
                #negative small and equal collisions
                else:
                    if st[-1] == abs(asteroid):
                        st.pop()
        ans += st
        return ans
                    