

function render_cat(category) {
    console.log(category)
    url = ''
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            "category": category
        })
    })
        .then((response) => {
            response.json().then((data) => {
                datas = data['data']
                console.log(datas)
                html = ``
                for (let i = 0; i < datas.length; i++) {
                    html+=`
                    <div class="col-xl-3 col-lg-4 col-md-4 col-12">
                                            <div class="single-product">
                                                <div class="product-img">
                                                    <a href="product-details.html">
                                                        <img class="default-img"
                                                             src="${datas[i]['image']}"" alt="#">
                                                        <img class="hover-img" src="${datas[i]['image']}"
                                                             alt="#">
                                                    </a>
                                                    <div class="button-head">
                                                        <div class="product-action">
                                                            <a data-toggle="modal" data-target="#exampleModal"
                                                               title="Quick View" href="#"><i class=" ti-eye"></i><span>Quick Shop</span></a>
                                                            <a title="Wishlist" href="#"><i
                                                                    class=" ti-heart "></i><span>Add to Wishlist</span></a>
                                                            <a title="Compare" href="#"><i class="ti-bar-chart-alt"></i><span>Add to Compare</span></a>
                                                        </div>
                                                        <div class="product-action-2">
                                                            <a title="Add to cart" onclick="addtocart(${datas[i]['id']})  "href="#">Add to cart</a>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="product-content">
                                                    <h3><a href="product-details.html">${datas[i]['name']}</a></h3>
                                                    <div class="product-price">
                                                        <span>$${datas[i]['price']}</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                    `
                }
                document.getElementById('product_cat').innerHTML = html

            })
        })
}

render_cat(5)

function addtocart(category_id) {
    console.log(category_id)
    url = 'addtocart/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            "product_id": category_id
        })
    })
        .then((response) => {
            response.json().then((data) => {
                console.log(data['data'])
                


            })
        })
}



function minusproduct(category_id) {
    console.log(category_id)
    url = 'http://127.0.0.1:8000/minusproduct/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            "product_id": category_id
        })
    })
        .then((response) => {
            response.json().then((data) => {
                console.log(data['data'])
                


            })
        })
}

