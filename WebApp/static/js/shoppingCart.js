// ************************************************
// Shopping Cart API
// ************************************************
var walletBalance = parseFloat($('.total-balance')[0].innerHTML.trim());
// Add item

$("body").on("click", ".add-to-cart", function () {
	var name = $(this).parent().parent().find(".title").text();
	var price = $(this).parent().parent().find(".price").text();
	var id = parseInt($(this)[0].className.split(' ')[2].split('_')[1])

	price = Number(price.substring(1));
	$('.added__animation').addClass('clicked');
	setTimeout(function () {
		$('.added__animation').removeClass('clicked');
	}, 600);
	shoppingCart.addItemToCart(name, price, 1, id);
	displayCart();
});

//flash message for 4s
setTimeout(function () {
	$('.alert-warning').remove();
}, 4000);


var shoppingCart = (function () {
	// =============================
	// Private methods and propeties
	// =============================
	cart = [];

	// Constructor
	function Item(name, price, count, id) {
		this.name = name;
		this.price = price;
		this.count = count;
		this.id = id;
	}

	// Save cart
	function saveCart() {
		sessionStorage.setItem("shoppingCart", JSON.stringify(cart));
	}

	// Load cart
	function loadCart() {
		cart = JSON.parse(sessionStorage.getItem("shoppingCart"));
	}
	if (sessionStorage.getItem("shoppingCart") != null) {
		loadCart();
	}

	// =============================
	// Public methods and propeties
	// =============================
	var obj = {};

	// Add to cart
	obj.addItemToCart = function (name, price, count, id) {

		for (var item in cart) {
			if (cart[item].name === name && cart[item].price == price) {
				cart[item].count++;
				saveCart();
				return;
			}
		}
		var item = new Item(name, price, count, id);
		cart.push(item);
		saveCart();

	};
	// Set count from item
	obj.setCountForItem = function (name, count) {
		for (var i in cart) {
			if (cart[i].name === name) {
				cart[i].count = count;
				break;
			}
		}
	};
	// Remove item from cart
	obj.removeItemFromCart = function (name) {
		for (var item in cart) {
			if (cart[item].name === name) {
				cart[item].count--;
				if (cart[item].count === 0) {
					cart.splice(item, 1);
				}
				break;
			}
		}
		saveCart();
	};

	// Remove all items from cart
	obj.removeItemFromCartAll = function (name) {
		for (var item in cart) {
			if (cart[item].name === name) {
				cart.splice(item, 1);
				break;
			}
		}
		saveCart();
	};

	// Clear cart
	obj.clearCart = function () {
		cart = [];
		saveCart();
	};

	// Count cart
	obj.totalCount = function () {
		var totalCount = 0;
		for (var item in cart) {
			totalCount += cart[item].count;
		}
		return totalCount;
	};

	// Total cart
	obj.totalCart = function () {
		var totalCart = 0;
		for (var item in cart) {
			totalCart += cart[item].price * cart[item].count;
		}
		walletBalance -= Number(totalCart.toFixed(2))
		return Number(totalCart.toFixed(2));
	};

	// List cart
	obj.listCart = function () {
		var cartCopy = [];
		for (i in cart) {
			item = cart[i];
			itemCopy = {};
			for (p in item) {
				itemCopy[p] = item[p];
			}
			itemCopy.total = Number(item.price * item.count).toFixed(2);
			cartCopy.push(itemCopy);
		}
		return cartCopy;
	};

	// cart : Array
	// Item : Object/Class
	// addItemToCart : Function
	// removeItemFromCart : Function
	// removeItemFromCartAll : Function
	// clearCart : Function
	// countCart : Function
	// totalCart : Function
	// listCart : Function
	// saveCart : Function
	// loadCart : Function
	return obj;
})();

// Clear items
$(".clear-cart").click(function () {
	shoppingCart.clearCart();
	displayCart();
});

//Clear cart after success order
if ($(".alert-warning").length > 0) {
	shoppingCart.clearCart();
	displayCart();
}

//display cart items
function displayCart() {
	var cartArray = shoppingCart.listCart();
	var output = "";
	for (var i in cartArray) {
		output +=
			"<tr>" +
			"<td class=" +
			cartArray[i].id +
			">" +
			cartArray[i].name +
			"</td>" +
			"<td>(" +
			cartArray[i].price +
			")</td>" +
			"<td><div class='input-group'><button class='minus-item input-group-addon btn btn-primary' data-name=" +
			cartArray[i].name +
			">-</button>" +
			"<input type='number' class='item-count form-control' data-name='" +
			cartArray[i].name +
			"' data-price='" +
			cartArray[i].price +
			"' value='" +
			cartArray[i].count +
			"'>" +
			"<button class='plus-item btn btn-primary input-group-addon' data-name=" +
			cartArray[i].name +
			" data-price=" +
			cartArray[i].price +
			">+</button></div></td>" +
			"<td><button class='delete-item btn btn-danger' data-name=" +
			cartArray[i].name +
			">X</button></td>" +
			" = " +
			"<td>" +
			cartArray[i].total +
			"</td>" +
			"</tr>";
	}
	$(".show-cart").html(output);
	$(".total-cart").html(shoppingCart.totalCart());
	$(".total-count").html(shoppingCart.totalCount());
}

//disable order button if cart value is none
$("body").on("click", ".cart", function () {
	var totalcart = parseInt($('.total-cart')[0].innerText);
	if (totalcart <= 0) {
		$('.order').prop('disabled', true);
		$('.ordera').addClass('isDisabled');
	} else {
		$('.order').prop('disabled', false);
		$('.ordera').removeClass('isDisabled');
	}
});

// Delete item button
$(".show-cart").on("click", ".delete-item", function (event) {
	var name = $(this).data("name");
	shoppingCart.removeItemFromCartAll(name);
	displayCart();
});

// -1
$(".show-cart").on("click", ".minus-item", function (event) {
	var name = $(this).data("name");
	shoppingCart.removeItemFromCart(name);
	displayCart();
});
// +1
$(".show-cart").on("click", ".plus-item", function (event) {
	var name = $(this).data("name");
	var price = $(this).data("price");
	shoppingCart.addItemToCart(name, price);
	displayCart();
});

// Item count input
$(".show-cart").on("change", ".item-count", function (event) {
	var name = $(this).data("name");
	var count = Number($(this).val());
	shoppingCart.setCountForItem(name, count);
	displayCart();
});

//    AJAX call for order sent
$("body").on("click", ".order", function () {
	var cartData = (sessionStorage.getItem("shoppingCart"));
	var request = {
		'data': cartData,
		'wallet': walletBalance
	}
	$.ajax({
		type: "POST",
		url: '/location',
		dataType: "json",
		data: JSON.stringify(request),
		contentType: 'application/json',
		success: function (data) {
			console.log("Ajax success")
			$('#flash_message').html(JSON.stringify(data, null, '   '));
			window.location.href = "/location";
		},
		error: function (data) {
			console.log(data);
			$('#flash_message').html(JSON.stringify(data, null, '   '));
			window.location.href = "/";
		}
	});


});

displayCart();