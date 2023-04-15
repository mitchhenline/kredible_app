document.addEventListener("DOMContentLoaded", function() {
    
    const advocateRows = document.querySelectorAll('.adv-row');

    advocateRows.forEach(row => {
        row.addEventListener('click', () => {
            const advocateId = row.dataset.advocateId;
            // Make an AJAX request to your Flask server to retrieve advocate info
            const xhr = new XMLHttpRequest();
            xhr.open('GET', `/advocates/${advocateId}`);
            xhr.onload = () => {
                if (xhr.status === 200) {
                    const advocate = JSON.parse(xhr.responseText);
                    displayAdvocateInfo(advocate);
                } else {
                    console.error('Error:', xhr.statusText);
                }
            };
            xhr.onerror = () => {
                console.error('Error:', xhr.statusText);
            };
            xhr.send();
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

