import json

def get_employeedetails():
    data={}
    data['name']=input("Enter employee name: ")
    data['id']=input("Enter id: ")
    data['roll']=input("Enter job roll: ")
    data['qualification']=input("Enter qualification: ")
    data['salary']=input("Enter Salary: ")
    return (data)
out=[]
while True:
    quit=input("Enter Y/N to continue")
    if quit.lower() == 'n':
        break
    record = get_employeedetails()
    out.append(record)

with open('employee-details.json','w') as file:
    json.dump(out,file,indent=2)