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