document.getElementById('submit-button').addEventListener('click', function() {
    var data = {};

    // Select all input elements within the form
    const inputs = document.querySelectorAll('form input');

    // Populate the data object with the values from the form fields
    inputs.forEach(input => {
        if (input.type === 'checkbox') {
            data[input.name] = input.checked;
        } else {
            data[input.name] = input.value;
        }
    });

    // Populate the data object with the values from the form fields
    fetch('/api/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        var image = document.getElementById('result-image');
        if (data.status === 'transported') {
            image.src = 'static/transported.jpeg';
            image.classList.add('intense-dance');
        } else {
            image.src = 'static/safe.jpeg';
            image.classList.add('dance');
        }
        image.style.display = 'block';
    });
});

const submitButton = document.getElementById('submit-button');
const image = document.getElementById('result-image');

// Function to make the image dance
function makeImageDance() {
    // Add a CSS class to the image to apply animations
    image.classList.add('dance');
}

// Add event listener to the submit button
submitButton.addEventListener('click', function() {
    // Ensure the image is loaded and visible
    if (image.complete) {
      makeImageDance();
    } else {
      image.onload = makeImageDance;
    }
});

document.addEventListener('DOMContentLoaded', function() {
    // Select all input elements on the page
    const inputs = document.querySelectorAll('input');

    // Function to generate a random value
    function getRandomInteger() {
        return Math.floor(Math.random() * 100); // Generates a random number between 0 and 99
    }

    // Function to generate a random string
    function getRandomString(length) {
        const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        let result = '';
        for (let i = 0; i < length; i++) {
            result += characters.charAt(Math.floor(Math.random() * characters.length));
        }
        return result;
    }

    // Function to generate a random boolean
    function getRandomBoolean() {
        return Math.random() < 0.5;
    }

    // Function to generate a random float
    function getRandomFloat(max) {
        return (Math.random() * max).toFixed(2);
    }

    // Function to generate a random name
    function getRandomName() {
        const names = ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown'];
        return names[Math.floor(Math.random() * names.length)];
    }

    // Populate each input with a random value based on its name attribute
    inputs.forEach(input => {
        switch (input.name) {
            case 'PassengerId':
                input.value = getRandomInteger();
                break;
            case 'HomePlanet':
                input.value = getRandomString(8);
                break;
            case 'CryoSleep':
                input.checked = getRandomBoolean();
                break;
            case 'Cabin':
                input.value = getRandomString(5);
                break;
            case 'Destination':
                input.value = getRandomString(8);
                break;
            case 'Age':
                input.value = getRandomFloat(100);
                break;
            case 'VIP':
                input.checked = getRandomBoolean();
                break;
            case 'RoomService':
                input.value = getRandomFloat(1000);
                break;
            case 'FoodCourt':
                input.value = getRandomFloat(1000);
                break;
            case 'ShoppingMall':
                input.value = getRandomFloat(1000);
                break;
            case 'Spa':
                input.value = getRandomFloat(1000);
                break;
            case 'VRDeck':
                input.value = getRandomFloat(1000);
                break;
            case 'Name':
                input.value = getRandomName();
                break;
            case 'hash':
                input.value = getRandomString(16);
                break;
            case 'status':
                input.value = getRandomString(8);
                break;
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/count_transported')
        .then(response => response.json())
        .then(data => {
            document.getElementById('transported-count').textContent = data.count;
        })
        .catch(error => console.error('Error fetching transported count:', error));
});