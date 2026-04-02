class RomanConverter:

    def int_to_roman(self,num):
  


        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
 

        roman_num = ""
        i = 0

        while num >0:
             for j in range(num // val[i]):
                roman_num = roman_num + syms[i]
                num = num - val[i]
             i = i + 1

        return roman_num




number = int(input("Enter an integer; "))


converter = RomanConverter()


result = converter.int_to_roman(number)
print("Roman numeral:", result)

