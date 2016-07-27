// 主页面main.html JQuery begin
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
    var msg ="姓名:格式正确";
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
    return msg == "姓名:格式正确";;
}
// 登录页面密码校验
function checkpassWordforlogin()
{
    var password = $("#fpassword").val();
    var passwordRegex = /^[!@#$%^&*()\w]{0,15}$/;
    var msg ="密码:格式正确";
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
    return msg == "密码:格式正确";
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

/*用户名校验*/
function checkuserName()
{
    var userNameValue = $("#fname").val();
    // 从status.html页面get数据,动态检查用户名是否使用
    jQuery.getJSON('//localhost:8009/status',{"username":userNameValue},function(data)
            {
                $('#msg').html(data['msg']);
                Message = data['msg'];
                // 没有检查到错误,更新页面提示信息
                if(Message == "")
                {
                $("#usernameSpan").html("姓名:");
                $('#msg').html("欢迎注册!");
                CheckNameOther()
                }else
                {
                Message = "<font color='red'>"+Message +"</font>";
                $("#usernameSpan").html(Message);
                }
            }
     );
}
function CheckNameOther()
{
    var userNameValue = $("#fname").val();
    var usernameRegex = /^[\u4E00-\u9FA5\uF900-\uFA2D\w]{0,15}$/;
    var msg ="姓名:格式正确";
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
    return msg == "姓名:格式正确";;
}

/* 密码校验 */
function checkpassWord()
{
    var password = $("#fpassword").val();
    var passwordRegex = /^[!@#$%^&*()\w]{0,15}$/;
    var msg ="密码格式正确";
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
    return msg == "密码:格式正确";
}

/*密码重复校验*/
function checkrepassWord()
{
var repassword = $("#frepassword").val();
var password = $("#fpassword").val();
//var repasswordRegex = /^[!@#$%^&*()\w]{0,15}$/;
var msg ="再次输入密码:OK";
if(repassword == null || repassword == "")
msg = "再次输入密码:"+"<font color='red'>请再次输入密码!</font>";
else if(repassword != password)
msg = "<font color='red'>再次输入密码:密码不一致!</font>";
$("#repasswordSpan").html(msg);
return msg == "再次输入密码:OK";
}