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
// Section indicator elements
const indicatorItems = document.querySelectorAll('.indicator-item');
const movingBar = document.getElementById('moving-bar');

// Update indicator for given section ID
function updateIndicator(current) {
    const activeItem = document.querySelector(`.indicator-item[data-target="${current}"]`);
    indicatorItems.forEach(item => item.classList.remove('active'));
    if (activeItem) {
        activeItem.classList.add('active');
        const itemTop = activeItem.offsetTop;
        const itemHeight = activeItem.offsetHeight;
        movingBar.style.top = `${itemTop}px`;
        movingBar.style.height = `${itemHeight}px`;
    }
}

// Observe sections entering view
const observerOptions = { root: null, rootMargin: '0px', threshold: 0.5 };
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            updateIndicator(entry.target.id);
        }
    });
}, observerOptions);
sections.forEach(section => observer.observe(section));

window.addEventListener('scroll', () => {
    if (header) {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
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

    // Update indicator via scroll fallback
    updateIndicator(current);
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

// Set dynamic build date in footer
window.addEventListener('DOMContentLoaded', () => {
    const dateEl = document.getElementById('build-date');
    if (dateEl) {
        const now = new Date();
        dateEl.textContent = now.toDateString();
    }
});
