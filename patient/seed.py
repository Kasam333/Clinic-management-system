import random
from datetime import timedelta, date
from faker import Faker
from .models import Patient  # Replace 'your_app' with the name of your app

# Initialize Faker
fake = Faker()

# Function to create fake data
def create_fake_patients(num_records=50):
    for _ in range(num_records):
        name = fake.name()
        age = random.randint(1, 100)
        gender = random.choice(['male', 'female', 'other'])
        mobile = random.randint(1000000000, 9999999999)  # Assuming a 10-digit mobile number
        address = fake.address()
        details = fake.text(max_nb_chars=200)
        medicine_detail = fake.text(max_nb_chars=100)
        note = fake.sentence()
        amount = round(random.uniform(50, 5000), 2)  # Random amount between 50 and 5000
        next_visit = random.randint(1, 30)  # Number of days until next visit
        visit_date = date.today() + timedelta(days=random.randint(-30, 30))  # Random past or future date

        # Create and save patient record
        Patient.objects.create(
            name=name,
            age=age,
            gender=gender,
            mobile=mobile,
            address=address,
            details=details,
            medicine_detail=medicine_detail,
            note=note,
            amount=amount,
            next_visit=next_visit,
            visit_date=visit_date,
        )

    print(f"{num_records} fake patient records created successfully.")

# Call the function
create_fake_patients(50)  # Create 50 fake records
