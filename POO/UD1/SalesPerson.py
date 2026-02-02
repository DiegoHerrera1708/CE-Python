import random
class SalesPerson:  
    total_revenue = 0
    names = [] 
    def __init__(self,name):
        self.name = name
        self.sales_amount = 0
        self.names.append(name)
 
    def make_sale(self,money):
        self.sales_amount += money
        SalesPerson.total_revenue += money
    
    def show(self):
        print(self.name, self.sales_amount)

 
s1 = SalesPerson('Alumno1')
s2 = SalesPerson('Alumno2')
s3 = SalesPerson('Alumno3')
s4 = SalesPerson('Alumno4')
s5 = SalesPerson('Alumno5')
s6 = SalesPerson('Alumno6')
s7 = SalesPerson('Alumno7')
s8 = SalesPerson('Alumno8')    
s9 = SalesPerson('Alumno9')
s10 = SalesPerson('Alumno10')
s11= SalesPerson('Alumno11')
s12 = SalesPerson('Alumno12')

list = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12]
 
for i in list: 
    i.make_sale(random.randint(1000, 3000))
    i.show()


print(SalesPerson.names)
print(SalesPerson.total_revenue)
