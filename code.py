class Solution:
    def myAtoi(self, str):
        import re
        ret = re.search('^(([+|-]\d+)|\d+)',str.strip())
        if ret:
            ret = ret.group()
            ret_int = int(ret)
        else:
            ret_int = 0
        if ret_int > 2147483647:
            ret_int = 2147483647
        elif ret_int < -2147483648:
            ret_int = -2147483648
        return ret_int
