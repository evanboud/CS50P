class Jar:
    def __init__(self, capacity=12, cookies=0,):
        self.capacity = capacity
        self.cookies = cookies 
        
    def __str__(self):
        emjois = self._cookies * "🍪"
        return f"{emjois}"
    def deposit(self, n):
        self.cookies = self.cookies + n 

    def withdraw(self, n):
        self.cookies = self.cookies - n 
    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
    

    @property
    def cookies(self):
        return self._cookies 
    @cookies.setter 
    def cookies(self, cookies):
        if cookies < 0:
            raise ValueError
        elif cookies > self._capacity: 
            raise ValueError
        self._cookies = cookies
        

def main():
    ...

if __name__ == "__main__":
    main()