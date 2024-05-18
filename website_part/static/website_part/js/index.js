const navlinks = document.querySelectorAll(".navbar-nav .nav-item .nav-link");
navlinks.forEach((navlink) => {
    navlink.addEventListener('click', function () {
        navlinks.forEach((item) => {
            item.classList.remove('active')
        });
        navlink.classList.add('active')
    });
});

/**
 * Permet d'ajouter la classe ".scrolled" a <nav>
 * lorsqu'on defile la page
 */
const nav = document.querySelector('nav');

window.addEventListener('scroll', function () {
    if (window.scrollY > 50){
        // La navbar change de couleur
        nav.classList.add('scrolled');
    } else {
        // La navbar devient transparente
        nav.classList.remove('scrolled');
    }
});

/**
 * Lorsque l'user est dans la section '.donation'
 * l'evenement est déclenchée pour le bouton '.shake'
 */
document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll(".donation");

    const options = {
        threshold: 0.5 // Déclencher l'observation lorsque 50% de l'élément est visible
    };

    const observer = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Démarrer l'événement lorsque l'utilisateur entre dans la section
                startEvent(entry.target.querySelector(".shake"));
            } else {
                // Arrêter l'événement lorsque l'utilisateur quitte la section
                stopEvent(entry.target.querySelector(".shake"));
            }
        });
    }, options);

    sections.forEach(section => {
        observer.observe(section);
    });

    function startEvent(element) {

        // Déclencher l'événement toutes les 2 secondes
        element.interval = setInterval(function() {
            element.classList.toggle("animate__animated");
            element.classList.toggle("animate__shakeX");
        }, 2000);
    }

    function stopEvent(element) {
        element.classList.remove("animate__animated", "animate__shakeX");
        
        // Arrêter l'intervalle de l'événement
        clearInterval(element.interval);
    }
});


/** 
 * Animation pour nos-actions 
 * Lorsqu'on clique sur les boutons
 */
document.addEventListener("DOMContentLoaded", function() {
    const slides = document.querySelectorAll(".slide");
    let currentIndex = 0;
    let transitioning = false;

    function showSlide(index, direction) {
        if (transitioning) return; 
        transitioning = true;

        const currentSlide = slides[currentIndex];
        const nextSlide = slides[index];

        currentSlide.classList.remove("active", "animate__animated");
        nextSlide.classList.remove("animate__animated");

        let currentAnimationClass, nextAnimationClass;

        if (direction === "next") {
            currentAnimationClass = "animate__fadeInRight";
            nextAnimationClass = "animate__fadeInRight";
        } else {
            currentAnimationClass = "animate__fadeInLeft";
            nextAnimationClass = "animate__fadeInLeft";
        }

        currentSlide.classList.add("animate__animated", currentAnimationClass);
        nextSlide.classList.add("active", "animate__animated", nextAnimationClass);

        setTimeout(function() {
            currentSlide.classList.remove("animate__animated", currentAnimationClass);
            nextSlide.classList.remove(nextAnimationClass);
            transitioning = false;
        }, 500);

        currentIndex = index;
    }

    document.getElementById("nextBtn").addEventListener("click", function() {
        let nextIndex = currentIndex + 1;
        if (nextIndex >= slides.length) {
            nextIndex = 0;
        }
        showSlide(nextIndex, "next");
    });

    document.getElementById("prevBtn").addEventListener("click", function() {
        let prevIndex = currentIndex - 1;
        if (prevIndex < 0) {
            prevIndex = slides.length - 1;
        }
        showSlide(prevIndex, "prev");
    });

    slides[currentIndex].classList.add("active");
});


// Code qui permet de vérifier les champs lors de l'envoie
(() => {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
      form.classList.add('was-validated');
    }, false);
  })
})();

// Code pour le Tab au niveau du choix de la donation
document.addEventListener("DOMContentLoaded", function(){
    var tabList = [].slice.call(document.querySelectorAll("#donationTabs a"));

    tabList.forEach(function(tab){
        var tabTrigger = new bootstrap.Tab(tab);

        tab.addEventListener("click", function(event){
            event.preventDefault();
            tabTrigger.show();
        });
    });
});

const payemntMethods = document.querySelector('.payment-method input[type="radio"]');

// Exécution du bouton '#scroll-btn'
const scrollToTopButton = document.querySelector('#scroll-btn');

document.addEventListener("DOMContentLoaded", function(){
    scrollToTopButton.style.display = "none";
});

window.addEventListener('scroll', function () {
    if (window.scrollY > 50){
        scrollToTopButton.style.display = "block";
    } else {
        scrollToTopButton.style.display = "none";
    }
});

function scrollToTopFunction() {
    document.body.scrollTop = 0; // pour safari
    document.documentElement.scrollTop = 0; // pour chrome
}

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
// const typeUtilisateurSelect = document.getElementById('type_utilisateur');
// const typeCompteSelect = document.getElementById('type_compte');
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
