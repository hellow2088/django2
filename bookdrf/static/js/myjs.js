function pt(){
    var p1 = document.getElementById('p1');
    console.log(p1);
    p1.value='123';
}

function getpt(){
    var p2 = document.getElementById('p2');
    var diqu = document.getElementById('diqu')
    // console.log(p2.value);
    console.log(diqu.value)

    if (diqu.value=='1'){
        p2.value = '北京';
    }
    if (diqu.value=='2'){
        p2.value='上海';
    }
}

function cgdiqu(){
    var diqu = document.getElementById('diqu');
    console.log(diqu.value);
}

function setkeyword() {
   var kd = document.getElementById('keyword');
    console.log(123);

    kd.value='Book';
}

function ck() {
    var b = document.getElementById('p1');
    p1.value='124';
}


function setLoginForm(){
    var username = document.getElementById('id_username');
    var pwd = document.getElementById('id_password');
    username.setAttribute('class','form-control');
    pwd.setAttribute('class','form-control');
}


// function getNewImageCode(){
//     var src = document.getElementById('imageCode');
//     console.log(src)
//     // src = src.src+'?';
//     src = 'www.baidu.com';
//     console.log(src);
//     src.setAttribute('src',src);
// }

    // $('#imageCode').click(function (){
    //     $(this)[0].src+='?';
    // })