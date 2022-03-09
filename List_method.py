# countryList = ["Bangladesh", "UK", "Germany", "India", "Scotland"]
# countryList.append("Italy")
# print(countryList)
#
# countryList.extend(["Bhutan", "Nepal", "Bharma", "SriLanka"])
# print(countryList)
# countryList.insert(7, "Neatherland")
# print(countryList)
# countryList.remove("Bharma")
# print(countryList)
# country = countryList.pop(4)
# print(country)
# print(countryList)
# countryList.clear()
# print(countryList)


countryList = ["Bangladesh", "UK", "Germany", "India", "Scotland","Malysia","Nigeria","Nohakhali","USA","Zimbabwe","Russia"]

countryList.sort()
print(countryList)
countryList.reverse()
print(countryList)

countryList.sort(key=str.lower,reverse=False)
print(countryList)