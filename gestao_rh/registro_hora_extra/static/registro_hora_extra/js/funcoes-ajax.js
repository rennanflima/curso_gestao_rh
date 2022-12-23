function marcarHoraExtraUtilizada(id) {
    token = $("input[name='csrfmiddlewaretoken']").val();

    $.ajax({
        url: '/horas-extra/' + id + '/marcar-utilizada/',
        type: 'POST',
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function (data) {
            console.log(data);
            $('#mensagem').html('Hora extra marcada como utilizada com sucesso!<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>');
            $('#mensagem').removeClass('d-none');
            $('#btn-ajax').addClass('d-none');
        }
    });
}

function marcarHoraExtraNaoUtilizada(id) {
    token = $("input[name='csrfmiddlewaretoken']").val();

    $.ajax({
        url: '/horas-extra/' + id + '/marcar-nao-utilizada/',
        type: 'POST',
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function (data) {
            console.log(data);
            $('#mensagem').html('Hora extra marcada como não utilizada com sucesso!<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>');
            $('#mensagem').removeClass('d-none');
            $('#btn-ajax-utilizada').addClass('d-none');
        }
    });
}
