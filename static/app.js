const d = document,
    $btn = d.querySelector("#btn"),
    $sideBar = d.querySelector(".sidebar"),
    $openBtn = d.getElementById("open"),
    $closeBtn = d.getElementById("close"),
    $modalContainer = d.getElementById("modal-container");

$btn.onclick = function () {
    $sideBar.classList.toggle("active")
}

$openBtn.addEventListener("click", () => {
    $modalContainer.classList.add("show");
});


$closeBtn.addEventListener("click", () => {
    $modalContainer.classList.remove("show");
});




