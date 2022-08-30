$(document).ready(function (e) {

      $('#upload').on('click', function() {
        $('#spinner1').show();
        var form_data = new FormData();
        var ins = document.getElementById('multifiles').files.length;
        console.log(ins);
        if(ins == 0){
          $('#msg').html('<div class="alert alert-danger" role="alert">Select at least one file</div>');
          return;
        }
        else if(ins > 1){
          $('#msg').html('<div class="alert alert-danger" role="alert">Bitte nur eine Datei auswählen</div>');
          return;
        }
        else{
          form_data.append("files[]", document.getElementById('multifiles').files[0])
        }
        csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
        console.log(csrf_token);

        form_data.append("csrfmiddlewaretoken", csrf_token);

        $.ajax({
          url: '',
          dataType: 'json',
          cache: false,
          contentType: false,
          processData: false,
          data: form_data,
          type: 'post',
          success: function(response) {
            $('#msg').html(response.msg);
            $('#download').html(response.download);
            $('#spinner1').hide();

          },
          error: function(response) {
            $('#msg').html(response.message);
          }

        })

      });
});