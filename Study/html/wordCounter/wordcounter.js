// very basic study of web browser js 
// 1. ���� ����������  ��� �ؽ�Ʈ����
let words = document.getElementsByTagName('body')[0].innerText;
// 3. �ܾ���� �ɰ� �� 
let splitedwords = words.split(' ');
// 4. ���� Ƚ���� ����ϰ� 
let counterword = {};
for(let i=0; i<splitedwords.length; i++){
    if(counterword[splitedwords[i]] === undefined){ //if it's first time to be found -> assign 1
        counterword[splitedwords[i]] = 1;
    }
    else{ // else we can add one 
        counterword[splitedwords[i]] += 1;
    }
}
// array has a space which is labeled by index order. 
// object is lableled by property name.
// 5. change obj to array form to place in oreder.
/*
arr.sort((a,b)=>{ // in alphabetic order 
    if(a>b){return 1;}
    else{return -1;}
})
*/
const orederdlist = [];
for (let name in counterword){
    orederdlist.push([name, counterword[name]])
}
orederdlist.sort((a,b)=>{
    if(a[1]>b[1]){return 1;}
    else{return -1;}
})
// 6. �ܼ�â�� ����Ѵ�. 
let str = '';
for(let i=0; i<orederdlist.length; i++){
    str += (orederdlist[i][0] +' : '+ orederdlist[i][1]+ '\n');
}
alert(str)
// Use the bookmarklet-