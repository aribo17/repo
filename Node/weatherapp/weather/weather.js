const request = require('request');

var getWeather = (lat, lng, callback) => {
  const request = require('request');
  request({
      url:`https://api.darksky.net/forecast/d27d3db47cf2d826a51bd8539ec4f032/${lat},${lng}?units=si`,
      json: true
  }, (error, response, body)=>{
    if (!error && response.statusCode === 200) {
      callback(undefined, {
        temperature:body.currently.temperature,
        apparentTemperature: body.currently.apparentTemperature
      });
    } else {
      callback('Unable to fetch weather.');
    }

  });

};

module.exports.getWeather = getWeather;
