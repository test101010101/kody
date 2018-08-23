import re

line = "Bieg na orientację dookoła miejskiego zoo."

m = re.findall(".oo", line, re.IGNORECASE)

print (m)
