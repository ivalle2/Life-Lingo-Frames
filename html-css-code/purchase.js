let itemCount = 0;
let totalPrice = 0;

function addItem(itemName, itemPrice) {
    itemCount++;
    totalPrice += itemPrice;

    document.getElementById('itemCount').textContent = itemCount;
    document.getElementById('totalPrice').textContent = totalPrice;
}

function goToCheckout() {
    sessionStorage.setItem('itemCount', itemCount);
    sessionStorage.setItem('totalPrice', totalPrice);

    window.location.href = 'checkout.html';
}
