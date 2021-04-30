from Project import Project
from Employee import Employee

class Manager(Employee,Project):
    
    def __init__(self, name, sap, project, pay, contact):
        #Fill your code
        self._name=name
        self._sap=sap
        self._project=project
        self._pay=pay
        self._contact=contact
        self._email=self._name+self._sap+"@hcl.com"
        self._employees_list=[]
        self._employees_dict={}
        self._login={}
        self._login[self._sap]=str(contact)

    def change_password(self,password):
        self._login[self._sap]=password
        print("\nPassword changed successfully")
        
    def add_employee(self, emp):
        #Fill your code
        self._employees_list.append(emp)
        self._employees_dict[emp._sap]=emp
        print("\nEmployee Added Successfully")

    def remove_employee(self, emp):
        #Fill your code
        self._employees_list.remove(emp)
        print("\nEmployee Removed Successfully")
    
    def display_employees(self):
        if len(self._employees_list)==0:
            print("\nNo employees found")
        else:
            for i in self._employees_list:
                i.emp_display()
    
    def mngr_display(self):
        print("\nName: {}\nSAP Code: {}\nProject: {}\ncontact number: {}\nemail address: {}\n".format(self._name,self._sap,self._project,self._contact,self._email))