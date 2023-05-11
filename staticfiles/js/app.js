window.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.querySelector(".sidebar"),
        sidebarBtn = document.querySelector(".bar_btn"),
        loader = document.querySelector(".loader"),
        main = document.querySelector(".main"),
        success = document.querySelector(".success");
    loader.addEventListener("transitioned", () => {
        document.body.removeChild("loader")
    })
    loader.classList.add("hidden")
    sidebarBtn.addEventListener("click", () => {
        sidebar.classList.toggle("close")
        sidebarBtn.classList.toggle("close")
        main.classList.toggle("close")
    })
    success.classList.add("show")
})