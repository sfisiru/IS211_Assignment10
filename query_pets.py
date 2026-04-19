import sqlite3

conn = sqlite3.connect('pets.db')
cursor = conn.cursor()
 
while True:
    user_input = input("Enter a person's ID (or -1 to exit): ")
    person_id = int(user_input)
 
    if person_id == -1:
        break
 
    cursor.execute("SELECT * FROM person WHERE id = ?", (person_id,))
    person = cursor.fetchone()
 
    if person is None:
        print("No person found with that ID.")
    else:
        first_name = person[1]
        last_name = person[2]
        age = person[3]
        print(first_name + " " + last_name + ", " + str(age) + " years old")
 
        cursor.execute("""
            SELECT pet.name, pet.breed, pet.age
            FROM pet
            JOIN person_pet ON pet.id = person_pet.pet_id
            WHERE person_pet.person_id = ?
        """, (person_id,))
        pets = cursor.fetchall()
 
        for pet in pets:
            print(first_name + " " + last_name + " owned " + pet[0] + ", a " + pet[1] + ", that was " + str(pet[2]) + " years old")
 
conn.close()

if __name__ == "__main__":
    print("Running query_pets.py")
