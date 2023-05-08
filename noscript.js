// import {d} from "./index.js";
 // Output: "John"
const DD = localStorage.getItem('Data');
console.log(JSON.parse(DD));
var workData = JSON.parse(DD)
// console.log(workData["Name"]);

 var city = workData.Weather.City;
  var temp = workData.Weather.Temp_in_Celcius
  var myWeather = workData.Weather.Weather_Description;
  var humidity = workData.Weather.Humidity;
  var windSpeed = workData.Weather.Wind_Speed;
  var suggestion = workData.Response;
  var warning = workData.Weather.Warnings;


let weather = {
    apiKey: "1bdf680594d070a600a6565972a4991c",
    fetchWeather: function (city) {
      fetch(
        "https://api.openweathermap.org/data/2.5/weather?q=" +
          city +
          "&units=metric&appid=" +
          this.apiKey
      )
        .then((response) => {
          if (!response.ok) {
            alert("No weather found.");
            throw new Error("No weather found.");
          }
          return response.json();
        })
        .then((data) => this.displayWeather(data));
    },
    displayWeather: function (data) {
      const { name } = data;
      const { icon, description } = data.weather[0];
      const { temP, Humidity } = data.main;
      const { speed } = data.wind;
      document.querySelector(".city").innerText = "Weather in " + city;
      document.querySelector(".icon").src =
        "https://openweathermap.org/img/wn/" + icon + ".png";
      document.querySelector(".description").innerText = myWeather;
      document.querySelector(".temp").innerText = temp + "°C";
      document.querySelector(".humidity").innerText =
        "Humidity: " + humidity + "%";
      document.querySelector(".wind").innerText =
        "Wind speed: " + windSpeed + " km/h";
      document.querySelector(".crop").innerText =
        "Crop: " + windSpeed;
      document.querySelector(".suggestion").innerText =
        "Suggestion: " + suggestion;
      document.querySelector(".warning").innerText =
        "Warning: " + warning;
      document.querySelector(".weather").classList.remove("loading");
      document.body.style.backgroundImage =
        "url('https://source.unsplash.com/1600x900/?" +  "farming"+ "')";
    },
    search: function () {
      this.fetchWeather(document.querySelector(".search-bar").value);
    },
  };
  
  document.querySelector(".search button").addEventListener("click", function () {
    weather.search();
  });
  
  document
    .querySelector(".search-bar")
    .addEventListener("keyup", function (event) {
      if (event.key == "Enter") {
        weather.search();
      }
    });

 


  weather.fetchWeather(city);