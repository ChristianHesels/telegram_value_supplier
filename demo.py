### Script to let the Bot reply 'This is a test' to a /get request
from value_supplier_bot import ValueSupplier
inp = ""

supplier = ValueSupplier()

supplier.set_value("This is a test")

while inp != "stop":
    inp = input("Write 'stop' to stop bot from supplying: ")

supplier.shutdown()
