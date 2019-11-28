#!/usr/bin/env python3
import os
import time

class CompanyProfile:
    def __init__(self,name,address,website,email,domain="IT company",contact="NA"):
        self.name = name
        self.address = address
        self.domain = domain
        self.website = website
        self.email = email
        self.contact = contact
    def add(self):
        with open("list_of_IT_companay.md","a",newline="") as f:
            data = f''' |{self.name} | [GOTO]({self.website}) | {self.domain} | {self.email} | {self.address} |{self.contact}'''
            f.write(data) 
    def git_push(self):
        os.system("git add .")
        print("Added to the git")
        time.sleep(5)
        os.system(f'git commit -m "{self.name } is added to the list"')
        print(f"Committed for {self.name}")
        time.sleep(5)
        os.system("git push")
        print("Pushed")

if __name__ == "__main__":
    print("Enter the details of company \n")
    name = input("Enter the name of company ")
    website = input("provide the link of company ")
    address = input("Address of the company ")
    contact = input("Contact number of the company ")
    email = input("Email ")
    domain = input("Which is the domain of company ")
    company = CompanyProfile(name,address,website,email,domain,contact)
    company.add()
    company.git_push()
