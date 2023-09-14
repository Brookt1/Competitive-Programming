class DataStream:
    

    def __init__(self, value: int, k: int):
        self.value=value
        self.k=k
        self.counter=0
        
        
    # counter=0
    def consec(self, num: int) -> bool:
        
        if num==self.value:
            self.counter+=1
        else: 
            if self.counter!=0: self.counter-=1
        print(self.counter)
        if self.k==self.counter: 
            
            self.counter-=1
            return True
        else: return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
