console.log('Привет мир!!!')
/*Получаем csrf-токен */
function getCookie(name) {
	let cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		const cookies = document.cookie.split(';');
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
const csrftoken = getCookie('csrftoken');
/*Функция очистки */
function clearElem(){
	let main_block_painting = document.querySelector('.main_block_painting');
	main_block_painting.innerHTML = ''
}
/*Функция заполнения новых карточек по данным FETCH */
function addPaintingCart(obj){
	let main_block_painting = document.querySelector('.main_block_painting');
	let cart = document.createElement('div');
	cart.classList.add('cart')
	cart.innerHTML = `
	<a href="/paintings/paint/${obj.slug}">
	<img src="/media/${obj.imagePainting}" alt="Нет фото">
	</a>
					<p class="autor_painting">${obj.autor}</p>
					<h3 class="name_painting">${obj.name}</h3>
					<p class="format_painting">${obj.formPaint_id}</p>
					<h3 class="price_painting">${obj.price+',00'}</h3>
					<form action="/cart/add_cart/${obj.id}" method="post">
						<input type="hidden" name="csrfmiddlewaretoken" value=${csrftoken}>
						<input type="submit" class="card_painting" value="В корзину">
					</form>
	`
	main_block_painting.append(cart);
}

/*Делаем запрос */
let btn_res = document.querySelectorAll('.btn_res');
btn_res.forEach(btn=>{
	btn.addEventListener('click', takePaintings);
})
//Функция для запроса
function takePaintings(event) {
	let name_country = event.target.value;
	let url = "";
	let data = { country: name_country };
	fetch(url, {
		method: "POST",
		headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken },
		body: JSON.stringify(data)
	}).then(res => res.json()).then(data => {
		data = JSON.parse(data)
		clearElem();
		data.forEach((item)=>{
			addPaintingCart(item)
			console.log(item)
		})
	}).catch(err => {
		console.log(err)
	})
}
/*http://127.0.0.1:8000/paintings/paint/dama-s-sobachkoj */
/*http://127.0.0.1:8000/paintings/paint/dama-s-sobachkoj */

/*Открытие и закрытие меню навигации */

let open_close_btn_menu = document.querySelector('.open_close');
let menu = document.querySelector('.header__nav');
open_close_btn_menu.onclick = () => {
	menu.classList.toggle('header__buttons__close')
}