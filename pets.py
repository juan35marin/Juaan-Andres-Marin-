pets = []

def add_pet(name, species, age):
    pet = {
        'name': name,
        'species': species.lower(),
        'age': age
    }
    pets.append(pet)

def search_by_species(species):
    species = species.lower()
    return [p for p in pets if p['species'] == species]

def filter_by_age(min_age=None, max_age=None):
    result = pets
    if min_age is not None:
        result = [p for p in result if p['age'] >= min_age]
    if max_age is not None:
        result = [p for p in result if p['age'] <= max_age]
    return result

def show_pets(pet_list):
    if not pet_list:
        print("No pets found.")
    for p in pet_list:
        print(f"Name: {p['name']}, Species: {p['species']}, Age: {p['age']}")

def menu():
    while True:
        print("\n--- Pet Adoption Center ---")
        print("1. Add a pet")
        print("2. Search pets by species")
        print("3. Filter pets by age")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Name: ")
            species = input("Species: ")
            try:
                age = int(input("Age: "))
            except ValueError:
                print("Invalid age. Please try again.")
                continue
            add_pet(name, species, age)
            print("Pet added.")
        
        elif choice == '2':
            species = input("Species to search: ")
            result = search_by_species(species)
            show_pets(result)

        elif choice == '3':
            try:
                min_age = input("Minimum age (leave empty for no minimum): ")
                min_age = int(min_age) if min_age else None
                max_age = input("Maximum age (leave empty for no maximum): ")
                max_age = int(max_age) if max_age else None
            except ValueError:
                print("Invalid age. Please try again.")
                continue
            result = filter_by_age(min_age, max_age)
            show_pets(result)

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

menu()