document.addEventListener('DOMContentLoaded', () => {
    const mapButton = document.getElementById('mapButton');
    const cardsButton = document.getElementById('cardsButton');
    const content = document.getElementById('content');

    mapButton.addEventListener('click', () => {
        fetch('/map')
            .then(response => response.json())
            .then(data => {
                content.innerHTML = data.map_html;
            })
            .catch(error => console.error('Error fetching map:', error));
    });

    cardsButton.addEventListener('click', () => {
        content.innerHTML = '<h1>Cards Feature</h1>'; // Replace with actual card feature integration
    });

    // Initially show cards
    content.innerHTML = '<h1>Cards Feature</h1>'; // Replace with actual initial feature if needed
});
