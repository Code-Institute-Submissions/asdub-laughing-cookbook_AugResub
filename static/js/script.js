// Event listener for Materilize components
document.addEventListener('DOMContentLoaded', function() {
    // Vars for mobile side navigation 
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
    // Vars and options for Materialize tooltip for 'Add to My Recipes'
    var tooltip = document.querySelectorAll('.tooltipped');
    var instances = M.Tooltip.init(tooltip, {
                                    position: "top", 
                                    html: "Save to My Recipes",
                                    margin: 0.2
                                  });
  });