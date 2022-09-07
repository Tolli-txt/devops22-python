# Datatyper Extra Övning
# print(" ") Kommer användas vid olika tillfällen
# i syfte av mera enkel läsning i 'cmd'

X = 1
Y = 4

addresses = {
    "Adam":     "Ormvägen 5",
    "Bella":    "Klockvägen 1",
    "Cornelia": "Vikingagatan 3"
}
cars = ["Volvo", "Opel", "BMW"]
numbers1 = {1, 2, 3, X, 6}
numbers2 = {Y, 2, 4, 7}

# 1. X & Y är datatyp int/integer
# 2. addresses är datatyp 'set'

# 3
print(addresses["Bella"])

# 4. Svar: Daniel och hans adress läggs till i addresses 'set'
addresses["Daniel"] = "Prinsgränd 2"

print(" ")

# 5.
for key, value in addresses.items():
    print(key, value)

print(" ")

# 5.1
for key, value in sorted(addresses.items(), key=lambda x: x[0], reverse=True):
    print(value)
