class TimLab:
    people = []
    funding_per_year = []
    years_needed = []
    status = 'unfunded'

    def __init__(self, year):
        self.year = year
    
    def add_student(self, name, funding, years):
        self.people.append(name)
        self.funding_per_year.append(funding)
        self.years_needed.append(years)

    def total_cost(self):
        total = sum(funding * years for funding, years in zip(self.funding_per_year, self.years_needed))
        return total

    def funding(self, fund, account_number):
        if fund == 'NSERC':
            print("NSERC funding.")
            print(f"Account number: {account_number}")
            self.status = "funded"
        elif fund == "CIHR":
            print("CIHR funding.")
            print(f"Account number: {account_number}")
            self.status = "funded"
        elif fund == "None":
            print("No funding available.")
            self.status == "not funded"
        else:
            raise Exception(f"Unknown funding source: {fund}")


aol2024 = TimLab(2024)
aol2024.add_student("Bing", 30, 1)
aol2024.add_student("Jesse", 30, 0)
aol2024.add_student("Jamal", 30, 3)

print(aol2024.total_cost())
aol2024.funding("NSERC", 123456)
print(aol2024.status)
