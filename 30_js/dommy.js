/*
    Changes the heading of the html file to the given argument e
*/
var changeHeading = function(e) {
    var h = document.getElementById("h")
    h.innerHTML = e
};


var addItem = function(e) {
    // Create a list element with the desired contents
    var list = document.getElementById("thelist");
    var item = document.createElement("li");
    item.innerHTML="WORD";
    
    // Add all the required event listeners to the list element
    item.addEventListener('mouseover',function(e){
    console.log(e);
    changeHeading(this.innerHTML);});
    item.addEventListener('mouseout', function(e){
    console.log(e);
    changeHeading("Hello World!")});
    item.addEventListener('click', function(e){
    console.log(e);
    this.remove()});

    // Make the list element a child of the list
    list.appendChild(item);
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var lis = document.getElementsByTagName("li");

for(var i=0; i < lis.length; i++) {
    //This eventlistener causes the heading to change when the cursor is hovered over a list element to the text of that list element 
    lis[i].addEventListener('mouseover',function(e){
	console.log(e);
    changeHeading(this.innerHTML);});

    //This eventlistener causes the heading to change back to the original heading when the cursor is not over any list element
    lis[i].addEventListener('mouseout', function(e){
	console.log(e);
    changeHeading("Hello World!")});

    //This eventlistener causes a list element to be removed when clicked
    lis[i].addEventListener('click', function(e){
	console.log(e);
	this.remove()});
};

var fib = function(n) {
    if(n == 0){
        return 0;
    }
    if(n == 1){
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
};
var fib2 = (n) => {
    
    var window = [0, 1];
    if(n < 2){
        return window[n];
    }else{
        var count =0;
        while(count<n){
            sum = window[0] + window[1];
            window[0] = window[1];
            window[1]=sum;
            count++;
        }
        return window[0];
    }
}

/*
    The addFib function adds a list element with the corresponding fibonacci number to the fiblist
*/
var count=0;
var addFib = function(e){
    console.log(e);
    var list=document.createElement("li");
    var num=document.createTextNode(fib(count));
    list.appendChild(num);
    count++;
    document.getElementById("fiblist").appendChild(list);
};

var addFib2 = function(e){
    console.log(e);
    var list=document.createElement("li");
    var num=document.createTextNode(fib2(count));
    list.appendChild(num);
    count++;
    document.getElementById("fiblist").appendChild(list);
};
// attaches the addFib function to the button fb
var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
var fb = document.getElementById("fb2");
fb.addEventListener("click", addFib2);