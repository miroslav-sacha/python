# list 
employees = ["David", "Harry", "Ron"]
print(employees[0])
print(employees[1])
print(employees[2])

# meni polozku
employees[1] = "Hermiona"
print(employees)

# pridani polozky nakonec jako posledni polozku
employees.append("Harry")
print(employees)

# pridavani vice polozek
employees.extend(["Crabe, Goyle"])
print(employees)

# odstraneni polozky
employees.remove("Ron")
print(employees)