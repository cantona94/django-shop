$(document).on('click', '.remove', function () {
    if (window.confirm('Вы действительно хотите удалить ноутбук?')) {
        var cart_item = $('.remove').length;
        var id_tr = $(this).val();
        data = {
            id_product: id_tr,
        };
        $.ajax({
            method: 'DELETE',
            url: 'remove_cart_item/',
            data: data,
            success: function (data) {
                if (cart_item > 1) {
                    update_cart_item(id_tr);
                }
                else {
                    update_cart()
                };
                update_cart_item(id_tr);
                $('#allCountToCart').text(data.allCountToCart);
                $('#countTotalToCart').text(data.allCountToCart);
                $('#total_price').text(data.total_price);
                $('#totalPriceToCart').text(data.total_price);
            },
            error: function () {
                console.log('error');
            }
        });
    };
});

$(document).on('click', '#clear_cart', function () {
    if (window.confirm('Вы действительно хотите очистить корзину?')) {
        data = {};
        $.ajax({
            method: 'DELETE',
            url: 'clear_cart/',
            data: data,
            success: function (data) {
                update_cart();
                $('#allCountToCart').text(data.allCountToCart);
                $('#totalPriceToCart').text(data.total_price);
            },
            error: function () {
                console.log('error');
            }
        });
    };
});

function update_cart_item(name) {
  let all_rows = '';
  $('#' + name).html(all_rows);
};

function update_cart() {
  let all_rows = '<div class="container-sm">' +
  '<div class="cart_empty">' +
  '<h1>Корзина пустая</h1></div>' +
  '</div>' +
  '<div class="container-sm">' +
  '<div class="cart_empty">' +
  '<a href="http://127.0.0.1:8000/">'+
  '<button class="come_back">Вернуться назад</button>' +
  '</a>'+
  '</div>' +
  '</div>';

  $('#pageCart').html(all_rows);
};