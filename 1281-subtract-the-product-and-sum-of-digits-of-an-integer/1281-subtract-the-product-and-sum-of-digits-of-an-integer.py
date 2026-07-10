class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp=n
        sum_num=0
        pro_num=1
        while temp>0:
            r=temp%10
            temp//=10
            sum_num+=r
            pro_num*=r

        return pro_num - sum_num    
        