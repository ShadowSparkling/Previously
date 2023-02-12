{
  /* // jQuery syntax looks like This */
}

// $(selector).action()
$(document).ready(function () {
  //To view I clicked on element p when I click on element p
    $("p").click(function () {
    console.log("I clicked on element p.", this);
    });

    //To double click on p
    // $('p').dblclick(function () {
    //     console.log("I clicked on element p.", this);
    //     });


    //hover event
    // $('p').hover(function() {
    //     console.log('you hovered on: ', this);

    // },
    // function() {
    //     console.log('Thanks for coming.')
    // });


  //This is an instance of class selector.
  // $(".odd").click(function () {
  //   $(this).hide();
  // });

  //Id selector
  // $("#second").click(function() {
  //   $(this).hide();
  // })

  //other selector
  // $("*") ...  //Selects all the elements
  // $('p.odd').click()    //selects the p element having 'odd' class
  // $('p:first').click()   //selects the first p element

// Mouse events = click, dblclick, mouseenter, mouseleave
// Keyboard Events = keypress, keydown, MediaKeyStatusMap
//form events = submit, change, focus, blur
// document/window events = load, resize, scroll, unload


// demoing the ON method 
    // $('p').on(
    //     {
    //         click: function () {
    //             console.log("Thanks for clicking", this);
    //         },
    //         mouseleave: function() {
    //             console.log("mouseleave");
    //         }



    //     });

    // $('#wiki').hide(1000, function() {
    //     console.log('hidden');
    // })
    // $('#wiki').show(1000, function() {
    //     console.log('SHOW');
    // })


    //using a button to use fade in and fade out animation
// $('#but').click( function(){
//     $('#wiki').fadeOut(1000); 


//Slide methods - takes time and callback method as parameters.
// $('#wiki').slideToggle(1000);
// $('#wiki').slideDown(1000);
// $('#wiki').slideUp(1000);



// })


//Animate function in jQuery
// $('#wiki').animate({opacity: 0.3}, 2000);
// $('#wiki').animate({height: '4rem'}, 2000);

// Stop the animation using
// $('#wiki').stop();


$('#wiki').css('background', 'red'); 




});
