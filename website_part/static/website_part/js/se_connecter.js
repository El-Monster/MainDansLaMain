/* Choix du compte dans le modal
*******************************/
const typeUtilisateurSelect = document.getElementById('type_utilisateur');
const typeCompteSelect = document.getElementById('type_compte');

typeUtilisateurSelect.addEventListener('change', updateCompteOptions);

typeUtilisateurSelect.addEventListener('change', function() {
    const erreur_utilisateur = document.getElementById('erreur_utilisateur');
    erreur_utilisateur.style.display = 'none'; // Masquer le message d'erreur
});

typeCompteSelect.addEventListener('change', function() {
    const erreur_compte = document.getElementById('erreur_compte');
    erreur_compte.style.display = 'none'; // Masquer le message d'erreur
});

function updateCompteOptions() {
    const selectedUtilisateur = typeUtilisateurSelect.value;
    const compteOptions = typeCompteSelect.options;

    // Vider les options existantes
    compteOptions.length = 0;

    // Ajouter l'option "Choisissez..."
    const defaultOption = document.createElement('option');
    defaultOption.value = '';
    defaultOption.text = 'Choisissez...';
    compteOptions.add(defaultOption);

    // Ajouter des options en fonction du type d'utilisateur sélectionné
    if (selectedUtilisateur === 'personne') {
        addCompteOption('donateur');
        addCompteOption('necessiteux');
        addCompteOption('benevole');
    } else if (selectedUtilisateur === 'organisation') {
        addCompteOption('donateur');
        addCompteOption('necessiteux');
    } else if (selectedUtilisateur === 'entreprise') {
        addCompteOption('donateur');
    }

    const erreur_utilisateur = document.getElementById('erreur-choix');
    erreur_utilisateur.style.display = 'none'; // Masquer le message d'erreur
}

function addCompteOption(compteValue) {
    const compteOption = document.createElement('option');
    compteOption.value = compteValue;
    compteOption.text = compteValue.charAt(0).toUpperCase() + compteValue.slice(1);
    typeCompteSelect.options.add(compteOption);
}

/* Traitement et soumission du formulaire
******************************************/
const submitButton = document.getElementById('btn_modal_inscription');

function verifierChoixEtGenererUrl() {
    const selectedUtilisateur = typeUtilisateurSelect.value;
    const selectedCompte = typeCompteSelect.value;

    const erreur_utilisateur = document.getElementById('erreur_utilisateur');
    const erreur_compte = document.getElementById('erreur_compte');

    if (selectedUtilisateur === '' || selectedCompte === '') {
        if (selectedUtilisateur === '') {
            erreur_utilisateur.textContent = 'Veuillez sélectionner le type d\'entité.';
            erreur_utilisateur.style.display = 'block';
        }
        if (selectedCompte === '') {
            erreur_compte.textContent = 'Veuillez sélectionner le type de compte.';
            erreur_compte.style.display = 'block';
        }
        return;
    }
}

submitButton.addEventListener('click', verifierChoixEtGenererUrl);

/*
    Affichage du bouton en fonction des choix
*/
const boutonsContinuer = document.querySelectorAll('.creation');
const boutonInscriptionModal = document.getElementById('btn_modal_inscription');

typeUtilisateurSelect.addEventListener('change', () => {
  afficherBoutonsContinuer();
});

typeCompteSelect.addEventListener('change', () => {
  afficherBoutonsContinuer();
});

function afficherBoutonsContinuer() {
  const typeUtilisateur = typeUtilisateurSelect.value;
  const typeCompte = typeCompteSelect.value;

  boutonsContinuer.forEach(bouton => {
    const boutonId = bouton.id;
    const type_compte_selected = boutonId.split('-')[0]; // Exemple : "donateur-personne" -> "donateur"
    const type_utilisateur_selected = boutonId.split('-')[1]; // Exemple : "donateur-personne" -> "personne"

    if (type_compte_selected === typeCompte && type_utilisateur_selected === typeUtilisateur) {
      bouton.classList.remove('d-none'); // Afficher le bouton
      bouton.disabled = false; // Activer le bouton
    } else {
      bouton.classList.add('d-none'); // Masquer le bouton
      bouton.disabled = true; // Désactiver le bouton
    }
  });

  // Gérer le bouton sans lien (inscription modale)
  if (typeCompte === '' || typeUtilisateur === '') {
    boutonInscriptionModal.classList.remove('d-none'); // Afficher le bouton modal
    boutonInscriptionModal.disabled = false; // Activer le bouton modal
  } else {
    boutonInscriptionModal.classList.add('d-none'); // Masquer le bouton modal
    boutonInscriptionModal.disabled = true; // Désactiver le bouton modal
  }
}

// Initialiser l'affichage des boutons au chargement de la page
afficherBoutonsContinuer();
