/**
 * Exercise #8: Card board
 */

$(document).ready(function() {

    // This is for you to complete
    $("form[name='layout_form]").submit(function(){
        
        $("#cardboard").empty();
        
        var sizeCols = 3;
        var sizeRows = 4;
        var layout = $("#layout").val();
        var dim = layout.split("x");
        
        
        for(var row=0; row < sizeRows; row++){
            for(var col=0; col<sizeCols; col++){
                var card = $("<div>").addClass("card");
                if(col == 0){
                    card.addClass("clearleft");
                }
                $("#cardboard").append(card);
            }
        }
    
        return false;
    
    });
});
  