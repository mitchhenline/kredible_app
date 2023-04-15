document.addEventListener("DOMContentLoaded", function() {
    
    const advocateRows = document.querySelectorAll('.adv-row');

    advocateRows.forEach(row => {
        row.addEventListener('click', () => {
            const advocateId = row.dataset.advocateId;
            // Make an AJAX request to your Flask server to retrieve advocate info
            // Once the info is retrieved, call a function to display it in the pop-up modal
        });
    });

    function displayAdvocateInfo(advocate) {
        const modal = document.getElementById('advocate-modal');
        // Update the modal's HTML with the advocate's info
        modal.innerHTML = `
            <h2>${advocate.name}</h2>
            <p>${advocate.email}</p>
            <p>${advocate.company}</p>
            <!-- Add more advocate info here -->
        `;
        modal.style.display = 'block';
    }

    const modalCloseBtn = document.getElementById('modal-close-btn');
    const modalOverlay = document.getElementById('modal-overlay');
    const modal = document.getElementById('advocate-modal');

    modalCloseBtn.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    modalOverlay.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    window.addEventListener('click', (event) => {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });

});
