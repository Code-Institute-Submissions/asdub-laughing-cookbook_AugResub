// Event listener for Materilize components
document.addEventListener('DOMContentLoaded', function() {
    // Vars for mobile side navigation 
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
    // Vars and options for Materialize tooltip for 'Add to My Recipes'
    var save_tooltip = document.querySelectorAll('.tooltipped');
    var instances = M.Tooltip.init(save_tooltip, {
                                    position: "top", 
                                    html: "Save to My Recipes",
                                    margin: 0.2
                                  });
    var remove_tooltip = document.querySelectorAll('.remove-fab');
    var instances = M.Tooltip.init(remove_tooltip, {
                                    position: "top", 
                                    html: "Unpin from My Recipes",
                                    margin: 0.2
                                  });
    var delete_tooltip = document.querySelectorAll('.delete-fab');
    var instances = M.Tooltip.init(delete_tooltip, {
                                    position: "top", 
                                    html: "Delete your Recipe",
                                    margin: 0.2
                                    });
  });

document.getElementById("addingredient").addEventListener("click", function add_ingredient() {
  var x = document.getElementById("incredientsContainer");
  var new_field = document.createElement("input");
  new_field.setAttribute("type", "text");
  new_field.setAttribute("name", "ingredients");
  new_field.setAttribute("minlength", "5");
  new_field.setAttribute("maxlength", "30");
  new_field.setAttribute("class", "validate");
  var pos = x.childElementCount;

  x.insertBefore(new_field, x.childNodes[pos]);

});

document.getElementById("addinstruction").addEventListener("click", function add_instruction() {
  var x = document.getElementById("instructionsContainer");
  var new_field = document.createElement("input");
  new_field.setAttribute("type", "text");
  new_field.setAttribute("name", "instructions");
  new_field.setAttribute("minlength", "5");
  new_field.setAttribute("maxlength", "30");
  new_field.setAttribute("class", "validate");
  var pos = x.childElementCount;

  x.insertBefore(new_field, x.childNodes[pos]);
});

// CREDIT: https://dev.to/niick007/how-to-add-unlimited-fields-in-form-using-javascript-and-store-into-database-with-php-14ni