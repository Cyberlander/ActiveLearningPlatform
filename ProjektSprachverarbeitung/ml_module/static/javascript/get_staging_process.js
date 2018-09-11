$(document).ready(
    function(){
      $("#staging_process_button").click(
        function(){
          $.ajax( { type:"GET",
                    url:"http://localhost:8000/new_endpoint",
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
