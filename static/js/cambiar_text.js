$(document).ready(function(){
$('#botones .boton').click(function(){ /*al hacer click en un botón*/
$('body').removeClass();    /*borre todas las clases*/
if(this.id == 'aumentar'){   /*si la clase botón tiene el ID aumentar*/
    $('body').addClass('grande');  /*cargue desde el CSS la clase grande*/
    }
else if(this.id == 'disminuir'){ /*si el ID es disminuir*/
    $('body').addClass('chica'); /*cargue la clase chica*/
}
$('#botones .boton').removeClass('seleccion'); /*elimine la negrita del boton*/
    $(this).addClass('seleccion');/*agregue la negrita al botón activo*/
 });
});

/*EFECTO HOVER*/
$(document).ready(function() {
  $('#botones .boton').hover(function() {
    $(this).addClass('sobre'); /*agregue efecto hover*/
  }, function() {
    $(this).removeClass('sobre');  /*quite efecto hover*/
  });
});