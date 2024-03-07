class TimLab:
    people = []
    funding_per_year = []
    years_needed = []
    status = 'unfunded'

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
        else:
            raise Exception(f"Unknown funding source: {fund}")
            print("New pull request 2")

print("Fetch isn't going to happen.")

aol = TimLab()
aol.add_student("Bing", 30, 1)

print(aol.total_cost())
aol.funding("NSERC", 123456)
print(aol.status)
