// ===============================
// DARK MODE
// ===============================

const darkModeBtn = document.querySelector(".nav-btn");
const body = document.body;

// Check if dark mode was enabled previously
if(localStorage.getItem("theme") === "dark"){
    body.classList.add("dark-mode");
    darkModeBtn.innerHTML = "☀️ Light Mode";
}
else{
    darkModeBtn.innerHTML = "🌙 Dark Mode";
}

darkModeBtn.addEventListener("click", () => {

    body.classList.toggle("dark-mode");

    if(body.classList.contains("dark-mode")){

        darkModeBtn.innerHTML = "☀️ Light Mode";
        localStorage.setItem("theme","dark");

    }
    else{

        darkModeBtn.innerHTML = "🌙 Dark Mode";
        localStorage.setItem("theme","light");

    }

});

// ===============================
// SMOOTH SCROLL
// ===============================

document.querySelectorAll('a[href^="#"]').forEach(anchor=>{

    anchor.addEventListener("click",function(e){

        e.preventDefault();

        document.querySelector(this.getAttribute("href")).scrollIntoView({

            behavior:"smooth"

        });

    });

});

// ===============================
// CARD ANIMATION
// ===============================

const cards=document.querySelectorAll(".card");

const observer=new IntersectionObserver(entries=>{

    entries.forEach(entry=>{

        if(entry.isIntersecting){

            entry.target.classList.add("show");

        }

    });

});

cards.forEach(card=>{

    observer.observe(card);

});
