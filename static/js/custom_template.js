var element_pos = 0;    // Position of the newly created elements.
    var iCnt = 0;
    let id = 1;
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

            $('<select name="typedata" id="typedata"><option value="null">none</option> <option value="video">video</option> <option value="image">image</option> <option value="text">text</option></select>').appendTo(dynamic_div)
    
            if($(dynamic_div).appendTo('.container').draggable().resizable())
            {
              console.log("successfully added")
            };
            console.log('elements top',$(dynamic_div).offsetTop)
            
            
            $(dynamic_div).dblclick(function() {
                // alert( "Handler for .dblclick() called." );
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
        console.log('working')
        console.log("cloning")
    let test1 = document.getElementById('test')
    // let test2 = document.getElementById('divResize')
    
    let i=0
    let data = '&&&'
    let contentData = {}
    let id = ''
    // let value = ''
    
    test1.childNodes.forEach(element => {
        if($(element).children().find(":selected").val()!=undefined){
            let select = $(element).children()
            let selected_val = select.find(":selected").val()
            console.log('selected value is ',selected_val)
            $(element).children().remove()
            console.log('element-',i,typeof( element.outerHTML))
            id = $(element).attr('id')
            // id = JSON.stringify(id)
            // selected_val = JSON.stringify(selected_val)
            console.log(id)
            contentData[id] = selected_val
            
            data += element.outerHTML
            console.log($(element).attr('id'),selected_val)
            if(i < test1.childNodes.length-1){
              data += '&&&'
            }  
            console.log(contentData)
        }
 
    });                       
    console.log('contentData',contentData);

    let input1 = document.getElementById('inputfield')
    input1.value = data
    let input2 = document.getElementById('inputfield2')
    input2.value = JSON.stringify(contentData)
    console.log('input value1 is  ',input1.value,'input value2 = ',contentData)
    document.getElementById("myform").submit();
  
    
    

    
})
