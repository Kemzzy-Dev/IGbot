fetch('/task')
    .then(response => response.json())
    .then(data => {
        const fileLink = data.file;  

        document.getElementById('loadingScreen').style.display = 'none';
        document.getElementById('result').style.display = 'block';

         // Populate the <p> tag with the result data
         const cardText = document.querySelector('.card-body .card-text');
         cardText.textContent = `Find the results here: ${fileLink}`;

         // Populate the <a> tag with the file link
        const linkElement = document.querySelector('.card-body a.btn-primary');
        linkElement.href = fileLink;
        linkElement.textContent = 'Open File'; // Update the text of the link

        var hostname = window.location.hostname;
        var file = fileLink.replace(`${hostname}/`, '');
        console.log(hostname)
        console.log(file)

        // Open the file link in a new tab for viewing
        linkElement.addEventListener('click', function(event) {
            event.preventDefault();
            window.open(file, '_blank');
        })
    })
    .catch(error => console.error('Error:', error));
 
