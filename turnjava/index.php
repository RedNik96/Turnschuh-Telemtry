<?php

include("template/header.php");

?>
<div class="container">

        <div class="input-group mb-3" style="padding-top: 20px;">

                <div class="input-group-prepend">
                        <form action="{% url 'upload' %}" method="POST" enctype="multipart/form-data">
                        <input type="submit" value="submit" class="input-group-text" id="inputGroupFileAddon01">
                </div>
                <div class="custom-file">

                        <input type="file" class="custom-file-input" id="file" name="file"
                                aria-describedby="inputGroupFileAddon01">

                        <label class="custom-file-label" for="file">Choose file</label>
                        <input>
                        </form>

                </div>

        </div>
 



        <h3>Wählen Sie die gewünschten Dateien aus:</h3>

        <div class="container"
                style="border: 1px solid #ccc; background-color: #eee; margin: 5px 0 5px 0; border-radius: 5px; padding: 5px">
                <div class="row">
                        <div class="col-lg-4">

                                <div class="text-center">
                                        <img src="http://windows10portal.com/data/download-minecraft/thumbnail/thumbnail.png"
                                                class="media-object" style="width:80px">
                                </div>


                        </div>
                        <div class="col-lg-8">
                                <div class="form-group form-control-m">
                                        <label for="Name" value=""><b>Name:</b></label>
                                        <label for="Time" value=""><b>Datum:</b>
                                               <b>File:</b>
                                               </label>
                                </div>



                                <div class="btn-group mr-2" role="group" aria-label="Basic example"
                                        style="width: 100%; max-width: 500px;">
                                        <form action="" method="POST">
                                         
                                                <input type="hidden" name="down" id="down" value="{{id.path}}">
                                                <button type="submit" value="submit"
                                                        class="btn btn-secondary btn-xs">Download</button>

                                        </form>

                                        <form action="" method="" style="width: 100%;">
                                                <button type="button" class="btn btn-secondary " data-toggle="modal"
                                                        data-target="#exampleModal" data-whatever="@"
                                                        style="width: 100%; ">Send to
                                                        Agrirouter Datei:  </button>
                                        </form>

                                        <form action="" method="POST">
                                         
                                                <input type="hidden" name="delete" id="delete" value="">
                                                <button type="submit" value="submit"
                                                        class="btn btn-secondary btn-xs">Delete</button>
                                        </form>
                                </div>
                        </div>
                </div>
        </div>




        <p>No polls are available.</p>
     
</div>




<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog" role="document">
                <div class="modal-content">
                        <div class="modal-header">
                                <h5 class="modal-title" id="exampleModalLabel">New message</h5>
                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">&times;</span>
                                </button>
                        </div>
                        <div class="modal-body">
                                <form>
                                        <div class="form-group">
                                                <label for="recipient-name" class="col-form-label">Senden
                                                        erfolgreich !</label>
                                                <!-- <input type="text" class="form-control" id="recipient-name">-->
                                        </div>
                                </form>
                        </div>
                        <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                        </div>
                </div>
        </div>
</div>

<script>
        $('#exampleModal').on('show.bs.modal', function (event) {
                var button = $(event.relatedTarget) // Button that triggered the modal
                var recipient = button.data('whatever') // Extract info from data-* attributes
                // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
                // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
                var modal = $(this)
                modal.find('.modal-title').text('New message to ' + recipient)
                modal.find('.modal-body input').val(recipient)
        })


// Add the following code if you want the name of the file appear on select
$(".custom-file-input").on("change", function() {
  var fileName = $(this).val().split("\\").pop();
  $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
});
</script>



<?php

include("template/footer.php");

?>