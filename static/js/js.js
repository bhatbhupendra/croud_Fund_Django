let element = document.getElementById("id_name");
let target = document.getElementById("textChanging");

element.addEventListener("input",function(){
    let value = id_name.value;
    if (value){
        value = "Hi! " + value + ". Please note down Data that you Filled.";
        target.innerHTML = value;     
    }else{
        target.innerHTML="Place Order"
    }
    
});

