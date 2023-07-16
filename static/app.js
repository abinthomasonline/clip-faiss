document.getElementById('searchButton')
.addEventListener('click', function() {
    const searchTerm = document.getElementById('searchInput').value;
    if (searchTerm.trim() !== '') {
        const apiUrl = `/search?search_query=${searchTerm}`;
        fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            // data is a list of image urls
            // clear any previous results in results div
            // and add new results
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';
            data.forEach(imageUrl => {
                const img = document.createElement('img');
                img.src = imageUrl;
                resultsDiv.appendChild(img);
            });
        });
    }
});