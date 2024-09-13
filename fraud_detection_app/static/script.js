// Simple form validation
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', function (e) {
        const amount = document.getElementById('amount').value;
        const gender = document.getElementById('gender').value;
        const age = document.getElementById('age').value;
        const isInternational = document.getElementById('isInternational').value;

        // Basic validation
        if (!amount || !gender || !age || !isInternational) {
            e.preventDefault(); // Prevent form submission
            alert('All fields are required!');
        } else {
            // Show a loading spinner or a success message
            document.querySelector('button[type="submit"]').innerHTML = 'Checking...';
            document.querySelector('button[type="submit"]').disabled = true;
        }
    });
});

// Add some simple animation effects
document.addEventListener('DOMContentLoaded', function () {
    const formElements = document.querySelectorAll('.form-control, .form-select');
    
    formElements.forEach((element) => {
        element.addEventListener('focus', function () {
            this.style.transition = 'all 0.3s ease';
            this.style.boxShadow = '0 0 10px rgba(0, 123, 255, 0.7)';
        });

        element.addEventListener('blur', function () {
            this.style.boxShadow = 'none';
        });
    });
});
