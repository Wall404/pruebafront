$("#modal-agenda").on("submit", ".js-agregar-item", function () {

    var form = $(this);
    $.ajax({
		url: form.attr("action"),
		data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',       
        success: function (data) {
			if(data.form_is_valid) {
				$("#agenda-table tbody").html(data.html_agenda_lista);
				$("#modal-agenda").modal("hide");
			}
			else {
				$("#modal-agenda .modal-content").html(data.html_form);
			}
        }
      });
	return false
  
  });