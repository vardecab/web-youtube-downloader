document.addEventListener('DOMContentLoaded', () => { // run this when page is loaded
    // define 
    const musicCheckbox = document.getElementById('musicCheckbox');
    const videoCheckbox = document.getElementById('videoCheckbox');
    const submitButton = document.getElementById("submitButton");

    // see which checkbox is ticked
    musicCheckbox.addEventListener('change', () => {
        if (musicCheckbox.checked) {
            videoCheckbox.checked = false;
        }
    });

    videoCheckbox.addEventListener('change', () => {
        if (videoCheckbox.checked) {
            musicCheckbox.checked = false;
        }
    });

    // make sure checkbox is ticked before submitting the form so we know if user wants music or video
    function validateCheckboxes() {
        // define
        const musicChecked = document.querySelector('#musicCheckbox').checked;
        const videoChecked = document.querySelector('#videoCheckbox').checked;
        const submitButton = document.querySelector('button[type=submit]');

        if (!musicChecked && !videoChecked) {
            submitButton.disabled = true;
        } else {
            submitButton.disabled = false;
        }
    }

    validateCheckboxes();

    const checkboxes = document.querySelectorAll('input[type=checkbox]');

    for (const checkbox of checkboxes) {
        checkbox.addEventListener('change', validateCheckboxes);
    }
});