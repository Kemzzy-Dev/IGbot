fetch('/task')
    .then(response => response.json())
    .then(data => {
        const filename = data.file;  

        document.getElementById('loadingScreen').style.display = 'none';
        document.getElementById('result').style.display = 'block';

        const linkElement = document.querySelector('.card-body a.btn-primary');
        linkElement.textContent = 'Download File';
        linkElement.href = 'download/' + filename;

        // Add event listener to the download link to prevent redirection
        linkElement.addEventListener('click', function(event) {
            event.preventDefault();
        });
    })
    .catch(error => console.error('Error:', error));