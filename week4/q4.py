class q4:

    str =' '
    def getstring(self,string):
        self.str=string

    def uppercase(self):
        result = ''
        str_data=self.str
        for char in str_data:
            if ord(char) >= 97:
                result += chr(ord(char) - 32)
        print(result)


aux=q4()


s = str(input("enter a string "))
aux.getstring(s)
aux.uppercase()


