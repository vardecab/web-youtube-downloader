/* ---- check if radio selected ---- */

document.addEventListener('DOMContentLoaded', () => { // run this when page is loaded

    // define 
    const radioMusic = document.getElementById('radioMusic');
    const radioVideo = document.getElementById('radioVideo');
    const submitButton = document.getElementById("buttonSubmit");

    // see which radio is selected
    radioMusic.addEventListener('change', () => {
        if (radioMusic.checked) {
            radioVideo.checked = false;
        }
    });

    radioVideo.addEventListener('change', () => {
        if (radioVideo.checked) {
            radioMusic.checked = false;
        }
    });

    // make sure radio is selected before submitting the form so we know if user wants music or video
    function validateCheckboxes() {
        // define
        const musicChecked = document.querySelector('#radioMusic').checked;
        const videoChecked = document.querySelector('#radioVideo').checked;
        const submitButton = document.querySelector('button[type=submit]');

        if (!musicChecked && !videoChecked) {
            submitButton.disabled = true;
        } else {
            submitButton.disabled = false;
        }
    }

    validateCheckboxes();

    const radios = document.querySelectorAll('input[type=radio]');

    for (const radio of radios) {
        radio.addEventListener('change', validateCheckboxes);
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