#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
print("\t\tWelcome to Address Book\n1. Add_contact\n2. Display_contact\n3. Delete_contact\n4. Modify_contact\n5. Search_contact")
choice = input("\nEnter your choice: ")
print("\nEnter 0 to exit")


# In[2]:


def pickle_write():
    with open('contacts.pickle', 'wb') as file:
        pickle.dump(contact_list, file, protocol=pickle.HIGHEST_PROTOCOL)


def pickle_get():
    with open('contacts.pickle', 'rb') as file:
        try:
            list = pickle.load(file)
        except EOFError:
            list = []
        return list


# In[3]:


contact_list = pickle_get()
if not contact_list:
    pickle_write()


# In[5]:


while choice:
    if choice == "1":
        name = input("Enter contact name: ")
        email = input("Enter contact email: ")
        phone = input("Enter contact number: ")
        contact_details = {"name": name, "email": email, "phone": phone}
        contact_list.append(contact_details)
        pickle_write()
        print("\nContact successfully added")

    elif choice == "2":
        contact_list = pickle_get()
        if contact_list:
            for i in contact_list:
                print(
                    f"\nName: {i['name']}\nEmail: {i['email']}\nContact Number: {i['phone']}")
        else:
            print("No such contact in address book")

    elif choice == "3":
        contact_list = pickle_get()
        if not contact_list:
            print("Address book empty. No contact to delete")
        else:
            name = input("Enter contact name: ")
            for i in contact_list:
                if i["name"] == name:
                    contact_list.remove(i)
                    print("Contact Successfully Deleted")
                    pickle_write()
                    break
            else:
                print("No contact with this name")

    elif choice == "4":
        contact_list = pickle_get()
        if not contact_list:
            print("Address book empty. No contact to modify")
        else:
            name = input("Enter contact name: ")
            for i in range(len(contact_list)):
                if contact_list[i]["name"] == name:
                    name = input("Enter new name: ")
                    email = input("Enter new email: ")
                    phone = input("Enter new number: ")
                    contact_details = {"name": name,
                                    "email": email, "phone": phone}
                    contact_list[i] = contact_details
                    print("\nContact modified")
                    pickle_write()
                    break
            else:
                print("No contact with this name found")

    elif choice == "5":
        contact_list = pickle_get()
        if not contact_list:
            print("Address book empty. No contact to delete")
        else:
            name = input("Enter contact name: ")
            for i in contact_list:
                if i["name"] == name:
                    print("Email:", i["email"])
                    print("Contact Number:", i["phone"])
                    break
            else:
                print("No contact with this name found")
    elif choice == "0":
        print("\n\nThanks for logging in :)")
        break
    else:
        print("Invalid Choice!!!")
    choice = input("\nEnter your choice: ")


# In[ ]:




