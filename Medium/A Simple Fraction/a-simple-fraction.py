#User function Template for python3
class Solution:
   def fractionToDecimal(self, numerator, denominator):
       # Code here
       nr = numerator
       result = ""

       quot, nr = divmod(nr, denominator)
       result += str(quot)
       
       if nr:
           table = {}
           recurring = False
           fraction = ""
           pos = 0
           while nr:
               if table.get(nr) != None:
                   recurring = True
                   pos = table[nr]
                   break
               else:
                   table[nr] = pos
                   nr *= 10
                   quot, nr = divmod(nr, denominator)
                   fraction += str(quot)
                   pos += 1
                   
           if recurring:
               fraction = fraction[:pos] + '(' + fraction[pos:] + ')'
           result += '.' + str(fraction)
       
       return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		numerator, denominator = input().split()
		numerator = int(numerator); denominator = int(denominator)
		ob = Solution()
		ans = ob.fractionToDecimal(numerator, denominator)
		print(ans)
# } Driver Code Ends