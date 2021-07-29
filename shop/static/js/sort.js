function product_cag(product_cag) {
  document.getElementById('laptop').value = '';
  let param = 'product_cag=' + product_cag;
  send_request(param);
}

function sort_product(sort_product) {
  document.getElementById('laptop').value = '';
  let param = 'sort_product=' + sort_product;
  send_request(param);
}

function find_name() {
  let name = document.getElementById('laptop').value;
  let param = 'name=' + name;
  send_request(param);
}

function send_request(param) {
  $.ajax({
    method: 'GET',
    url: 'api/get_products/?' + param,
    success: function (result) {
      console.log(result);
      update_table(result);
    },
    error: function () {
      console.log('error');
    }
  });
}


function update_table(data) {
  let row;
  let all_rows = '';

  Object.keys(data).forEach(key => {
    elem = data[key];
    row = '<div class="product-block">' +
         ' <img class="product-block__image"' +
              'src="' +  elem['image'] + '"alt="Product"/>' +
         '<h4 class="product-block__title">' + elem['name'] + '</h4>' +
         '<div class="product-block__bottom">' +
             '<div class="product-block__price">' + elem['price'] + '₽</div>' +
             '<Button class="bth" value="' + elem['id'] + '" id="countProductToCart-' + elem['id'] + '" type="button">' +
                 'Добавить ' +
                 '<span id="countProductToCart-' + elem['id'] + 'Qty">' + elem['availabilityToCart'] + '</span>' +
             '</Button>' +
         '</div>' +
     '</div>';
    all_rows = all_rows + row;
  });

  $('#myProducts').html(all_rows);
};