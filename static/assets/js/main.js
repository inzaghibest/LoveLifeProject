// 主页面JQuery
$(document).on("pageinit","#page-main",function(){
});
// 登录页面JQuery
$(document).on("pageinit","#page-login",function(){
alert("1");
    $("#fname").blur(checkuserName);
    $("#fpassword").blur(checkpassWord);
    $("#login-commit").click(function()
    {
    var bUserName = checkuserName();
    var bPassWord = checkpassWord();
    return bUserName&&bPassWord;
    })
});
function checkuserName()
{
    var userNameValue = $("#fname").val();
    var usernameRegex = /^[\u4E00-\u9FA5\uF900-\uFA2D\w]{0,15}$/;
    var msg ="right";
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
    return msg == "right";
}
function checkpassWord()
{
    var password = $("#fpassword").val();
    var passwordRegex = /^[!@#$%^&*()\w]{0,15}$/;
    var msg ="right";
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
    return msg == "right";
}