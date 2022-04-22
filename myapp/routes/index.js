const { json } = require('express');
var express = require('express');
var fs = require('fs');
var path = require('path');
var router = express.Router();

/* absorb data to browser page*/
var object_data = null;
fs.readFile(path.resolve(__dirname, '../DATA/pear_video.json'), function(err, data){
  if(err){
    return console.error(err);
  }
  // object_data = {aa:11, bb:'789'}
  object_data = JSON.parse(data)

  console.log('this is a starting sign.')
  console.log('data:' + object_data)
  for(var key in object_data){
    console.log(key, typeof(key))
  }
  console.log('this is a middle sign.')
  
  // res.render('index', { json_data: JSON.parse(data)});
  console.log('this is a successful sign of sending data to browser.')
  
});

/* GET home page. */
router.get('/', function(req, res, next) {

  res.render('index', { json_data: object_data });
  // next() // pass control to the next handler
  
});


module.exports = router;
