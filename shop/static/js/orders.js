$(document).on('click', '.button_order', function () {
    data = {}
    $.ajax({
        method: 'POST',
        url: 'add_order/',
        data: data,
        success: function () {
            alert("Заказ оформлен!")
        }
    });
});