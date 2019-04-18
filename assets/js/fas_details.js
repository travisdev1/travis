$(document).ready(function () {
  /*
  Place the button inside input field
  */
  $("#id_fasid").after($("#search_fasid"))

  /*
  Making the input fields clear when the page reloads
  */
  $("#id_fasid").val('')
  $("#id_recipient_name").val('')
  $("#id_recipient_email").val('')

  $("#search_fasid").click(function () {

    let fasid = $('#id_fasid').val()
    $("#server-error").remove()

    if (fasid != '') {

      $("#id_recipient_name").attr("placeholder", "")
      $("#id_recipient_name").val('')
      $("#id_recipient_email").val('')
      $("#id_fasid").prop('disabled', true);
      $("#no-fas-id-error").remove()
      $("#server-error").remove()
      $("#div_id_fasid").after('<p class="searching-text">Searching for FAS Username.........</p>')

      email = $.get('/send/search', { fasid: fasid }, function (data) {

        if (data['server_error'] == 'True') {
          $("#id_fasid").val('')
          $('#server-error').remove()
          $('.searching-text').remove()
          $("#id_fasid").prop('disabled', false);
          $("#div_id_fasid").after('<p class="error" id="server-error" >Internal Server Error Occured! Enter Name and Email manually!</p>')
          $('#server-error').fadeIn('slow', function () {
            $('#server-error').delay(3000).fadeOut()
          })
        }
        else {
          $('.error').remove()
          $('.searching-text').remove()
          $("#id_fasid").prop('disabled', false);

          if (data['account_exists'] == 'Yes') {

            if (data['name'] == 'No name') {
              $("#id_recipient_name").attr("placeholder", "Privacy is Set! Type Name Manually")
            }

            else {
              $("#id_recipient_name").val(data['name'])
            }

            $("#id_recipient_email").val(data['email'])
          }
          else {
            $("#no-fas-id-error").remove()
            $("#div_id_fasid").after('<p class="error" id="no-fas-id-error">Sorry! No such FAS Username exist</p>')
            console.log('No such FAS username exsists')
            $('#no-fas-id-error').fadeIn('slow', function () {
              $('#no-fas-id-error').delay(2700).fadeOut()
            })
            $("#id_fasid").val('')
          }
          return data;
        }
      })
    }
  })
});
