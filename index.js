
var obj1;
fetch('data.json').then(response => response.json()).then(data => {
   
store(data.obj);
})

function store(obj){
    obj1=obj
}

function myFunction(obj) {
    var allDetalis=`name :${obj1["name"]} </br> age: ${obj1["age"]}  </br> salary :${obj1["Salary"]} </br> country:  ${obj1["Salary"]}`
    document.getElementById("demo").innerHTML = allDetalis;
} 

