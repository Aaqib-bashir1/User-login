import random
class Authenticate:
    def __init__(self):
        self.username=input("Enter your username: ")
        self.password=input("Enter your password: ")
        self.otp=self.otp_genrator()
        print(self.otp)
        self.h_otp=self.hash_function(self.otp)
        self.create_user()


    def otp_genrator(self):
        string="0123456789"
        otp="".join(random.choices(string,k=9))
        return otp
    def hash_function(self,otp):
        ascii_values=[ord(string) for string in otp ]
        partitions=[ascii_values[i:i+2] for i in range(0,len(ascii_values),2) ]
        hash_value=sum(sum(partition) for partition in partitions)
        hash_value=hash_value % (10**2)
        return hash_value
    def __str__(self):
        return (f"otp is {self.otp} and hashed otp is{self.h_otp}")
    def create_user(self):
        with open("users.txt","a") as file:
            file.write(str({self.h_otp:(self.username,self.password,self.otp)}))
            file.write(",\n")


class User_retriver(Authenticate):
    def __init__(self):
        self.otp = input("enter your otp")
        self.user = self.retrieve_user()


    def retrieve_user(self):
        with open("users.txt", "r") as f:
            data = f.read()
            self.user_data = eval("["+data+"]")
        hashed_otp = self.hash_function(self.otp)

        for i in self.user_data:
            if hashed_otp in i:
                return (i[hashed_otp])
    def hash_function(self, otp):
        ascii_values = [ord(string) for string in otp]
        partitions = [ascii_values[i:i + 2] for i in range(0, len(ascii_values), 2)]
        hash_value = sum(sum(partition) for partition in partitions)
        hash_value = hash_value % (10 ** 2)
        return hash_value
    def __str__(self):
        return str(self.user)

# a=Authenticate()
# b=Authenticate()
# c=Authenticate()
user=User_retriver()
print(user)
