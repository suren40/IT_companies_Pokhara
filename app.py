class CompanyProfile:
    def __init__(self,name,address,website,email,domain="IT company"):
        self.name = name
        self.address = address
        self.domain = domain
        self.website = website
        self.email = email
    def add(self):
        with open("list_of_IT_companay.md","a",newline="") as f:
            data = f''' |{self.name} | [Website_link]({self.website}) | {self.domain} | {self.email} | {self.address} '''
            f.write(data) 
