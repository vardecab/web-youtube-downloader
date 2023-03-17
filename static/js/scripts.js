/* ---- check if checkbox ticked ---- */

document.addEventListener('DOMContentLoaded', () => { // run this when page is loaded

    // define 
    const musicCheckbox = document.getElementById('checkboxMusic');
    const videoCheckbox = document.getElementById('checkboxVideo');
    const submitButton = document.getElementById("buttonSubmit");

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
        const musicChecked = document.querySelector('#checkboxMusic').checked;
        const videoChecked = document.querySelector('#checkboxVideo').checked;
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

/* ------ check if YouTube URL ------ */

});

function validateForm() {
    const urlInput = document.getElementById('fieldURL');
    if (!urlInput.value || !urlInput.value.includes('youtube.com') && !urlInput.value.includes('youtu.be')) {
        alert('Please enter a valid YouTube video URL');
        return false;
    }

    return true;
}