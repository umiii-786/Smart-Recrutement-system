function switchForm(role) {
    const slider = document.getElementById('slider');
    const candidateForm = document.getElementById('candidate-form');
    const companyForm = document.getElementById('company-form');
    const options = document.querySelectorAll('.toggle-option');

    if (role === 'candidate') {
        slider.style.transform = 'translateX(0)';
        candidateForm.classList.add('active');
        companyForm.classList.remove('active');
        options[0].classList.add('text-white');
        options[0].classList.remove('text-gray-400');
        options[1].classList.add('text-gray-400');
        options[1].classList.remove('text-white');
    } else {
        slider.style.transform = 'translateX(100%)';
        companyForm.classList.add('active');
        candidateForm.classList.remove('active');
        options[1].classList.add('text-white');
        options[1].classList.remove('text-gray-400');
        options[0].classList.add('text-gray-400');
        options[0].classList.remove('text-white');
    }
}