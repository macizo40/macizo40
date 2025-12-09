#on this excersise we will built a table that will be saved in a file this will helps to make the data permanent


"""
     Value 1  Value 2  Value 3
A      AA       BB       CC
B      AA       BB       CC
C      AA       BB       CC

"""

#the idea is to use pickle as part of the propoerties that we will use

from io import open
import pickle

class Client:

    def __init__(self,name,mobile,social_network):
        self.name = name
        self.mobile = mobile
        self.social_network = social_network

    def __str__(self):
        return (f" Client {self.name}, mobile {self.mobile} and social network {self.social_network}")

class Client_Catalog:
    #having a list where we will store the clients data
    clients_list = []

    #constructor to call a load method from the file with pickle

    def __init__(self):
        self.load_client_file()

    def add_client_name(self,cli):
        for temp in self.clients_list:
            if temp.name == cli.name:
                return
        self.clients_list.append(cli)
        self.save_to_file()

    def delete_client_name(self,name):
        for temp in self.clients_list:
            if temp.name == name:
                self.clients_list.remove(temp)
                self.save_to_file()
                print("Client {} is deleted".format(temp.name))
                return


    def show_clients(self):
        if len(self.clients_list) == 0:
            print("client file is empty")
            return
        for c in self.clients_list:
            print(c)

    def load_client_file(self):
        file = open('practice/files/my_gym_file.pckl','ab+')
        file.seek(0)
        try:
            self.clients_list = pickle.load(file) #first time does not exist and will pass to the next block
        except: 
            print("File is empty or is the first time that is created")
        finally:
            file.close() #in case that error we always close it
            print("We have loaded {} objects from the file".format(len(self.clients_list)))

    def save_to_file(self):
        #this save file process will be used to replace all the content of the file always.
        file = open('practice/files/my_gym_file.pckl','wb')
        pickle.dump(self.clients_list,file)
        file.close()

    

Catalog_new_users = Client_Catalog()
Catalog_new_users.show_clients()

Catalog_new_users.add_client_name(Client ("Jenna Kelly",9334567347,"@jenna_k"))
Catalog_new_users.add_client_name(Client ("Jill Patrick",9331117347,"@jill_patrick"))
Catalog_new_users.add_client_name(Client ("Tera Jameson",9334533347,"@terajameson_1998"))

Catalog_new_users.show_clients()

Catalog_new_users.delete_client_name("Jenna Kelly")
Catalog_new_users.show_clients()
