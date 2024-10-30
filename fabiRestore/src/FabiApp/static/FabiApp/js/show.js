document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('.mado_image');
    const lightbox = document.getElementById('lightbox');
    const lightboxImage = document.querySelector('.lightbox-image');
    const closeBtn = document.querySelector('.close');
    const lightboxTitle = document.querySelector('.lightbox-title');
    const lightboxCounter = document.querySelector('.lightbox-counter');
    let currentIndex = 0;

    images.forEach((image, index) => {
        image.addEventListener('click', function() {
            currentIndex = index;
            lightbox.style.display = 'block';
            lightboxImage.src = image.src;
            lightboxTitle.textContent = document.querySelector('.meuble_partie_haute h1').textContent;
            updateCounter();
        });
    });

    closeBtn.addEventListener('click', function() {
        lightbox.style.display = 'none';
    });

    window.plusSlides = function(n) {
        currentIndex += n;
        if (currentIndex >= images.length) {
            currentIndex = 0;
        } else if (currentIndex < 0) {
            currentIndex = images.length - 1;
        }
        lightboxImage.src = images[currentIndex].src;
        updateCounter();
    };

    function updateCounter() {
        lightboxCounter.textContent = `${currentIndex + 1}/${images.length}`;
    }
});