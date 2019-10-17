<!DOCTYPE html>
<html lang="en">
<head>
    <title>Turnschuh</title>
        <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <script src="js/files.js"></script>
</head>

<body>
    <nav class="navbar navbar-light bg-light">
        <a class="navbar-brand">Turnschuh</a>
     
        <a href="" class="btn btn-outline-success my-2 my-sm-0">Authorize & Onboard</a>

        <form class="form-inline" action="{% url 'logout' %}" method="GET">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Logout</button>
        </form>
  
            <form class="form-inline" action="{% url 'login' %}" method="POST">
                <input class="form-control mr-sm-2" type="text" placeholder="Username" name="username">
                <input class="form-control mr-sm-2" type="password" placeholder="Password" name="password">
                <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Login</button>
            </form>
   
      </nav>
    <div id="content">
      
        
    </div>

