{% extends "base.tpl" %}
{% block content %}
<form method="post"{% ifequal msg "Logged out." %} action="/"{% endifequal %}>
<center>
<p>{{ msg }}</p>
<table cellspacing="0" cellpadding="0" class="black">
<tr>
<td>
<table cellspacing="1" cellpadding="3">
    <tr class="datahigh">
        <th colspan="2">Login</th>
    </tr>
    <tr class="header">
        <th>Username:</th>
        <td><input type="text" name="username" size="16"/></td>
    </tr>
    <tr class="header">
        <th>Password:</th>
        <td><input type="password" name="password" size="16"/></td>
    </tr>
    <tr class="header">
        <th colspan="2"><input type="submit" value="Login"/></th>
    </tr>
</table>
</td>
</tr>
</table>
</center>
</form>
{% endblock %}
