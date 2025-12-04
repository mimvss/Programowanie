company = "ABC Data"
phone = "555-123-009"
employees = 25
remote_work = True
big_company = employees > 100
income = 4500000
income_per_person = income / employees

names=["company", "phone", "employees","remote_work","big_company", "income", "income_per_person" ]
list=[company, phone, employees,remote_work,big_company, income, income_per_person ]

str=0
int=0
bool=0
float=+0

for i in range (len(list)):
    print(f'var name:{names[i]}, value: {list[i]}, value type: {type (list [i]).__name__}  ')


    if type (list[i]) == type("str"):
        str = str+1
    elif type (list[i]) == type(2/2):
        float = float+1
    elif type (list[i]) == type(2+2==4):
        bool = bool+1
    else: int=int+1

    
print ("str:", str)
print ("int:", int)
print ("bool:", bool)
print ("float:", float)

