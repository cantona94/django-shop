$(document).on('click', '.bth', function () {
    var id_button = this.id + 'Qty';
    console.log(id_button)
    data = {
        id_product: $(this).val(),
    }
    $.ajax({
        method: 'POST',
        url: 'add_to_cart/',
        data: data,
        success: function (data) {
            $('#allCountToCart').text(data.allCountToCart)
            $('#' + id_button).text(data.productToCart)
        },
        error: function () {
            console.log('error');
        }
    });
});