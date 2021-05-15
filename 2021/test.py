import pandas
import urllib.request as r
from bs4 import BeautifulSoup as bs
import json

me=[
    { "jour":23,
      "NbTest":424,
      "NbNvCas":424,
      "NbCmCas":424,
      "NbCcas":424,
      "NbGueris":424,
      "NomFichier":"covidtest1",
      "DateHeureExtraction":"date",
      "Localite":[
        {
          "NomLocalite":"Dakar",
          "NbCas":12
        },
        {
          "NomLocalite":"Thies",
          "NbCas":12
        },
        {
          "NomLocalite":"Touba",
          "NbCas":12
        }
      ]
    } ,
        { "jour":22,
          "NbTest":424,
          "NbNvCas":424,
          "NbCmCas":424,
          "NbCcas":424,
          "NbGueris":424,
          "NomFichier":"covidtest1",
          "DateHeureExtraction":"date",
          "Localite":[
            {
              "NomLocalite":"Dakar",
              "NbCas":12
            },
            {
              "NomLocalite":"Thies",
              "NbCas":12
            },
            {
              "NomLocalite":"Touba",
              "NbCas":12
            }
          ]
        } 
]
print(me[0]["Localite"][1]["NomLocalite"])
url = "https://github.com/Ar-Babacar/Covid-Modeler-Api/blob/main/2021_03.json"
df = pandas.read_json(url)
df.head()

url = r.urlopen(url)
content = url.read()
soup = bs(content)
newDictionary=json.loads(str(soup))