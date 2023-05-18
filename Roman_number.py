import re

class Roman:
    def __init__(self,roman=None):
        if str(roman).isdigit():
            self.number = roman
            self.digits_to_roman()
        elif roman is None:
            self.roman = ' '
            self.number = 0
        else:
            self.roman = roman
            if self.is_roman():
                self.roman_to_digits()
            else:
                raise Exception("Please enter a proper roman number")

    def is_roman(self):
        self.roman = str(self.roman).upper()
        rom = re.compile(r'''^(-)?([M]{0,3}[-\s]?)?
        ([D][C]{0,3}[-\s]?|[C][D][-\s]?|[C][M][-\s]?|[C]{1,3}[-\s]?)?
        ([L][X]{0,3}[-\s]?|[X][L][-\s]?|[X][C][-\s]?|[X]{1,3}[-\s]?)?
        ([V][I]{0,3}|[I][V]|[I][X]|[I]{1,3})?$''',re.VERBOSE) 
        data = rom.search(self.roman)
        if data is None:
            return False
        for i in self.roman:
            if i not in ['-','C','M','D','V','X','L','I',' ']:
                return False
        if len(self.roman)>19:
            return False   
        return True
    

    def roman_to_digits(self):
        one = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9}
        two = {'X':1,'XX':2,'XXX':3,'XL':4,'L':5,'LX':6,'LXX':7,'LXXX':8,'XC':9}
        three = {'C':1,'CC':2,'CCC':3,'CD':4,'D':5,'DC':6,'DCC':7,'DCCC':8,'CM':9}
        four = {'M':1,'MM':2,'MMM':3}
        if self.is_roman() is False:
            raise Exception ("Please enter a proper roman number with - or space after each element")       
        if self.roman[0] == '-':
            roman_number='-'
            for i in self.roman:
                if i not in [' ','-'] :
                    roman_number+=i  
        else:
            roman_number=''
            for i in self.roman:
                if i not in [' ','-'] :
                    roman_number+=i 

        rom = re.compile(r'''^(-)?([M]{0,3}[-\s]?)?
        ([D][C]{0,3}[-\s]?|[C][D][-\s]?|[C][M][-\s]?|[C]{1,3}[-\s]?)?
        ([L][X]{0,3}[-\s]?|[X][L][-\s]?|[X][C][-\s]?|[X]{1,3}[-]?)?
        ([V][I]{0,3}|[I][V]|[I][X]|[I]{1,3})?$''',re.VERBOSE) 
        data = rom.search(roman_number)
        m,f,th,tw,o = data.groups()
        if m is  None:
            number = str(four.get(f,''))+str(three.get(th,0))+str(two.get(tw,0))+str(one.get(o,0))
            number = int(number)
        else:
            number = '-'+str(four.get(f,''))+str(three.get(th,0))+str(two.get(tw,0))+str(one.get(o,0))
            number = int(number) 
        self.number = number  
        return number
    
    def digits_to_roman(self):
        one = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX'}
        two = {'1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6':'LX','7': 'LXX', '8': 'LXXX', '9': 'XC'}
        three = {'1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM'}
        four = {'1': 'M', '2': 'MM', '3': 'MMM'}

        if str(self.number)[0] == '-':
            k = 1 
            number = ''
            for i in str(self.number)[1:]:
                number += i
            self.number = int(number)  
        else:
            k=0      

        if not str(self.number).isdigit():
            raise Exception ("Please enter a proper digit (1-9)")
        elif self.number>3999:
            raise Exception ("Please enter a digit smaller than 3999")

        num = str(self.number)
        if self.number>999:
            f = four.get(num[0],None)
            th = three.get(num[1],None)
            tw = two.get(num[2],None)
            o = one.get(num[3],None)
        elif self.number>99:
            f = None
            th = three.get(num[0],None)
            tw = two.get(num[1],None)
            o = one.get(num[2],None)
        elif self.number>9:
            f = None
            th = None
            tw = two.get(num[0],None)
            o = one.get(num[1],None)
        elif self.number>0:
                f = None
                th = None
                tw = None
                o = one.get(num[0],None)

        
        num = [f,th,tw,o]
        if k == 1 :
            roman_number = '-'
        else:
            roman_number = ''    
        for i in num:
            if i is not None:
                roman_number += i + ' '
        self.roman = roman_number
        return roman_number  


    def __add__ (self,roman):
        num1 = self.roman_to_digits()
        num2 = roman.roman_to_digits()
        num = num1 + num2
        roman = Roman(num)
        roman.digits_to_roman()
        return roman
    

    def __sub__(self,roman):
        num1 = self.roman_to_digits()
        num2 = roman.roman_to_digits()
        if num1>num2:
            num = num1 - num2
            roman = Roman(num)
            rom = roman.digits_to_roman()
            return roman
        else:
            num = num2 - num1
            roman = Roman(num)
            rom1 = roman.digits_to_roman()
            rom = '-'
            for i in rom1:
                rom +=i
            roman = Roman(rom)    
            return roman
    

    def __mul__(self,roman):
        num1 = self.roman_to_digits()
        num2 = roman.roman_to_digits()
        num = num1 * num2
        roman = Roman(num)
        rom = roman.digits_to_roman()
        roman = Roman(rom)
        return roman
    

    def __truediv__(self,roman):
        num1 = self.roman_to_digits()
        num2 = roman.roman_to_digits()
        num = int(num1 / num2)
        roman = Roman(num)
        rom = roman.digits_to_roman()
        roman = Roman(rom)
        return roman   
   
    
    def __eq__(self,roman):
        num1 = self.number
        num2 = roman.number
        if num1==num2:
            return True
        else:
            return False
        
    def __str__(self) -> str:
        return self.roman

        