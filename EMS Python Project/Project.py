class Project:
    def __init__(self, name, client, cost, manager):
        #Fill your code
        self._name= name
        self._client=client
        self._cost= cost
        self._manager= manager
        self._team=[]


    def add_member(self,name,role):
        self.team.append((name,role))
        print("\nMember added to the team")

    def remove_member(self,name,role):
        self.team.remove((name,role))
        print("\nMember removed from team")
    
    def update_status(self,new_status):
        self._statusPercentage=new_status
        print("\nStatus updated successfully")

    def prj_display(self) :
        #Fill your code
        print("\nName of the project : {}".format(self._name))
        print("Name of the client : {}".format(self._client))
        print("Cost of the project : {}".format(self._cost))
        print("Project Assigned to : {}".format(self._manager))
        
            
