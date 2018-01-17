// script.js

$(function() {
    
  $("button").click(function(){
     $('#box').fadeOut(1000);
  });
    
    /* -----------------
       jQUERY SELECTORS
       -----------------  */
    // Grouping selector
    //$('h2,h3,h4').css('border','solid 1px red');
    
    // ID selector
    //$('div#container').css('border','solid 1px red');
    
    // Class selector
    //$('p.lead').css('border','solid 1px red');
    
    // Pseudi-element selector - selects first element
    //$('li:first').css('border','solid 1px red');
    
    // Pseudo-element selector - selects even P tags
    //$('p:even').css('border','solid 1px red');
    
    // Descendant selector
    //$('div em').css('border','solid 1px red');
    
    // Child selector
    //$('div > p').css('border','solid 1px red');
    
    // jQuery Header selector
    //$(':header').css('border','solid 1px red');
    
    // jQuery Containts selector
    //$('div:contains("Ahmed")').css('border','solid 1px red');
    
    /* --------------------
       jQUER EVENT METHODS
       -------------------- */
    $('#box').click(function() {
      alert('you just clicked the box');  
    });
    
    $("input").blur(function() {
        if( $(this).val() == "" ){
            $(this).css('border','solid 1px red');
            $('#box').text('Forgot to add text?');
        }
    });
    
    $("input").keydown(function() {
        if($(this).val() !== ""){
            $(this).css('border','solid 1px #777');
            $('#box').text('Thanks for that!');
        }
    });
    
    $('#box').hover(function() {
        $(this).text('You hovered in!');
    }, function() {
        $(this).text('You hovered out!')
    });
    
    /* ---------------
       jQUERY CHAINING
       --------------- */
    
    $('.notification-bar').delay(2000).slideDown().delay(3000).fadeOut();
    
    
    /* -----------------
       jQUERY HIDE/SHOW
       ----------------- */
   // $('h1').hide();
    
   // $('div.hidden').show();
    
     //$('div.hidden').fadeIn();
    
    $('#box1').click(function() {
        $(this).fadeTo(1000, 0.25, function() {
            $(this).slideUp();
        });
    });
    
    $('div.hidden').slideDown();
    
    $('button').click(function(){
        $('#box1').slideToggle();
    });
    
    
    /* ---------------
       jQUERY ANIMATE 
       --------------- */

    $('#left').click(function() {
        $('.box').animate({
            left: "-=40px",
            fontSize: "+=2px"
        }, function() {
            // animation is complete
        
        });
    });
    
    
        $('#up').click(function() {
        $('.box').animate({
            top: "-=40px",
            opacity: "+=0.1"
        }, function() {
            // animation is complete
        
        });
    });
    
    
        $('#right').click(function() {
        $('.box').animate({
            left: "+=40px",
            fontSize: "-=2px"
        }, function() {
            // animation is complete
        
        });
    });
    
    
        $('#down').click(function() {
        $('.box').animate({
            top: "+=40px",
            opacity: "-=0.1"
        }, function() {
            // animation is complete
        
        });
    });
    
    
    /* --------------
       jQUERY CSS
       -------------- */
    
    $('#circle2').css({ 
        'background': '#8a8d22', 
        'display': 'inline-block', 
        'color': 'white', 
        'text-align': 'center', 
        'line-height': '140px', 
        'height': '140px', 
        'width': '140px',
    }).addClass('circleShape');
    
    
 
    // Click the GO button
    $('#go').click(function(){
        
        // build a function that checks to see if a car has won the race
        function checkIfComplete(){
            
            if( isComplete == false){
                isComplete = true;
            } else {
                place = 'second'
            }
        }
        
        // get the width of the cars
        var carWidth = $('#car1').width();
        
        // get the width of the racetrack
        var raceTrackWidth = $(window).width() - carWidth;
        
        // generate a random # between 1 and 5000
        
        var raceTime1 = Math.floor( (Math.random() * 5000) + 1 );
        var raceTime2 = Math.floor( (Math.random() * 5000) + 1 );
        
        // set a flasg variable to FALSE by default
        var isComplete = false;
        
        // set flag variable to FIRST by default
        var place = 'first';
        
        // animate car 1
        $('#car1').animate({
            
            // move the car with of the racetrack
            left: raceTrackWidth
        }, raceTime1, function() {
            
            // animation is complete
            
            // run a function
            checkIfComplete();
            
            // give some text feedback inthe race info box
            $('#raceInfo1 span').text('Finished in ' + place + ' place and clocked in at ' + raceTime1 + ' miliseconds!' );
        });
        
        // animate car 2
        $('#car2').animate({
            
            // move the car with of the racetrack
            left: raceTrackWidth
        }, raceTime2, function() {
            
            // animation is complete
            
            // run a function
            checkIfComplete();
            
            // give some text feedback inthe race info box
            $('#raceInfo2 span').text('Finished in ' + place + ' place and clocked in at ' + raceTime2 + ' miliseconds!' );
        });
    });
    
    // reset the race
    $('#reset').click(function() {
        $('.car').css('left','0');
        $('.raceInfo span').text('');
    });
    
    
    
    
    
    
    
    
});









