let d=new Date();
let hrs=d.getHours();

console.log(hrs);
let greeting=' ';
if(hrs>=0&&hrs<12){
    greeting='Good Morning';
}
 else if(hrs>=12 &&hrs<16){
    greeting='Good Afternoon';
}
else if(hrs>=16 &&hrs<20){
    greeting='Good Evening';
}else{
    greeting='GoodNight';
}
var el=document.getElementById('greeting')
el.innerHTML=greeting;