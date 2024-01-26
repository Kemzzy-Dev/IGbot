fetch('/task')
    .then(response => response.json())
    .then(data => {
        document.getElementById('loadingScreen').style.display = 'none';
        document.getElementById('result').style.display = 'block';
    })
    .catch(error => console.error('Error:', error));
 
