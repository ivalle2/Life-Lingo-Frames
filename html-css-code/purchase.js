let itemCount = 0;
let totalPrice = 0;

function addItem(itemName, itemPrice) {
    itemCount++;
    totalPrice += itemPrice;

    document.getElementById('itemCount').textContent = itemCount;
    document.getElementById('totalPrice').textContent = totalPrice;
}

function goToCheckout() {
    // Store item count and total price in session storage to access in checkout page
    sessionStorage.setItem('itemCount', itemCount);
    sessionStorage.setItem('totalPrice', totalPrice);

    // Redirect to checkout page
    window.location.href = 'checkout.html';
}
