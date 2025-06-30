// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Handle header scroll effect and active navigation link
const header = document.querySelector('header');
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
    // Add/remove scrolled class to header
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }

    // Highlight active navigation link
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (pageYOffset >= sectionTop - 60) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').includes(current)) {
            link.classList.add('active');
        }
    });
});

// Client-side form validation
const contactForm = document.getElementById('contact-form');
contactForm.addEventListener('submit', function(e) {
    const name = document.getElementById('id_name').value.trim();
    const email = document.getElementById('id_email').value.trim();
    const message = document.getElementById('id_message').value.trim();
    let errors = [];

    if (name === '') {
        errors.push('Name is required.');
    }
    if (email === '') {
        errors.push('Email is required.');
    } else if (!/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email)) {
        errors.push('Invalid email format.');
    }
    if (message === '') {
        errors.push('Message is required.');
    }

    if (errors.length > 0) {
        e.preventDefault();
        const errorDiv = document.querySelector('.form-errors ul');
        if (errorDiv) {
            errorDiv.innerHTML = '';
            errors.forEach(error => {
                const li = document.createElement('li');
                li.textContent = error;
                errorDiv.appendChild(li);
            });
        } else {
            const errorContainer = document.createElement('div');
            errorContainer.className = 'form-errors';
            const ul = document.createElement('ul');
            errors.forEach(error => {
                const li = document.createElement('li');
                li.textContent = error;
                ul.appendChild(li);
            });
            errorContainer.appendChild(ul);
            contactForm.prepend(errorContainer);
        }
    }
});

// Section-based Scroll Progress Indicator
(function() {
    console.log('Scroll progress script loaded');
    const progressBar = document.getElementById('progress-bar');
    const progressContainer = document.getElementById('progress-container');
    
    console.log('Progress bar element:', progressBar);
    console.log('Progress container element:', progressContainer);
    
    function updateProgressBar() {
        if (!progressBar) {
            console.log('Progress bar not found!');
            return;
        }
        
        const scrollY = window.scrollY || window.pageYOffset;
        const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
        
        // Simple overall scroll progress
        const progress = scrollY / totalHeight;
        
        // Change color based on scroll position
        let color = '#4ADE80'; // green
        if (progress > 0.33) color = '#3B82F6'; // blue
        if (progress > 0.66) color = '#FBBF24'; // amber
        
        progressBar.style.height = (progress * 100) + '%';
        progressBar.style.background = color;
        
        console.log('Progress:', progress, 'Height:', (progress * 100) + '%', 'Color:', color);
    }

    // Initialize on page load
    document.addEventListener('DOMContentLoaded', function() {
        console.log('DOM loaded, initializing progress bar');
        updateProgressBar();
        window.addEventListener('scroll', updateProgressBar);
        window.addEventListener('resize', updateProgressBar);
    });
})();
