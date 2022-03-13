
var base_url = window.location.href
var state = document.getElementById("state")
var city_tag = document.getElementById("city")
var pincode_tag = document.getElementById("pincode")
var submit_btn = document.getElementById("submit")

state.onchange = function(){
    fetch(base_url+"city/"+state.value).then(function(resp){
        resp.json().then(function(data){
            if (city_tag.childElementCount != 0){
                while(city_tag.firstChild){
                    city_tag.removeChild(city_tag.firstChild)
                }
               
            }
            for(let city in data.cities){
                
                var option = document.createElement('option')
                option.value = data.cities[city]
                option.innerText = data.cities[city]
                city_tag.append(option) 

            }
        })
    })
}

city_tag.onchange = function(){
    
    fetch(base_url+"pincode/"+state.value+'/'+city_tag.value).then(function(resp){
        resp.json().then(function(data){
            
            if (pincode_tag.childElementCount != 0){
                
                while(pincode_tag.firstChild){
                    pincode_tag.removeChild(pincode_tag.firstChild)
                }
                
            }
            for(let pincode in data.pincodes){
               
                var option = document.createElement('option')
                option.value = data.pincodes[pincode]
                option.innerText = data.pincodes[pincode]
                
                pincode_tag.append(option)
            }
        })
    })
}

submit_btn.onclick = function(event){
    event.preventDefault()
    var name = document.getElementById("name")
    var pincode_tag = document.getElementById("pincode")
    fetch(base_url+"saveuser",{
    method:"POST",
    body:JSON.stringify({
        name:name.value,
        state:state.value,
        city :city.value,
        pin:pincode_tag.value
    }),
    headers:{
        "Content-type":"application/json ; charset=UTF-8"
    }
}).then(response=>response.json())
.then(function(data){
   
    var toast_body = document.getElementById('toast-body');
    var toast_status = document.getElementById('status')
    if(data.status){
        toast_status.innerText = "Success";
        toast_body.innerText = data.msg
        $('.toast').toast('show');
        setTimeout(function(){
            window.location.href = base_url

        },2000)
    }
    else{
        toast_status.innerText = "Error";
        tost_body.innerText = data.msg
        $('.toast').toast('show');
    }
    
})
}