/*
Team Mileeon -- Mohammed Jamil, Isaac Jon, Emily Lee
SoftDev1 pd6
K#28 -- Sequential Progression
2018-12-19  
*/
var fibonacci=function(num){
    return fibhelp(num,0,1);
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
    if(a == 0)
	    return b;
    return gcd(b%a,a);
};

var students=['a','b','c','d','e','f','g'];

var randomStudent=function(){
    var num=Math.floor(Math.random() * students.length)
    return students[num];
};