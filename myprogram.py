company = "ABC Data"
phone = "555-123-009"
employees = 25
remote_work = True
big_company = employees > 100
income = 4500000
income_per_person = income / employees
blabla = False 

list=[type (company),type (phone), type (employees),type (remote_work),type (big_company), type (income), type (income_per_person), type (blabla)  ]

str=0
int=0
bool=0
float=+0

for i in range (len(list)):
    print(list[i])

    if list[i] == type("str"):
        str = str+1
    elif list[i] == type(2/2):
        float = float+1
    elif list[i] == type(2+2==4):
        bool = bool+1
    else: int=int+1

    
print ("str:", str)
print ("int:", int)
print ("bool:", bool)
print ("float:", float)

