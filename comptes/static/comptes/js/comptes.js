document.addEventListener('DOMContentLoaded', function () {
    // déclaration des variables pour les choix du type de compte 
    var type_utilisateur = document.getElementById('type_utilisateur');
    var type_compte = document.getElementById('type_compte');
    var type_utilisateur_value = "";
    var type_compte_value = "";

    // sélection des différentes zones de formulaires 
    const form_personne_donateur = document.getElementById('form-personne-donateur');
    const form_personne_necessiteux = document.getElementById('form-personne-necessiteux');
    const form_personne_benevole = document.getElementById('form-personne-benevole');
    const form_organisation_donateur = document.getElementById('form-organisation-donateur');
    const form_organisation_necessiteux = document.getElementById('form-organisation-necessiteux');
    const form_entreprise_donateur = document.getElementById('form-entreprise-donateur');

    var forms = [form_personne_donateur, 
        form_personne_necessiteux, 
        form_personne_benevole, 
        form_organisation_donateur,
        form_organisation_necessiteux,
        form_entreprise_donateur];

    // fonction de gestion de l'affichage
    function affichageFormulaire() {
        type_utilisateur_value = type_utilisateur.value;
        type_compte_value = type_compte.value;

        forms.forEach((form) => {
            form.style.display = none;
        });

        // type utilisateur : 'personne', 'organisation', 'entreprise'
        // type compte : 'donateur', 'necessiteux', 'benevole'
        switch (type_utilisateur_value) {
            case "personne":
                switch (type_compte_value) {
                    case "donateur":
                        // personne-donateur
                        form_personne_donateur.style.display = 'block';
                        break;
                    case "necessiteux":
                        // personne-necessiteux
                        form_personne_necessiteux.style.display = 'block';
                        break;
                    case "benevole":
                        // personne-benevole
                        form_personne_benevole.style.display = 'block';
                        break;
                    default:
                        break;
                }
                break;
            case "organisation":
                switch (type_compte_value) {
                    case "donateur":
                        // organisation-donateur
                        form_organisation_donateur.style.display = 'block';
                        break;
                    case "necessiteux":
                        // organisation-necessiteux
                        form_organisation_necessiteux.style.display = 'block';
                        break;
                    default:
                        break;
                }
                break;
            case "entreprise":
                switch (type_compte_value) {
                    case "donateur":
                        // entreprise-donateur
                        form_entreprise_donateur.style.display = 'block';
                        break;
                    default:
                        break;
                }
                break;
            default:
                break;
        }
    }

    type_utilisateur.addEventListener('change', affichageFormulaire);
    type_compte.addEventListener('change', affichageFormulaire);

    // initialisation du formulaire lors du chargement de la page
    affichageFormulaire();
});


/*
document.addEventListener('DOMContentLoaded', function() {
  const typeCompteSelect = document.getElementById('type_compte');
  const roleSelect = document.getElementById('role');
  const personneForm = document.getElementById('formulaire-personne');
  const organisationForm = document.getElementById('formulaire-organisation');
  const entrepriseForm = document.getElementById('formulaire-entreprise');

  function updateFormVisibility() {
    const selectedTypeCompte = typeCompteSelect.value;
    const selectedRole = roleSelect.value;

    // Masquer tous les formulaires par défaut
    personneForm.style.display = 'none';
    organisationForm.style.display = 'none';
    entrepriseForm.style.display = 'none';

    // Afficher le formulaire correspondant au type de compte sélectionné
    if (selectedTypeCompte === 'personne') {
      personneForm.style.display = 'block';
    } else if (selectedTypeCompte === 'organisation') {
      organisationForm.style.display = 'block';
    } else if (selectedTypeCompte === 'entreprise') {
      entrepriseForm.style.display = 'block';
    }

    // Afficher/masquer les champs spécifiques au rôle sélectionné
    // ...
  }

  typeCompteSelect.addEventListener('change', updateFormVisibility);
  roleSelect.addEventListener('change', updateFormVisibility);

  // Initialiser l'affichage des formulaires au chargement de la page
  updateFormVisibility();
});
*/

// Initialiser Filepond : EXPLICATION
const inputElement = document.querySelector('input[type="file"]');
FilePond.create(inputElement);

/*
function creationCompteTraitement() {
    const type_utilisateur = document.getElementById('type_utilisateur');
    const type_compte = document.getElementById('type_compte');

    type_utilisateur.addEventListener("change", function() {
        var type_utilisateur_value = type_utilisateur.value;
        console.log("Option proprio sélectionnée:", type_utilisateur_value);
        // Ajoutez ici le code que vous souhaitez exécuter lorsque l'option est sélectionnée
    });

    type_compte.addEventListener("change", function() {
        var type_compte_value = type_compte.value;
        console.log("Option type sélectionnée:", type_compte_value);
        // Ajoutez ici le code que vous souhaitez exécuter lorsque l'option est sélectionnée
    });

    var message = "Type de compte sélectionné: " + accountType + "\n";
    message += "Rôle d'utilisateur sélectionné: " + userRole;

    alert(message);
}
*/
