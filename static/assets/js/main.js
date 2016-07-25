// 主页面JQuery
$(document).on("pageinit","#page-main",function(){
//setTimeout(requestInventory, 2000);
});

/*function requestInventory()
{
    setTimeout(requestInventory, 2000);
    var mydate = new Date();
    var t=mydate.toLocaleString();
    alert(1);
    jQuery.ajax({url: '//localhost:8003/',
                    type: 'POST',
                    data: {
                        time:t
                    },
                error: function(XMLHttpRequest, textStatus, errorThrown)
                {
                 alert(XMLHttpRequest.status);
                 alert(XMLHttpRequest.readyState);
                 alert(textStatus);
                },
                success: function(data, status, xhr) {
                    alert("succes");
                }
        );
}*/
// 登录页面JQuery
$(document).on("pageinit","#page-proanaly",function(){
    $("a").click(function()
    {
    var text = $(this).text();
    $("#name").text(text);
    }
)
});

// 登录页面JQuery
$(document).on("pageinit","#page-login",function(){
    $("#fname").blur(checkuserName);
    $("#fpassword").blur(checkpassWord);
    $("#login-commit").click(function()
    {
    var bUserName = checkuserName();
    var bPassWord = checkpassWord();
    return bUserName&&bPassWord;
    })
});
//注册页面JQuery
$(document).on("pageinit","#page-register",function(){
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
    return msg == "密码格式正确";
}

/*密码重复校验*/
function checkrepassWord()
{
var repassword = $("#frepassword").val();
var password = $("#fpassword").val();
//var repasswordRegex = /^[!@#$%^&*()\w]{0,15}$/;
var msg ="两次密码一样!";
if(repassword == null || repassword == "")
msg = "<font color='red'>请再次输入密码!</font>";
else if(repassword != password)
msg = "<font color='red'>密码不一致!</font>";
$("#repasswordSpan").html(msg);
return msg == "两次密码一样!";
}