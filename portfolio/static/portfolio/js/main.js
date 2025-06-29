// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Highlight active navigation link on scroll
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
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
