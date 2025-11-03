import requests

URL = "https://pax.ulaval.ca/quoridor/api/a25"

def créer_une_partie(idul, secret):
    try:
        réponse = requests.post(f"{URL}/jeux", auth=(idul, secret))
        if réponse.status_code == 200:
            informations = réponse.json()
            return informations['id'], informations['état']
        
        elif réponse.status_code == 401:
            raise PermissionError(réponse.json()['message'])
        
        elif réponse.status_code == 406:
            raise RuntimeError(réponse.json()['message'])
        
        else:
            raise ConnectionError()



def appliquer_un_coup(id_partie, coup, position, idul, secret):
    try:
        URL = f"{URL}/jeux/{id_partie}"
        informations = {'id': id_partie, 'type': type_coup, 'pos': position}
        réponse = requests.put(URL, json=informations, auth=(idul, secret))
     
        if réponse.status_code == 200:
            informations = réponse.json()
            if informations.get('partie') == 'terminée':
                nom_du_gagnant = informations.get('gagnant')
                raise StopIteration(nom_du_gagnant)
            return informations['coup'], informations['position']
        
        elif réponse.status_code == 406:
            raise RuntimeError(réponse.json()['message']) 
      
        elif réponse.status_code == 401:
            raise PermissionError(réponse.json()['message'])
      
        elif réponse.status_code == 404:
            raise ReferenceError(réponse.json()['message'])
      
        else:
            raise ConnectionError()



def récupérer_une_partie(id_partie, idul, secret):
    try:
        réponse = requests.get(f"{URL}/jeux/{id_partie}", auth=(idul, secret))
        if réponse.status_code == 200:
            return réponse.json()['coup'], réponse.json()['état']
       
        elif réponse.status_code == 401:
             raise PermissionError(réponse.json()['message'])
        
        elif réponse.status_code == 404:
            raise ReferenceError(réponse.json()['message'])
        
        elif réponse.status_code == 406:
            raise RuntimeError(réponse.json()['message'])
        
        else:
            raise ConnectionError()