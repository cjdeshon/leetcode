class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length

        # fill in left products
        answer[0] = 1
        for i in range(1,length):
            answer[i] = nums[i-1] * answer[i-1]

        # use interger variable for right products
        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer

        # #creat list containing all products going left
        # preProd = [0] * length
        # preProd[0] = 1
        # for i in range(1, length):
        #     preProd[i] = nums[i - 1] * preProd[i - 1]


        # #create post prodoct list
        # postProd = [0] * length
        # postProd[length-1] = 1
        # for i in reversed(range(length-1)):
        #     postProd[i] = nums[i+1] * postProd[i+1]

        # #check list
        # print(preProd, postProd)


        # #construct final list
        # answer = [0] * length
        # for i in range(length):
        #     answer[i] = preProd[i] * postProd[i]

        # return answer
