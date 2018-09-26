$(document).ready(
    function(){
      $("#nn_training_button").click(
        function(){
          $.ajax( { type:"GET",
                    url:"http://0.0.0.0:8000/train_neural_network",
                    //url:"{% static 'ajax_info.txt' %}",
                    //dataType:"text",
                    dataType:"json",
                    error: function() {
                      console.log("error");
                    },
                    beforeSend: function(){
                    },
                    success: function(result){

                    }
            });

        }
      );
    });
