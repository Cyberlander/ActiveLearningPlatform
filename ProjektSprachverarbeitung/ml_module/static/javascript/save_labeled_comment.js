$(document).ready(
  function(){
$("#label_button").click(
        function(){


          $.post("http://0.0.0.0:8000/send_comment_label",
          {
            id: currentId,
            comment: currentComment,
            label_user: currentLabelNumerical
          },
          function(data, status){
            alert(label_user)
          });


          showSaveLabel( false );
          document.getElementById('comment_panel').className = 'panel';
          document.getElementById('comment_panel').classList.add('panel-primary');
          $.ajax( { type:"GET",
                    url:"http://localhost:8000/get_unlabeled_comment",
                    //url:"{% static 'ajax_info.txt' %}",
                    //dataType:"text",
                    dataType:"json",
                    error: function() {
                      console.log("error");
                    },
                    beforeSend: function(){
                      // Show image container
                      $("#panel_content").html("Loading");
                    },
                    success: function(result){
                      $("#panel_content").html(result.Message);
                      currentId = result.Id
                      currentComment = result.Message;
                      currentLabelMachine = label_dict[result.Predicted];
                      computer_says = "Computer says <strong>" + result.Predicted + "</strong>"
                      $("#classification_guess").html( computer_says )


                      $("#neural_network_prediction").html( result.Predicted )

                      var alert_class = "alert-info"
                      //change the color of the alert
                      if ( result.Predicted == "negative" ){
                        alert_class = "alert-danger"
                      }
                      else if ( result.Predicted == "neutral" ){
                        alert_class = "alert-warning"
                      }
                      else if ( result.Predicted == "positive" ){
                        alert_class = "alert-success"
                      }
                      document.getElementById('classification_guess').className = 'alert';
                      document.getElementById('classification_guess').classList.add( alert_class );
              }
            });
        }
);
});
