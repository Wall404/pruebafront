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
				$("#modal-agenda .modal-content").html(data.html_form);
			}
		});
	};

	var saveForm = function () {
		var form = $(this);
		$.ajax({
			url: form.attr("action"),
			data: form.serialize(),
			type: form.attr("method"),
			dataType: 'json',
			success: function (data) {
				if (data.form_is_valid) {
					$("#modal-agenda").modal("hide");
					$("#agenda-table tbody").html(data.html_agenda_lista);
				}
				else {
					$("#modal-agenda .modal-content").html(data.html_form);
				}
			}
		});
		return false;
	};

	// Agregar Item
	$(".js-agregar-item").click(loadForm);
	$("#modal-agenda").on("submit", ".js-agregar-item-form", saveForm);

	// Ver Item
	$(".js-ver-item").click(loadForm);
	$("#modal-agenda").on("submit", ".js-ver-item-form", saveForm);
	
	// Modificar item
	$("#agenda-table").on("click", ".js-modificar-item", loadForm);
	$("#modal-agenda").on("submit", ".js-boton-modificar", saveForm);
	
	// Borrar item
	$("#agenda-table").on("click", ".js-borrar-item", loadForm);
	$("#modal-agenda").on("submit", ".js-boton-borrar", saveForm);

});