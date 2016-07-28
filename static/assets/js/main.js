// 主页面main.html JQuery begin
// 对于 AJAX 请求来说，基本上是不需要担心跨站的，所以 Tornado 1.1.1 以前的版本并不对带有 X-Requested-With:
// XMLHTTPRequest 的请求做验证。后来 Google 的工程师指出，恶意的浏览器插件可以伪造跨域 AJAX 请求，所以也应
// 该进行验证。对此我不置可否，因为浏览器插件的权限可以非常大，伪造 cookie 或是直接提交表单都行。
// 不过解决办法仍然要说，其实只要从 cookie 中获取 _xsrf 字段，然后在 AJAX 请求时加上这个参数，或者放在
// X-Xsrftoken 或 X-Csrftoken 请求头里即可。嫌麻烦的话，可以用 jQuery 的 $.ajaxSetup() 来处理：
/*$.ajaxSetup({
    beforeSend: function(jqXHR, settings) {
        type = settings.type
        if (type != 'GET' && type != 'HEAD' && type != 'OPTIONS') {
            var pattern = /(.+; *)?_xsrf *= *([^;" ]+)/;
            var xsrf = pattern.exec(document.cookie);
            if (xsrf) {
                jqXHR.setRequestHeader('X-Xsrftoken', xsrf[2]);
            }
        }
}});*/
$(document).on("pageinit","#page-main",function(){

    // 定时获取当前时间
    setTimeout(GetCurrentTime, 1000);

    //滚动广告
    var len = $(".num > li").length;
    var index = 0;  //图片序号
    var adTimer;
    $(".num li").mouseover(function() {
        index = $(".num li").index(this);  //获取鼠标悬浮 li 的index
        showImg(index);
    }).eq(0).mouseover();
    //滑入停止动画，滑出开始动画.
    $('#scrollPics').hover(function() {
        clearInterval(adTimer);
    }, function() {
        adTimer = setInterval(function() {
            showImg(index)
            index++;
            if (index == len) {       //最后一张图片之后，转到第一张
                index = 0;
            }
        }, 2000);
    }).trigger("mouseleave");
    function showImg(index) {
        var adHeight = $("#scrollPics>ul>li:first").height();
        $(".slider").stop(true, false).animate({
            "marginTop": -adHeight * index + "px"    //改变 marginTop 属性的值达到轮播的效果
        }, 500);
        $(".num li").removeClass("on")
            .eq(index).addClass("on");
    }
});
//获取当前时间的函数
function GetCurrentTime()
{
    var date = new Date();
    var seperator1 = "-";
    var seperator2 = ":";
    var month = date.getMonth() + 1;
    var strDate = date.getDate();
    if (month >= 1 && month <= 9) {
        month = "0" + month;
    }
    if (strDate >= 0 && strDate <= 9) {
        strDate = "0" + strDate;
    }
    var currentdate = date.getFullYear() + seperator1 + month + seperator1 + strDate
            + " " + date.getHours() + seperator2 + date.getMinutes()
            + seperator2 + date.getSeconds();
    $("#current_time").text(currentdate);
    setTimeout(GetCurrentTime, 1000);
}
// 主页面end


// 登录页面login JQuery begin
$(document).on("pageinit","#page-login",function(){
    $("#fname").blur(checkuserNameforlogin);
    $("#fpassword").blur(checkpassWordforlogin);
    $("#login-commit").click(function()
    {
    var bUserName = checkuserNameforlogin();
    var bPassWord = checkpassWordforlogin();
    return bUserName&&bPassWord;
    })
});

