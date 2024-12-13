class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        cur = 0
        while i < len(chars):
            group_length = 1

            # find grouplength
            while (i + group_length < len(chars) and chars[i + group_length] == chars[i]):
                group_length += 1

            # update character
            chars[cur] = chars[i]
            cur += 1

            # update grouplength
            if group_length > 1:
                str_repr = str(group_length)
                chars[cur: cur+len(str_repr)] = list(str_repr)
                cur += len(str_repr)
            
            i += group_length
        
        return cur