from Project import Project
from Employee import Employee
from Manager import Manager

class Admin(Manager,Employee,Project):
    
    def __init__(self, name,sap,contact):
        #Fill your code
        self._name=name
        self._sap=sap
        self.contact=contact
        self._managers_list=[]
        self._managers_dict={}
        self._projects_list=[]
        self._projects_dict={}
        self._login={}
        self._login[self._sap]=str(contact)

    def change_password(self,password):
        self._login[self._sap]=password
        print("\nPassword changed successfully")
        
    def add_manager(self, mngr):
        #Fill your code
        self._managers_list.append(mngr)
        self._managers_dict[mngr._sap]=mngr
        print("\nManager added successfully")

    def remove_manager(self, mngr):
        #Fill your code
        self._managers_list.remove(mngr)
        print("\nManager deleted successfully")
    
    def add_project(self, prj):
        #Fill your code
        if prj._manager in self._managers_dict:
            self._projects_list.append(prj)
            self._projects_dict[prj._name]=prj
            print("\nProject Added Successfully")
        else:
            print("\nManager Not Found")

    def remove_project(self, prj):
        #Fill your code
        self._projects_list.remove(prj)
        print("\nProject Removed Successfully")

    def print_managers(self):
        #Fill your code
        print("\nManagers' List :\n")
        if len(self._managers_list)==0:
            print("No managers found")
        else:
            for i in self._managers_list:
                i.mngr_display()

    def print_employees_under_each_manager(self):
        #Fill your code
        if len(self._managers_list)==0:
            print("\nNo managers found")
        else:
            for i in self._managers_list:
                print("\nManager Name : {}".format(i._name))
                print("\nEmployee List :\n")
                i.display_employees()
                print("\n")
    
    def projects_details(self):
        for i in self._projects_list:
            print('\n')
            i.prj_display()
            print("\n")