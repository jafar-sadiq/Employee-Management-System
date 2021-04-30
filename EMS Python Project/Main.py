from Project import Project
from Employee import Employee
from Manager import Manager
from Admin import Admin
import datetime


#admin object is created
admin1_name,admin1_sap,admin1_contact=("admin1","admin1",12345)
admin1=Admin(admin1_name,admin1_sap,admin1_contact)


#manager object is created
name,sap,project,pay,contact=("mngr1","mngr1","prj1","50000",12345)
mngr1=Manager(name,sap,project,pay,contact)
admin1.add_manager(mngr1)

#employees' objects is created
#employee 1
name,contact,sap,manager,project,role,pay=("emp1",12345,"emp1","mngr1","prj1","SE","20000")
emp1=Employee(name,contact,sap,manager,project,role,pay)
mngr1.add_employee(emp1)
#employee 2
name,contact,sap,manager,project,role,pay=("emp2",12345,"emp2","mngr1","prj1","TE","17000")
emp2=Employee(name,contact,sap,manager,project,role,pay)
mngr1.add_employee(emp2)

#adding project
name,client,cost,manager=("prj1","client1","500000","mngr1")
prj1=Project(name,client,cost,manager)
admin1.add_project(prj1)

print("\n\n---------------Welcome to Employee Management System--------------------")

while True:
    print("\nSelect the option from below\n1. Login as Admin\n2. Login as Manager\n3. Login as Employee\n4. Exit\n\nEnter your choice : ",end=" ")
    ch=int(input())
    
    #admin section
    if ch==1:
        sap=input("Please enter sap id : ")
        password=input("Please enter password : ")
        if admin1._login[sap]!=password:
            print("\nInvalid credentials\n")
            continue

        print("\nWelcome to Admin Section\n")
        while True:
            print("\nSelect the option from below\n1. Add Manager\n2. Remove Manager\n3. Add project\n4. Remove project\n5. Display Managers\n6. Display employees under each manager\n7. Display projects\n8. Change Password\n9. Logout\n\nEnter your choice : ",end=" ")
            ch2=int(input())
            if ch2==1:
                print("Enter enter the details of the manager to be added in comma separated values\nEx: (name,sap,project,pay,contact)")
                name,sap,project,pay,contact=input().split(',')
                mngr_obj=Manager(name,sap,project,pay,contact)
                admin1.add_manager(mngr_obj)
            elif ch2==2:
                sap1=input("Enter the sap id of the manager to be removed : ")
                mngr_obj=admin1._managers_dict[sap1]
                admin1.remove_manager(mngr_obj)
            elif ch2==3:
                print("Enter enter the details of the project to be added in comma separated values\nEx: (name,client,cost,manager)")
                name,client,cost,manager=input().split(',')
                prj_obj=Project(name,client,cost,manager)
                admin1.add_project(prj_obj)
            elif ch2==4:
                name=input("Enter the name of the project to be removed : ")
                if name in admin1._projects_dict:
                    prj_obj=admin1._projects_dict[name]
                    admin1._projects_list.remove(prj_obj)
                else:
                    print("\nNo project found\n")

            elif ch2==5:
                admin1.print_managers()

            elif ch2==6:
                admin1.print_employees_under_each_manager()

            elif ch2==7:
                admin1.projects_details()

            elif ch2==8:
                curr_password=input("Enter current password : ")
                if admin1._login[admin1_sap]==curr_password:
                    new_password=input("Enter new password : ")
                    admin1.change_password(new_password)
                else:
                    print("Invalid Password")

            elif ch2==9:
                print("\nLogged out successfully\n")
                break

            else:
                print("\nInvalid choice\n")
                break

    #manager section
    elif ch==2:
        mngr_sap=input("Please enter sap id : ")
        if mngr_sap in admin1._managers_dict:
            mngr_obj=admin1._managers_dict[mngr_sap]
        else:
            print("\nsap id not found\n")
            continue

        password=input("Please enter password : ")
        if mngr_obj._login[mngr_sap]!=password:
            print("\nInvalid credentials\n")
            continue

        print("\nWelcome to Manager Section\n")
        while True:
            print("\nSelect the option from below\n1. Add employee\n2. Remove employee\n3. display employees\n4. Change Password\n5. My profile\n6. Logout\n\nEnter your choice : ",end=" ")
            ch2=int(input())
            if ch2==1:
                print("Enter enter the details of the employee to be added in comma separated values\nEx: (name, contact, sap, manager, project, role, pay)")
                name, contact, sap, manager, project, role, pay=input().split(',')
                emp_obj=Employee(name,contact,sap,manager,project,role,pay)
                mngr_obj.add_employee(emp_obj)

            elif ch2==2:
                sap1=input("Enter the sap id of the employee to be removed : ")
                emp_obj=mngr_obj._employees_dict[sap1]
                mngr_obj.remove_employee(emp_obj)

            elif ch2==3:
                mngr_obj.display_employees()

            elif ch2==4:
                curr_password=input("Enter current password : ")
                if mngr_obj._login[mngr_sap]==curr_password:
                    new_password=input("Enter new password : ")
                    mngr_obj.change_password(new_password)
                else:
                    print("\nInvalid Password\n")

            elif ch2==5:
                mngr_obj.display()

            elif ch2==6:
                print("\nLogged out successfully\n")
                break

            else:
                print("\nInvalid choice\n")
                break
    
    #Employee section
    elif ch==3:
        mngr_sap=input("Please enter sap id of your manager : ")
        if mngr_sap in admin1._managers_dict:
            mngr_obj=admin1._managers_dict[mngr_sap]
        else:
            print("\nmanager not found\n")
            continue

        emp_sap=input("Please enter your sap id : ")
        if emp_sap in mngr_obj._employees_dict:
            emp_obj=mngr_obj._employees_dict[emp_sap]
        else:
            print("\nsap id not found\n")
            continue

        password=input("Please enter password : ")
        if emp_obj._login[emp_sap]!=password:
            print("\nInvalid credentials\n")
            continue

        print("\nWelcome to Employee Section\n")
        while True:
            print("\nSelect the option from below\n1. Check in\n2. Check out\n3. Update log\n4. Change Password\n5. My profile\n6. Logout\n\nEnter your choice : ",end=" ")
            ch2=int(input())
            if ch2==1:
                time=datetime.datetime.now()
                emp_obj.check_in(time)

            elif ch2==2:
                time=datetime.datetime.now()
                emp_obj.check_out(time)

            elif ch2==3:
                report=input("\nEnter the work report\n")
                emp_obj.update_log(report)

            elif ch2==4:
                curr_password=input("Enter current password :")
                if emp_obj._login[emp_sap]==curr_password:
                    new_password=input("Enter new password : ")
                    emp_obj.change_password(new_password)
                else:
                    print("\nInvalid Password\n")

            elif ch2==5:
                emp_obj.display()

            elif ch2==6:
                print("\nLogged out successfully\n")
                break

            else:
                print("\nInvalid choice\n")
                break

    elif ch==4:
        print("\nThank You, Have a good day\n")
        break
    else:
        print("\nInvalid choice\n")
        break   
