function hideThisFunc()
{
    var p = document.getElementById("hidden");
    if(p.style.display === "block")
    {
        p.style.display = "none";
    }
    else
    {
        p.style.display = "block";
    }
}

function toggleSideBar()
{
    document.getElementById("sidebar").classList.toggle('active');
}