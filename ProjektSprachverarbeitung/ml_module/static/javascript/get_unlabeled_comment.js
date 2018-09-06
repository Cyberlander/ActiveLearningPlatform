
$(document).ready(
    function(){
      $("#good_button").click(
        function(){
          showSaveLabel( true );
          currentLabelNumerical = 2;
          document.getElementById('comment_panel').className = 'panel';
          document.getElementById('comment_panel').classList.add('panel-success');
        }
      );
});
$(document).ready(
    function(){
      $("#neutral_button").click(
        function(){
          showSaveLabel( true );
          currentLabelNumerical = 1;
          document.getElementById('comment_panel').className = 'panel';
          document.getElementById('comment_panel').classList.add('panel-warning');
        }
      );
  });
$(document).ready(
    function(){
      $("#bad_button").click(
        function(){
          showSaveLabel( true );
          currentLabelNumerical = 0;
          document.getElementById('comment_panel').className = 'panel';
          document.getElementById('comment_panel').classList.add('panel-danger');
        }
      );
  });
$(document).ready(
    function(){
      $("#comment_button").click(
        function(){
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
                    console.log(result)
                    console.log( typeof result )
                    console.log( result.Message )
                    console.log( myGlobalVar )
                    $("#panel_content").html(result.Message);
                    currentId = result.Id
                    currentComment = result.Message;
                    predicteted_nn_negative = result.predicteted_nn_negative
                    predicteted_nn_neutral = result.predicteted_nn_neutral
                    predicteted_nn_positive = result.predicteted_nn_positive
                    nn_says = "Negative: " + predicteted_nn_negative + " Neutral: " + predicteted_nn_neutral + " Positive: " + predicteted_nn_positive
                    currentLabelMachine = label_dict[result.Predicted]
                    //computer_says = "Computer says <strong>" + result.Predicted + "</strong>"
                    //$("#classification_guess").html( computer_says )

                    $("#neural_network_prediction").html( nn_says )

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
