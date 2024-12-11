class Solution:
    def checkValid(self, flowerbed: List[int], pot: int) -> bool:
        return flowerbed[pot] == 0

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        curr_consec_zero = 0
        has_flower = False

        for pot in flowerbed:
            if pot == 0:
                curr_consec_zero += 1
            else:
                if not has_flower:
                    count += curr_consec_zero // 2
                elif curr_consec_zero > 2:
                    count += (curr_consec_zero-1) // 2
                
                curr_consec_zero = 0
                has_flower = True

        if not has_flower:
            count += (curr_consec_zero+1) // 2
        else:
            count += curr_consec_zero // 2
        
        return count >= n


        #     checkFront = checkBack = False
        #     # check if adjecent front in empty
        #     if (flowerbed[pot] == 0):
        #         if (pot == 0):
        #             checkFront = True
        #         else :
        #             checkFront = self.checkValid(flowerbed, pot-1)
            
        #         if (pot == len(flowerbed)-1):
        #             checkBack = True
        #         else :
        #             checkBack = self.checkValid(flowerbed, pot+1)

        #     print(pot, checkBack, checkFront)
        #     if (checkBack and checkFront):
        #         flowerbed[pot] = 1
        #         count += 1
        #         if count >= n:
        #             return True

        # return n <= 0

