/*
Team MoJo -- Mohammed Jamil, Isaac Jon
SoftDev1 pd6
K#29 -- Sequential Progression
2018-12-20  
*/
var result = document.getElementById('results');
var fibonacci=function(num){
    var fibnum= fibhelp(num,0,1);
    console.log(fibnum);
    result.innerHTML=fibnum;
    return fibnum;
};
var fibhelp=function(num,last,last2){
    if(num==0){
	    return last;
    }
    else if(num==1){
	    return last2;
    }
    else{
	    return fibhelp(num-1,last2,last+last2);
    }
}
var gcd=function(a,b){
    if(a == 0){
        console.log(b);
        result.innerHTML=b;
        return b;
    }
    return gcd(b%a,a);
};

var students=["George", "Bob", "Nina", "Elizabeth", "John", "Charlie"];

var randomStudent=function(){
    var num=Math.floor(Math.random() * students.length);
    var randomstu=students[num];
    console.log(randomstu);
    result.innerHTML=randomstu;
    return randomstu;
};

f = document.getElementById('fib');
g = document.getElementById('gcd');
r = document.getElementById('randStu');

var arg=Math.floor(Math.random() * 30);
f.innerHTML+=" (Argument : "+arg+")";

var gcdarg0=Math.floor(Math.random() * 1000);
var gcdarg1=Math.floor(Math.random() * 1000);

g.innerHTML+=" (Arguments : "+gcdarg0+", "+gcdarg1+")";

f.addEventListener('click',function(){fibonacci(arg)});
g.addEventListener('click',function(){gcd(gcdarg0,gcdarg1)});
r.addEventListener('click', randomStudent);
