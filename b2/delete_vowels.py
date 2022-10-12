class Soluiton(object):
    
    def removeVowels(self, s):
        s = s.replace('a','')
        s = s.replace('e','')
        s = s.replace('i','')
        s = s.replace('o','')
        s = s.replace('u','')

        return s

obj_1 = Soluiton()

print(obj_1.removeVowels(input('Enter a string: ')))       