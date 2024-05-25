document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.card');
    let startX, currentCard;

    cards.forEach(card => {
        card.addEventListener('mousedown', (e) => {
            startX = e.clientX;
            currentCard = card;
            currentCard.style.transition = 'none';
        });

        card.addEventListener('mousemove', (e) => {
            if (currentCard) {
                let moveX = e.clientX - startX;
                currentCard.style.transform = `translateX(${moveX}px) rotate(${moveX / 20}deg)`;
            }
        });

        card.addEventListener('mouseup', (e) => {
            if (currentCard) {
                let moveX = e.clientX - startX;
                currentCard.style.transition = 'transform 0.3s, opacity 0.3s';

                if (Math.abs(moveX) > 150) {
                    currentCard.style.transform = `translateX(${moveX > 0 ? 1000 : -1000}px) rotate(${moveX / 20}deg)`;
                    setTimeout(() => {
                        currentCard.remove();
                        const newCard = document.createElement('div');
                        newCard.classList.add('card');
                        newCard.textContent = 'New Card';
                        document.querySelector('.card-container').appendChild(newCard);
                    }, 300);
                } else {
                    currentCard.style.transform = 'translateX(0) rotate(0)';
                }

                currentCard = null;
            }
        });
    });

    document.addEventListener('mouseup', () => {
        if (currentCard) {
            currentCard.style.transition = 'transform 0.3s, opacity 0.3s';
            currentCard.style.transform = 'translateX(0) rotate(0)';
            currentCard = null;
        }
    });
});
