let cartItems = [];
let cartTotal = 0;

function addToCart(productName, price) {
    cartItems.push({ name: productName, price: price });
    cartTotal += price;

    updateCart();
}

function updateCart() {
    const cartElement = document.getElementById('cart-items');
    const cartTotalElement = document.getElementById('cart-total');
    
    cartElement.innerHTML = '';
    
    cartItems.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} - $${item.price}`;
        cartElement.appendChild(li);
    });

    cartTotalElement.textContent = cartTotal.toFixed(2);
}

function checkout() {
    alert(`Total amount payable: $${cartTotal.toFixed(2)}`);
    cartItems = [];
    cartTotal = 0;
    updateCart();
}
