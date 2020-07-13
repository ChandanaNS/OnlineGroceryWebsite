$(document).ready(function () {
	console.log('main.js')
	/* load json file form Database */
	var dataVar;
	if (typeof data != "undefined" && data != null) {
		dataVar = JSON.parse(data["productList"]);
		userData = data.userList;
		orderData = data.orderList;
		console.log(data);
	}
	//  update function
	if (typeof update != "undefined" && update != null) {
		const productToUpdate = update[0];
		$('#productId').val(productToUpdate["id"]);
		$('#productName').val(productToUpdate["productName"]);
		$('#category').val(productToUpdate["category"]);
		$('#subCategory').val(productToUpdate["subCategory"]);
		$('#description').val(productToUpdate["description"]);
		$('#image').val(productToUpdate["image"]);
		$('#price').val(productToUpdate["price"]);
		$('#discount').val(productToUpdate["discount"]);
	}
	//navigation css
	$("body").on("click", ".nav-link", function () {
		$(this).toggleClass('text-danger');
	});

    //flash message for 4s
	setTimeout(function () {
		$('.alert-warning').remove();
	}, 4000);


	//category filter
	var filterCategory = dataVar.reduce(
		(obj, item) => Object.assign(obj, {
			[item.category]: item.subCategory
		}), {}
	);


	//Category filter option
	$("body").on("click", ".filter-pills", function () {
		$(this).toggleClass('active');
		var selectedItems = [];
		$(".filter-pills").each(function () {
			if ($(this).hasClass("active")) {
				selectedItems.push($(this).attr("category"));
			}
		});
		var filteredItems;
		if (selectedItems.length != 0) {
			filteredItems = dataVar.filter(function (item) {
				return selectedItems.indexOf(item.category) > -1;
			});
		} else {
			filteredItems = dataVar;
		}
		viewProducts(filteredItems);
	});

	//filter nav pills
	$.each(Object.keys(filterCategory), function (index, item) {
		var categoryString =
			' <a class="filter-pills" href="#" category="' +
			item +
			'">' +
			item +
			"</a>";
		$(".category-listing-navigation-pills").append(categoryString);
	});

	//render template for products
	function viewProducts(dataVar) {
		var templateString = "";
		$.each(dataVar, function (i) {
			if (data['superAdmin'] == 'true') {
				templateString +=
					'<div class="col-lg-3 col-md-6 col-sm-6 col-xs-12">' +
					'<div class="product-grid">' +
					'<div class="product-image"><a href="#" class="image" style="background-color:#F3F3F3;"><img class="pic-1" alt="picture" src="' +
					(dataVar[i].image == undefined || dataVar[i].image == '' ? 'https://unsplash.com/a/img/empty-states/photos.png' : dataVar[i].image) +
					'"><a href="/update?id=' + dataVar[i].id + '" class="updateButton">EDIT</a></a></div>' +
					'<div class="product-content"><h3 class="title"><a href="#">' +
					dataVar[i].productName +
					'</a></h3><div class="price">$' +
					dataVar[i].price +
					'</div><p class="description"> ' +
					dataVar[i].description +
					'</p>'

					+
					(dataVar[i].discount != undefined ? "<p class='text-info text-center'> " + dataVar[i].discount + " left in stock</p>" : "") +

					'<ul class="rating">' +
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
					'</a></h3><div class="price">$' +
					dataVar[i].price +
					'</div><p class="description"> ' +
					dataVar[i].description +
					'</p>' +
					(dataVar[i].discount != undefined && dataVar[i].discount < 5 ? "<p class='text-danger text-center'> " + dataVar[i].discount + " left in stock</p>" : "") +

					'<ul class="rating">' +
					'<li class="fas fa-star"></li>' +
					'<li class="fas fa-star"></li>' +
					'<li class="fas fa-star"></li>' +
					'<li class="fas fa-star"></li>' +
					'<li class="fas fa-star disable"></li>' +
					'</ul></div><div class="action-buttons">' +
					'<a class="btn-outline add-to-cart product_' +
					dataVar[i].id + (dataVar[i].discount == 0 ? " isDisabled" : "") +
					'">ADD TO CART</a><a class="btn-outline-icon"><i class="far fa-heart"></i></a>' +
					"</div></div>" +
					"</div>";
			}
		});
		$("#products").html(templateString);
	}


	viewProducts(dataVar);


	//render template for users
	function viewUsers(userData) {

		var templateString = '';
		$.each(userData, function (i) {
			if (data['superAdmin'] == 'true') {
				templateString += '<tr><th scope="row">' +
					userData[i].loginId + '</th><td >' + userData[i].userName + '</td><td >' + userData[i].dateOfBirth +
					'</td><td >' + userData[i].email + '</td><td >' + userData[i].gender + '</td><td >' +
					userData[i].name + '</td><td >' + userData[i].phoneNumber + '</td><td >' + userData[i].walletBalance + '</th></tr>';
			}
		});
		var tableString = '<div class="tableClass"><div class="table-responsive"><table class="table "><thead class="thead-dark"><tr><th scope="col">UserId</th>' +
			'<th scope="col">User Name</th><th scope="col">Date of Birth</th><th scope="col">Email</th>' +
			'<th scope="col">Gender</th><th scope="col">Name</th><th scope="col">Phone Number</th>' +
			'<th scope="col">Wallet Balance</th></tr></thead><tbody>' +
			templateString +
			'</tbody></table></div></div>';
		$("#products").html(tableString);
	}

	//render template for Orders
	function ViewOrders(orderData) {
		[{
			"id": 4,
			"category": "Fresh",
			"productName": "Banana",
			"subCategory": "Fruits",
			"description": "10 Pieces",
			"image": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1100&q=80",
			"price": 6.0,
			"numberOfItems": 12,
			"totalCountOrdered": 1,
			"orderedBy": "sid",
			"timeStamp": "2020-07-11T22:43:56"
		}]
		var templateString = '';
		$.each(orderData, function (i) {
			if (data['superAdmin'] == 'true') {
				templateString += '<tr><th scope="row">' +
					orderData[i].id + '</th><td >' + orderData[i].category + '</td><td >' + orderData[i].subCategory +
					'</td><td >' + orderData[i].productName + '</td><td >' + orderData[i].price + '</td><td >' +
					orderData[i].numberOfItems + '</td><td >' + orderData[i].totalCountOrdered + '</td><td >' + orderData[i].orderedBy + '</td><td >' + orderData[i].timeStamp + '</td></tr>';
			}
		});
		var tableString = '<div class="tableClass"><div class="table-responsive"><table class="table "><thead class="thead-dark"><tr><th scope="col">Product ID</th>' +
			'<th scope="col">Category</th><th scope="col">Sub Category</th><th scope="col">Product Name</th>' +
			'<th scope="col">Price</th><th scope="col">No of products</th><th scope="col">Ordered Nos</th>' +
			'<th scope="col">Ordered By</th><th scope="col">Date of order</th></tr></thead><tbody>' +
			templateString +
			'</tbody></table></div></div>';
		$("#products").html(tableString);
	}

    //fetch user details
	$("body").on("click", ".user-statistic", function (event) {
		event.preventDefault();
		$('nav').find('.text-danger').removeClass('text-danger');
		$(this).addClass('text-danger');
		$('body').find('.feature-title').addClass('d-none');
		viewUsers(userData);
	});

	//fetch order details
	$("body").on("click", ".order-statistic", function (event) {
		event.preventDefault();
		$('nav').find('.text-danger').removeClass('text-danger');
		$(this).addClass('text-danger');
		$('body').find('.feature-title').addClass('d-none')
		ViewOrders(orderData);
	});

});