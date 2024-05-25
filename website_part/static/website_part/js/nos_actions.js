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
