import requests

URL = "https://www.sap.com/belgique/index.html"

r = requests.get(URL)

sap_html = open("sap.html", "wb")

sap_html.write(r.content)

with open("sap.html", "r") as f:
    with open("newSap.html", "w") as s:
        for line in f:
            s.write(line.replace("SAP", "Odoo"))
