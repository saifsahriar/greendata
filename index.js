
const url1 = 'https://script.google.com/macros/s/AKfycbzShHU0dDOB_REnETOnIxmbv2lFd__6tDJa5DNPvMsPS_JaQPJLb-hmE1Tee0kk3WV-iw/exec';

const url2 = "https://weather.jeetghosh3.repl.co/report/";

// let name = document.querySelector("#name").value;
// let phone = document.querySelector("#phone").value;
// let pin = document.querySelector("#pin").value;
// let city = document.querySelector("#city").value;

// let form = document.querySelector("form");


const form = document.querySelector('#myForm');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const nameInput = document.querySelector('#name');
  const phoneInput = document.querySelector('#phone');
  const pinInput = document.querySelector('#pin');
  const cityInput = document.querySelector('#city');
  const cropInput = document.querySelector('#crop');

  const name = nameInput.value;
  const phone = phoneInput.value;
  const pin = pinInput.value;
  const city = cityInput.value;
  const crop = cropInput.value;


  const sendUrl = `${url2}?name=${name}&phone=${phone}&pin=${pin}&city=${city}&crop=${crop}`;
var json = []
  async function myFunc(){
await fetch(sendUrl)
  .then(response => response.json())
  .then(data => {
    // store the JSON object in a local variable
    const mydata = data;
    // do something with the jsonData variable
    console.log(mydata);
    localStorage.setItem('Data', JSON.stringify(mydata));
    location.replace("./data.html");

  })
  .catch(error => {
    console.error('Error fetching data:', error);
     
  });
    
  }
  myFunc()
  // var X = fetch(sendUrl)
  // .then(response => response.json())
  // // .then(data => console.log(data))
  //   // .then(localStorage.setItem('jsonD', JSON.stringify(response)))
  // .catch(error => console.error(error));
  // // form.reset();
  // var Z = JSON.stringify(X)
  // console.log(Z);
  
  // export var d = data;
   // location.replace("./data.html");

});

// form.addEventListener('submit', (e) => {
//     e.preventDefault();
//     let data = new FormData(form);
//     fetch(url1, {
//         method: "POST",
//         body: data,
//     })
//         .then(res => res.text())
//         .then(data => console.log(data));
//   console.log(data)
// });

