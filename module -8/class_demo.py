class calc :
    x=0
    y=0

    def get(self , x,y):
        self.x=x
        self.y = y

    def product(self):
        return self.x + self.y,self.x -self.y , self.x* self.y,self.x%self.y
        
         
    
        
    

C=calc()
C.get (12,50)
ans=C.product()
print("product :",ans)



    
    


    





        




       