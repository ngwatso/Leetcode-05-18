class Solution:
    def defangIPaddr(self, address: str) -> str:
       
        return address.replace(".", "[.]")

# ===============

class Solution:
    def interpret(self, command: str) -> str:
        
        newStr = ""

        for i in range(len(command)):
            print('index i', i)
            print('i', command[i])
            if i != len(command) - 1:
                j = command[i+1]
            if command[i] == "(":
                print('j', j)
                if j == ")":
                    newStr += "o"
                elif j == "a":
                    newStr += "al"
            elif command[i] == "G":
                newStr += "G"
            else:
                continue

        return newStr
        
        
        
'''

U:

"G()(al)"
output = "Goal"

"()()()()()()()"
output = "ooooooo"

P:

Iterate through command; if G, newStr += "G", if "(", check next index; if ")", newStr += "o", if "a", newStr += "al"
'''

# ===============