// 登录页面用户校验
function checkuserNameforlogin()
{
    var userNameValue = $("#fname").val();
    var usernameRegex = /^[\u4E00-\u9FA5\uF900-\uFA2D\w]{0,15}$/;
    var msg ="<img src='static/images/right1.jpg' width='60px' height=40px'>";
    if(userNameValue == null || userNameValue == "")
    {
        msg = "姓名:";
        msg +="<font color='red'>用户名必须填写!</font>";
    }
    else if(!usernameRegex.test(userNameValue))
    {
        msg = "姓名:";
        msg +="<font color='red'>用户名格式不正确</font>";
    }
    $("#usernameSpan").html(msg);
    return msg == "<img src='static/images/right1.jpg' width='60px' height=40px'>";
}
// 登录页面密码校验
function checkpassWordforlogin()
{
    var password = $("#fpassword").val();
    var passwordRegex = /^[!@#$%^&*()\w]{0,15}$/;
    var msg ="<img src='static/images/right1.jpg' width='60px' height=40px'>";
    if(password == null || password == "")
    {
        msg = "密码:"
        msg += "<font color='red'>请输入登录密码!</font>";
    }
    else if(!passwordRegex.test(password))
    {
        msg = "密码:"
        msg +="<font color='red'>密码格式不正确</font>";
    }
    $("#passwordSpan").html(msg);
    return msg == "<img src='static/images/right1.jpg' width='60px' height=40px'>";
}
// 登录页面 login end



//注册页面JQuery
$(document).on("pageinit","#page-register",function(){
    // 注册信息校验
    $("#fname").blur(checkuserName);
    $("#fpassword").blur(checkpassWord);
    $("#frepassword").blur(checkrepassWord);
    $("#register-commit").click(function()
    {
    var bUserName = checkuserName();
    var bPassWord = checkpassWord();
    var bRePassWord = checkrepassWord();
    return bUserName&&bPassWord&&bRePassWord;
    })
});

/*注册页面用户名校验*/
function checkuserName()
{
    // 首先检查用户名格式
    var userNameValue = $("#fname").val();
    var usernameRegex = /^[\u4E00-\u9FA5\uF900-\uFA2D\w]{0,15}$/;
    var msg ="<img src='static/images/right1.jpg' width='60px' height=40px'>";
    if(userNameValue == null || userNameValue == "")
    {
        msg = "姓名:";
        msg +="<font color='red'>用户名必须填写!</font>";
    }
    else if(!usernameRegex.test(userNameValue))
    {
        msg = "姓名:";
        msg +="<font color='red'>用户名格式不正确</font>";
    }
   // $("#usernameSpan").html(msg);
   // return msg == "<img src='static/images/right1.jpg' width='60px' height=40px'>";
    // 从status.html页面get数据,动态检查用户名是否使用
    jQuery.getJSON('//localhost:8009/status',{"username":userNameValue},function(data)
            {
                $('#msg').html(data['msg']);
                Message = data['msg'];
                // 没有报错,说明可用
                if(Message == "")
                {
                $("#usernameSpan").html(msg);
                $('#msg').html("该用户名可用!");
                $(".register-legend").html("<img src='/static/images/register.jpg' width = '100px' height = '80px'>");
                }else
                {
                msg = "<font color='red'>"+Message +"</font>";
                $("#usernameSpan").html(msg);
                $(".register-legend").html("<img src='/static/images/already.jpg' width = '100px' height = '80px'>");
                }
            }
     );

     return msg == "<img src='static/images/right1.jpg' width='60px' height=40px'>";
}
function CheckNameOther()
{
    var userNameValue = $("#fname").val();
    var usernameRegex = /^[\u4E00-\u9FA5\uF900-\uFA2D\w]{0,15}$/;
    var msg ="<img src='static/images/right1.jpg' width='60px' height=40px'>";
    if(userNameValue == null || userNameValue == "")
    {
        msg = "姓名:";
        msg +="<font color='red'>用户名必须填写!</font>";
    }
    else if(!usernameRegex.test(userNameValue))
    {
        msg = "姓名:";
        msg +="<font color='red'>用户名格式不正确</font>";
    }
    $("#usernameSpan").html(msg);
    return msg == "<img src='static/images/right1.jpg' width='60px' height=40px'>";
}

/* 密码校验 */
function checkpassWord()
{
    var password = $("#fpassword").val();
    var passwordRegex = /^[!@#$%^&*()\w]{0,15}$/;
    var msg ="<img src='static/images/right1.jpg' width='60px' height=40px'>";
    if(password == null || password == "")
    {
        msg = "密码:"
        msg += "<font color='red'>密码必须设置!</font>";
    }
    else if(!passwordRegex.test(password))
    {
        msg = "密码:"
        msg +="<font color='red'>密码格式不正确</font>";
    }
    $("#passwordSpan").html(msg);
    return msg == "<img src='static/images/right1.jpg' width='60px' height=40px'>";
}

/*密码重复校验*/
function checkrepassWord()
{
    var repassword = $("#frepassword").val();
    var password = $("#fpassword").val();
    //var repasswordRegex = /^[!@#$%^&*()\w]{0,15}$/;
    var msg ="<img src='static/images/right1.jpg' width='60px' height=40px'>";
    if(repassword == null || repassword == "")
    msg = "再次输入密码:"+"<font color='red'>请再次输入密码!</font>";
    else if(repassword != password)
    msg = "<font color='red'>再次输入密码:密码不一致!</font>";
    $("#repasswordSpan").html(msg);
    return msg == "<img src='static/images/right1.jpg' width='60px' height=40px'>";
}