var Body = {
  setcolor : function(color){
    document.querySelector('body').style.color = color;
  },
  setBackgroundColor : function(color){
    document.querySelector('body').style.backgroundColor = color;
  }
}
var Link = {
  setcolor : function(color){

    /*Jquery로 표현하면 아래 반복문 자체를 한 명령어로 표현할 수 있다.*/
    $('a').css('color', color);
    /*
    var alist = document.querySelectorAll('a');
    var cnt = 0;
    while(cnt < alist.length){
      alist[cnt].style.color = color;
      cnt = cnt + 1;
    }
    */
  }

}
function DaynightHandler(){
  if(self.value === 'night'){
    Body.setcolor('white');
    Body.setBackgroundColor('black');
    self.value = 'day';
    Link.setcolor('powderblue');
  }
  else{
    Body.setcolor('black');
    Body.setBackgroundColor('white');
    self.value = 'night';
    Link.setcolor('blue');
  }
}
