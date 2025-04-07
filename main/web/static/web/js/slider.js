let currentSlide = 0;
const slides = document.querySelectorAll(".slide");

function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.toggle("active", i === index);
  });
}

function nextSlide() {
  currentSlide = (currentSlide + 1) % slides.length;
  showSlide(currentSlide);
}

function prevSlide() {
  currentSlide = (currentSlide - 1 + slides.length) % slides.length;
  showSlide(currentSlide);
}

// Otomatik geçiş
let interval = setInterval(nextSlide, 2000); // 5 saniyede bir geçiş

// (İsteğe bağlı) Fareyle üzerine gelince durdur
const slider = document.querySelector('.slider');
slider.addEventListener('mouseenter', () => clearInterval(interval));
slider.addEventListener('mouseleave', () => {
  interval = setInterval(nextSlide, 5000);
});

// Başlangıç slaytı
showSlide(currentSlide);
