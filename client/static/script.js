const API_URL = 'http://localhost:8080/api/products';
let products = []

document.addEventListener('DOMContentLoaded', async () => {
    const response = await fetch(API_URL);
    products = await response.json();
});

function displayProducts(productsToDisplay) {
    const productsContainer = document.getElementById('productsContainer');
    productsContainer.innerHTML = '';

    productsToDisplay.forEach(product => {
        const productCard = document.createElement('div');
        productCard.className = 'product-card';
        productCard.innerHTML = `
            <h2>${product.name}</h2>
            <p class="price">${product.price} руб.</p>
            <p>${product.description}</p>
            <p class="categories">Категории: ${product.categories.join(', ')}</p>
        `;
        productsContainer.appendChild(productCard);
    });
}

function filterProducts(category) {
    if (category === 'all') {
        displayProducts(products);
    } else {
        const filteredProducts = products.filter(product => 
            product.categories.includes(category)
        );
        displayProducts(filteredProducts);
    }
}