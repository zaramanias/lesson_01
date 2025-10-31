from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+7945678901"),
    Smartphone("Samsung", "Galaxy S21", "+79876543212"),
    Smartphone("Google", "Pixel 6", "+79223344550")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
