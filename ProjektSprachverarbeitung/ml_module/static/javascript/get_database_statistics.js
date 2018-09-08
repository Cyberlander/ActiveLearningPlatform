$(document).ready(
    function(){
      $("#database_statistics_link").click(
        function(){
          $.ajax( { type:"GET",
                    url:"http://localhost:8000/get_database_statistics",
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
                      $("#count_unlabeled_comments").html( " Unlabeled comments: " + result.count_unlabeled_comments )
                      $("#count_labeled_comments").html( "Labeled commments: " + result.count_labeled_comments )
                     $("#count_staging_comments").html( "Comments in staging: " + result.count_staging_area )


              }
            });
        }
      );
    });
