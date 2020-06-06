import pandas
import requests

from bs4 import BeautifulSoup 

#Getting the webpage 
webpage = requests.get("https://www.mygov.in/corona-data/covid19-statewise-status/")

#Loading the content 
content = webpage.content

#Parsing the content
result = BeautifulSoup(content,'html.parser')

#Identifying the products on the page by the div tag and the class name 
covid19StatesAffected = result.find_all("div", {"class": "field field-name-field-select-state field-type-list-text field-label-above"})
covid19totalConfirmed = result.find_all("div", {"class": "field field-name-field-total-confirmed-indians field-type-number-integer field-label-above"})
covid19curedDischarged = result.find_all("div", {"class":"field field-name-field-cured field-type-number-integer field-label-above"})
covid19totalDeath = result.find_all("div", {"class":"field field-name-field-deaths field-type-number-integer field-label-above"})
covid19epassLink = result.find_all("div", {"class": "field field-name-field-e-pass-url field-type-text field-label-above"})
state_Name =[] 
total_confirmed = []
total_cured_discharged_migrated = []
total_death =[]
e_pass = []
#Iterating over the list of products and extracting the necessary info
for item in covid19StatesAffected:
    stateName = item.find("div", { "class" : "field-items"}).string
    state_Name.append(stateName)

for item in covid19totalConfirmed : 
    totalConfirmed = item.find("div", { "class" : "field-items"}).string
    total_confirmed.append(totalConfirmed)

for item in covid19curedDischarged :
    totalDischarged = item.find("div", {"class" : "field-items"}).string
    total_cured_discharged_migrated.append(totalDischarged)

for item in covid19totalDeath :
    totalDeath = item.find("div", {"class" : "field-items"}).string
    total_death.append(totalDeath)

for item in covid19epassLink : 
    epass =   item.find("div", {"class" : "field-items"}).string
    e_pass.append(epass);

data = list(zip(state_Name,total_confirmed,total_cured_discharged_migrated, total_death,e_pass))

#creating the pandas dataframe

d= pandas.DataFrame(data, columns= ["State Name", "Total Confirmed", "Cured/ Discharged/ Migrated", "Death", "E-Pass Links"])

# Writing the data frame to a new Excel File 
try: 
    d.to_excel("Covid19IndiaData.xlsx")
except:
    print("\nSomething went wrong ! Please check code / Internet Connection")
else:
    print("\ncovid data successfully written to Excel.")
finally:
    print("\nQuitting the program. Bye !")

#End of program

























