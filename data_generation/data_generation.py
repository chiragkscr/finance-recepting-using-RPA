import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Generate synthetic data
data = []
for i in range(25000):  # Adjust the number of rows as needed
    data.append({
        "Receipt Number": fake.uuid4(),
        "Client Name": fake.name(),
        "Transaction Type": random.choice(["Card", "Cheque"]),
        "Vendor Email": fake.email(),
        "Client Email": fake.email(),
        "Amount": round(random.uniform(50.0, 5000.0), 2),
        "Date": fake.date_this_year()
    })

# Save to Excel
df = pd.DataFrame(data)
df.to_excel("synthetic_data.xlsx", index=False)
print("Synthetic data generated successfully!")
