from Project import Project

class Employee(Project):
    def __init__(self, name, contact, sap, manager, project, role, pay) :
        #Fill your code
        self._name=name
        self._contact=contact
        self._sap=sap
        self._manager=manager
        self._project=project
        self._role=role
        self._pay=pay
        self._email=self._name+self._sap+"@hcl.com"
        self._login={}
        self._login[self._sap]=str(contact)
        self._log=[]
        self._checkins=[]
        self._checkouts=[]

    def change_password(self,password):
        self._login[self._sap]=password
        print("\nPassword changed successfully\n")

    def update_log(self,log):
        self._log.append(log)
        print("\n\'{}\' is updated to log".format(log))

    def check_in(self,time):
        self._checkins.append(time)
        print("\nChecked in at {}".format(time))

    def check_out(self,time):
        self._checkouts.append(time)
        print("\nChecked out at {}".format(time))
    
    def emp_display(self):
        print("\nName: {}\nSAP Code: {}\nReports to: {}\nProject: {}\ncontact number: {}\nemail address: {}\n".format(self._name,self._sap,self._manager,self._project,self._contact,self._email))