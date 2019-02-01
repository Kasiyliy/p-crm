activate_and_send_email = function (orderProducts, childs, vendor, client, order) {
    var table = "<head>\n" +
        "  <meta charset=\"UTF-8\"> \n" +
        "</head>";
    table = "<style> table {\n" +
        "  border-collapse: collapse;width: 100%;text-align: center;\n" +
        "}\n" +
        "\n" +
        "table, th, td {\n" +
        "  border: 1px solid black;\n" +
        "}" +
        "" +
        "</style>";

    var orderDate = new Date(order[0].fields.created_at).toLocaleString('ru', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour : 'numeric',
        minute : 'numeric',
        second : 'numeric'

      });
    table +="<h3>Продавец: "+vendor[0].fields.username +"</h3> " +
        "<h3>Клиент: "+ client[0].fields.client_name +"</h3>" +
        "<h3>Дата заказа: "+ orderDate+"<h1>";

    table += "<table >" +
        "    <thead>" +
        "        <th>#</th>" +
        "        <th>Наименование</th>" +
        "        <th>Количество</th>" +
        "        <th>Цена</th>" +
        "        <th>Сумма</th>" +
        "    </thead>" +
        "    <tbody>";
    var sum = 0;
    for (var i = 0; i < orderProducts.length; i++) {
        orderProduct = orderProducts[i].fields;
        var product = getProductById(orderProducts[i].fields.product, childs);
        if (product == null) {
            continue;
        }
        var tr = "<tr>\n<td>" + (i + 1) + "</td><td>" + product.title + "</td><td>" + orderProduct.quantity + "</td><td>" + product.price + "</td>" +
            "<td>" + (parseInt(orderProduct.quantity) * parseInt(product.price)) + "</td>\n</tr>\n";
        sum += (parseInt(orderProduct.quantity) * parseInt(product.price)) ;
        table += tr;
    }

    table += "    </tbody>\n" +
        "</table>";
    table += "<br><br><br><span>Общая сумма: "+sum+"</span>"
    var source = table;

    var newWindow = window.open();
    newWindow.document.write(table);
    newWindow.print();
    newWindow.close();
};

function decode_utf8( s ) {
  return decodeURIComponent( escape( s ) );
}

function getProductById(id, products) {
    for (var i = 0; i < products.length; i++) {
        var product = products[i];
        if (product.pk == id) {
            return product.fields;
        }
    }
    return null;
}