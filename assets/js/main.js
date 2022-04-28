const elSearchInput = document.querySelector('.search-input');
const elMenuBtn = document.querySelector('.btn-menu');
const elMenu = document.querySelector('.navbar');
const elModal = document.querySelector('.layer');
const elCancelModal = document.querySelector('.hide-modal-btn');
const elMenuMask = document.querySelector('.menu-mask');
const elSearchBtn = document.querySelector('.search-btn');

elSearchBtn.addEventListener('click', () => {
  elSearchInput.classList.toggle('search-input--active');
});

elMenuBtn.addEventListener('click', () => {
  elMenuBtn.classList.toggle('menu-btn--active');
  document.querySelector('body').classList.toggle('open-menu');
  elMenuMask.classList.toggle('menu-mask--active');
});

elMenuMask.addEventListener('click', evt => {
  if (!evt.target.matches('.navbar')) {
    elMenuBtn.classList.toggle('menu-btn--active');
    document.querySelector('body').classList.toggle('open-menu');
    elMenuMask.classList.toggle('menu-mask--active');
  }
});


    
fetch('https://coronavirus-19-api.herokuapp.com/countries/uzbekistan')
  .then(response => response.json())
  .then(data => {
    document.querySelector('.infected').innerHTML = data.cases;
    document.querySelector('.died').innerHTML = data.deaths;
    document.querySelector('.recovered').innerHTML = data.recovered;
});
  
  

// if(location.href=="http://namanganliklar24.uz/"){
//   setTimeout(function(){
//     elModal.classList.add('modal--show');
//   }, 40000)
// }
  
// function showLayer(){
//   elModal.classList.add('modal--show');
// }

// setInterval(showLayer, 90000);

// elCancelModal.addEventListener('click', () => {
//   elModal.classList.remove('modal--show');
// });