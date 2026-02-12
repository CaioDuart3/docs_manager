(function() {
    const search = document.getElementById('search');
    if (search) {
        search.addEventListener('input', function() {
            const query = this.value.toLowerCase();

            const cards = document.querySelectorAll('.card-document');
            cards.forEach(card => {
                const title = card.querySelector('#title-document').textContent.toLowerCase();
                console.log(title);
                if (title.includes(query)) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }
})();