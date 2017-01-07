var googlehome = require('google-home-notifier');

var sarahHome = process.argv[3] != 'None';
var deanHome = process.argv[2] != 'None';

googlehome.device('Google-Home-ca919d63084d94043816cfed89259ca6');

function notifyHome(message){
  googlehome.notify(message, function(res) {
    console.log(res);
  });
}

if(deanHome == false && sarahHome == true){
  notifyHome('Sarah is the only one here');
  // more logic to come here
} else if(deanHome == true && sarahHome == false){
  notifyHome('Dean is the only one here');
  // more logic to come here
} else {
  notifyHome('I\'m not sure what went wrong here');
}

