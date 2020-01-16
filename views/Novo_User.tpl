<!DOCTYPE html>
<html>
<head>
	<title>Cadastro</title>
	<link rel="stylesheet" type="text/css" href="/css/reset.css">
	<link rel="stylesheet" type="text/css" href="/css/Style_Login.css">
	<style type="text/css">
		body{
			background-image: url("../../static/architectural-design-architecture-blue-416998.jpg");
			background-size: cover;
			font-family: sans-serif;
			font-size: 30px;
		}
		form{
			justify-content: center;
			align-items:center;
			display: flex;
			flex-direction: column;
			text-align: center
			top: 40%;
		}
		a{
			justify-content: center;
			align-items:center;
			display: flex;
			flex-direction: column;
			text-align: center
			top:40%;
		}
		input{
			margin: 15px;
		}
		.login-container{
			border: black solid 1px;
			background-color: rgba(255,155,0,0.3);
			justify-content: center;
			align-items:center;
			display: flex;
			flex-direction: column;
			width: 350px;
			padding-top: 100px;
			padding-bottom: 150px;

		}

		.container{
			display: flex;
			justify-content: center;
			align-items: center;
			height: 80vh;
		}
	</style>
</head>
<body>
	<div class="container">
		<div class="login-container">
			<form method='POST' action='/cadastro/'>
				<input type="text" name="novo_nome" placeholder="NOME">
				<input type="text" name="novo_user" placeholder="USERNAME">
				<input type="password" name="novo_pass" placeholder="SENHA">
				<input type="submit" value="Cadastrar">
			</form>
		</div>
	</div>
</body>
</html>