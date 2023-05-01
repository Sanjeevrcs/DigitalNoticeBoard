

var element_pos = 0;    // Position of the newly created elements.
    var iCnt = 0;
    let id = 0;
    $(document).ready(function() {

        
        $(function() { 
            $("#divResize").draggable().resizable()
         });
        
        $('#btClickMe').click(function() {

            var dynamic_div = $(document.createElement('div')).css({
                border: '1px dashed', position: 'absolute', left: element_pos, 
                top: $('#divResize').height() + 20,
                width: '120', height: '120', padding: '3', margin: '0'
            });
            dynamic_div.attr("id",'content'+id,'class','DragandRezise');
            id+=1
            element_pos = element_pos + $('#divContainer').width() + 140;
    
            $(dynamic_div).appendTo('.container-fluid').draggable().resizable();

            
            
            $(dynamic_div).dblclick(function() {
                alert( "Handler for .dblclick() called." );
                dynamic_div.remove()
              });
              $(dynamic_div).on("doubletap", function() {
                //doubletap stuff
                dynamic_div.remove()
            });

            iCnt = iCnt + 1;
        });
    });


    const getChildBtn = document.querySelector('#getChild')

    getChildBtn.addEventListener('click',()=>{
        console.log("cloning")
      

    console.log('child nodes of test2',test2.childNodes)
    let clone1 = test1.cloneNode(true);
    let clone2 = test2.cloneNode(true)
    console.log('clone =',clone1)
    document.body.appendChild(clone1)
    document.body.appendChild(clone2)
    
    let elements = {
        '1' : test1.childNodes,
        '2' : test2.childNodes
    }
    

    $.post('', elements, function(response){
        if(response === 'success')
        { 
            alert('Facial Image Successfully Sent!'); 
        }
        else{ 
            alert('Error Sending Facial Image!'); 
        }
    })

})
