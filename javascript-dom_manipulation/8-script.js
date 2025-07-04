fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
        document.querySelector('DIV#hello').textContent = data.hello;
    })
    .catch(error => console.error('Error:', error));