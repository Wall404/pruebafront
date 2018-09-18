$(function () {

    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-agenda").modal("show");
        },
        success: function (data) {
            
        }
      });
    };
  
    $(".js-constancia-enviar").click(loadForm);
  
  });