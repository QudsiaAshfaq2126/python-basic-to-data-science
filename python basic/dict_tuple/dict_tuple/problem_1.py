population={
    "china":143,
    "india":136,
    "usa":32,
    "pakistan":21
}
def add():
    country=input("Enter the name of country")
    country=country.lower()
    if country in population:
        print("country already exist ")
        return
    pop=float(input("Enter your population:"))
    population[country]=pop
    print_all()
def remove():
    country=input("enter country name to remove:")
    country=country.lower()
    if country not in population:
        print("country doesnot exist in dataset:")
        return
    del population[country]
    print_all()
def query():
    country=input("enter the country name")
    country=country.lower()
    if country not in population:
        print("country doesnot exist in dataset:")
        return
    print("population of {country} is: {population[country]} corers")
def print_all():
    for country, pop in population.items():
        print(f"{country}==>{pop}")
def main():
    op=input("Enter operation(add,remove,query,print)") 
    if op.lower()=="add":
        add()
    elif op.lower()=="remove":
        remove()
    elif op.lower()=="query":
        query()
    elif op.lower()=="print":
        print_all()

    main()

           
       

    


