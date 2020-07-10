$(document).ready(function() {

    /* load json file form Database */
    var dataVar;
    if (typeof data != "undefined" && data != null) {
        dataVar = JSON.parse(data["productList"]);
        console.log(typeof dataVar);
    }
    //  update function
    if (typeof update != "undefined" && update != null) {
        const productToUpdate = update[0];
        console.log(productToUpdate);
        $('#productId').val(productToUpdate["id"]);
        $('#productName').val(productToUpdate["productName"]);
        $('#category').val(productToUpdate["category"]);
        $('#subCategory').val(productToUpdate["subCategory"]);
        $('#description').val(productToUpdate["description"]);
        $('#image').val(productToUpdate["image"]);
        $('#price').val(productToUpdate["price"]);
        $('#discount').val(productToUpdate["discount"]);
    }

    //category filter
    var filterCategory = dataVar.reduce(
        (obj, item) => Object.assign(obj, {
            [item.category]: item.subCategory
        }), {}
    );

    //navigation css
    $("body").on("click", ".nav-link", function() {
        $(this).toggleClass('text-danger');
    });

    //Category filter option
    $("body").on("click", ".filter-pills", function() {
        $(this).toggleClass('active');
        var selectedItems = [];
        $(".filter-pills").each(function() {
            if ($(this).hasClass("active")) {
                selectedItems.push($(this).attr("category"));
            }
        });
        var filteredItems;
        if (selectedItems.length != 0) {
            filteredItems = dataVar.filter(function(item) {
                return selectedItems.indexOf(item.category) > -1;
            });
        } else {
            filteredItems = dataVar;
        }
        viewProducts(filteredItems);
    });

    //filter nav pills
    $.each(Object.keys(filterCategory), function(index, item) {
        var categoryString =
            ' <a class="filter-pills" href="#" category="' +
            item +
            '">' +
            item +
            "</a>";
        $(".category-listing-navigation-pills").append(categoryString);
    });

    //render template
    function viewProducts(dataVar) {
        var templateString = "";
        $.each(dataVar, function(i) {
            if (data['superAdmin'] == 'true') {
                templateString +=
                    '<div class="col-lg-3 col-md-6 col-sm-6 col-xs-12">' +
                    '<div class="product-grid">' +
                    '<div class="product-image"><a href="#" class="image" style="background-color:#F3F3F3;"><img class="pic-1" alt="picture" src="' +
                    (dataVar[i].image == undefined || dataVar[i].image == '' ? 'https://unsplash.com/a/img/empty-states/photos.png' : dataVar[i].image) +
                    '"><a href="/update?id=' + dataVar[i].id + '" class="updateButton">EDIT</a></a></div>' +
                    '<div class="product-content"><h3 class="title"><a href="#">' +
                    dataVar[i].productName +
                    '</a></h3><div class="price">&#36;' +
                    dataVar[i].price +
                    '</div><p class="description"> ' +
                    dataVar[i].description +
                    '</p><ul class="rating">' +
                    '<li class="fas fa-star"></li>' +
                    '<li class="fas fa-star"></li>' +
                    '<li class="fas fa-star"></li>' +
                    '<li class="fas fa-star"></li>' +
                    '<li class="fas fa-star disable"></li>' +
                    '</ul></div><div class="action-buttons">' +
                    "</div></div>" +
                    "</div>";
            } else {
                templateString +=
                    '<div class="col-lg-3 col-md-6 col-sm-6 col-xs-12">' +
                    '<div class="product-grid">' +
                    '<div class="product-image"><a href="#" class="image" style="background-color:#F3F3F3;"><img class="pic-1" alt="picture" src="' +
                    (dataVar[i].image == undefined || dataVar[i].image == '' ? 'https://unsplash.com/a/img/empty-states/photos.png' : dataVar[i].image) +
                    '"></a></div>' +
                    '<div class="product-content"><h3 class="title"><a href="#">' +
                    dataVar[i].productName +
                    '</a></h3><div class="price">&#36;' +
                    dataVar[i].price +
                    '</div><p class="description"> ' +
                    dataVar[i].description +
                    '</p><ul class="rating">' +
                    '<li class="fas fa-star"></li>' +
                    '<li class="fas fa-star"></li>' +
                    '<li class="fas fa-star"></li>' +
                    '<li class="fas fa-star"></li>' +
                    '<li class="fas fa-star disable"></li>' +
                    '</ul></div><div class="action-buttons">' +
                    '<a class="btn-outline add-to-cart product_' +
                    dataVar[i].id +
                    '">ADD TO CART</a><a class="btn-outline-icon"><i class="far fa-heart"></i></a>' +
                    "</div></div>" +
                    "</div>";
            }
        });
        $("#products").html(templateString);
    }
    viewProducts(dataVar);
});