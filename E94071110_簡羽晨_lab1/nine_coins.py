import random 
class Nine_Coins:
    def __init__(self,decimal):
        self.decimal = decimal
    def toss(self):                    # command line: c=toss()
        x = random.randint(1, 512)     # toss的方法利用隨機方式生成
        self.decimal = x
        
    def __repr__(self):     # command line: c
        binary = format(int(self.decimal),'09b')     # 將self.decimal轉成九位數的二進制
        ht = []                                      # 宣告一個list等等要用來存放由0、1轉成的H、T
        for i in range(len(binary)):                 # 建立一個迴圈，範圍是binary這個數字的長度
            if binary[i]=="1":                       # 若是"1"，ht放入"T"
                ht.insert(i,"T")
            else:                                    # 若是"0"，ht放入"H"
                ht.insert(i,"H")
        listToStr = ''.join([str(elem) for elem in ht])     # convert a list to string
        return f'Nine_coins: {listToStr}'

        #return f'{list(self.binary)}'
        #list = []
        #for i in range(len(self.binary)):
        #    list.insert(i,self.binary[i])
        #return f'{list}'

    def __str__(self):      # command line: print(c)
        binary = format(int(self.decimal),'09b')
        return f'binary: {binary} and decimal: {self.decimal} '
    

