// Chargement des pays et des différentes villes par l'API "COUNTRYSTATECITY"
const config = {
    countries_url: 'https://api.countrystatecity.in/v1/countries',
    countries_key: 'bUgzVHc2aFpNTVh5eHRkaUF5T3drajJPRnR5d0RBVllUV2lyMTI3UQ=='
}

const paysSelect = document.querySelector('.pays');
const villeSelect = document.querySelector('.villes');

function chargerPays () {
    let resultatAPI = config.countries_url;

    fetch(resultatAPI, {
        headers: {
            'X-CSCAPI-KEY': config.countries_key
        }
    })
    .then(Response => Response.json())
    .then(data => {
        console.log(data);
        data.forEach(pays => {
            const option = document.createElement('option');
            option.value = pays.iso2;
            option.textContent = pays.name;
            paysSelect.appendChild(option);
        });
    })
    .catch(error => console.log('Erreur de chargement des pays : ', error))
}

function chargerVilles() {
    const codePaysSelectionne = paysSelect.value;
    villeSelect.innerHTML = '<option value="">Selectionner votre ville</option>';
    fetch(`${config.countries_url}/${codePaysSelectionne}/cities`, {
        headers: {
            'X-CSCAPI-KEY': config.countries_key
        }
    })
    .then(Response => Response.json())
    .then(data => {
        console.log(data);
        data.forEach(ville => {
            const option = document.createElement('option');
            option.value = ville.name;
            option.textContent = ville.name;
            villeSelect.appendChild(option);
        })
    })
    .catch(error => console.log('Erreur de chargement des villes du pays sélectionné : ', error))
}

window.onload = chargerPays
