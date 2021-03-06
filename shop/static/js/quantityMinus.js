$(document).on('click', '.button_minus', function () {
    var id_button = 'quantity_to_cart' + this.id.substr(6);
    var total_price_product = 'total_price_product-' + this.id.substr(6)
    var quantity = $('#' + id_button).text();
    if (quantity > 1) {
        data = {
            id_product: $(this).val(),
        };
        $.ajax({
            method: 'PUT',
            url: 'quantity_minus/',
            data: data,
            success: function (data) {
                $('#allCountToCart').text(data.allCountToCart);
                $('#countTotalToCart').text(data.allCountToCart);
                $('#totalPriceToCart').text(data.total_price)
                $('#total_price').text(data.total_price);
                $('#' + id_button).text(data.all_quantity_to_cart);
                $('#' + total_price_product).text(data.total_price_to_cart_product);
            },
            error: function () {
                console.log('error');
            }
        });
    };
});