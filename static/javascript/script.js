fetch('/task')
    .then(response => response.json())
    .then(data => {
        const fileLink = data.file;  

        document.getElementById('loadingScreen').style.display = 'none';
        document.getElementById('result').style.display = 'block';

         // Create a blob URL for the file
        fetch(fileLink)
            .then(response => response.blob())
            .then(blob => {
                const url = URL.createObjectURL(blob);

                // Populate the <a> tag with the file link
                const linkElement = document.querySelector('.card-body a.btn-primary');
                linkElement.href = url;
                linkElement.download = fileLink.split('/').pop(); // Set the download attribute to the file name
                linkElement.textContent = 'Download File'; // Update the text of the link
            })
            .catch(error => console.error('Error:', error));
    })
    .catch(error => console.error('Error:', error));
