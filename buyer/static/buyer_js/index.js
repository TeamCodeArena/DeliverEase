let mobileView;
let closeMenu;

try {
    main(document)
}

catch(err) {
    const jsdom = require('jsdom');
    const { JSDOM } = jsdom
    
    const dom = new JSDOM(`
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>index page</title>
        <link rel="stylesheet" href="{% static  'main/style.css'%}">
        <link rel="stylesheet" href="{% static  'main/Navbar.css'%}">
        <link rel="stylesheet" href="{% static  'main/indexcontainer.css'%}">
        <style>
            img{
                padding: 80px;
                width: 300px;
                height: 400px;
            }
        </style>
    </head>
    <body>
        <div class="App">
    
            
    
            <header class="header">
                <nav class="navbar">
                    <h2> DeliverEase</h2>
                    <ul class="nav-menu">
                        <li class="nav-item">
                            <a href="{% url "global_index" %}" class="nav-link">Home</a>
                        </li>
                        <li class="nav-item">
                            <a href="/about_us" class="nav-link">About Us</a>
                        </li>
                        <li class="nav-item">
    <!--                         <a href="#" class="btn">My Orders</a> -->
                          <a href='/auth/login'  ><button  class="btn"> Login</button></a>
                        </li>
                    </ul>
                    <div class="hamburger">
                        <span class="bar"></span>
                        <span class="bar"></span>
                        <span class="bar"></span>
                    </div>
                </nav>
            </header>
    
            <div class='container'>
                <h1> Empowering Delivery Partners,<br/>Connecting Communities!</h1>
          
                <div class='containerLower'>
          
                  <div class='left'>
                          <p> New User ?</p>
                      <a href="/get_started"> <button class='btn'> Get started</button> </a>
                      
                      <a href="/about_us"><button class='btn'> Who we are</button></a>
                  </div>
          
                  <div class='right'>
                      <img src="{% static "media/homepage.jpg" %}" alt="homepageimg"  />
                  </div>
          
                </div>
            </div>
                
           
           
        </div>
        <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
        <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
    
        <script src="{% static "main_js/index.js" %}"></script>
        
    </body>
    </html>`)
    main(dom.window.document)
    module.exports = [mobileView, closeMenu]
}





function main(dom) {

    mobileView = function(DOM) {

        try {
            const hamburger = DOM.querySelector(".hamburger");
            const navMenu = DOM.querySelector(".nav-menu");
            const navLink = DOM.querySelectorAll(".nav-link");
            hamburger.classList.toggle("active");
            navMenu.classList.toggle("active");
            return true;
        }

        catch(err) {
            return false;
        };
    }

    closeMenu = function(DOM) {

        try {
            const hamburger = DOM.querySelector(".hamburger");
            const navMenu = DOM.querySelector(".nav-menu");
            const navLink = DOM.querySelectorAll(".nav-link");
            hamburger.classList.remove("active");
            navMenu.classList.remove("active");
            return true;
        }

        catch(err) {
            return false;
        };
    }


    const hamburger = dom.querySelector(".hamburger");
    const navMenu = dom.querySelector(".nav-menu");
    const navLink = dom.querySelectorAll(".nav-link");

    hamburger.addEventListener("click", mobileView);
    navLink.forEach(n => n.addEventListener("click", closeMenu));
    
}
