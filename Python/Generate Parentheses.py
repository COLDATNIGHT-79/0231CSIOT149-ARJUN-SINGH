#added n as an integer that cn be added value to by the user
n = int(input("Input desired value "))
class Solution(object):2
   
    
def generateParenthesis(self,n,currentString = '',close = 0):
        if n == 1 and close == 0:
              return [currentString + "()"]
        elif n == 0 and close == 1:
              return [currentString + ")"]
        elif n == 0 and close == 0:
              return [currentString]  

        allPossibleVariations = []  

        if n >= 1:
            getSubVariations = self.generateParenthesis(n-1,currentString+"(",close+1)
            if type(getSubVariations) != str:
                  for item in getSubVariations:
                       allPossibleVariations.append(item)
            else:
                 allPossibleVariations.append(getSubVariations)

        if close >= 1:
            getSubVariations = self.generateParenthesis(n,currentString+")",close-1)
            if type(getSubVariations) != str:
                for item in getSubVariations:
                    allPossibleVariations.append(item)
            else: allPossibleVariations.append(getSubVariations)
        return allPossibleVariations
solution = Solution()
result = solution.generateParenthesis(n+1)

for combination in result:
    print(combination)
