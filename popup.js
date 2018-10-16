var site;

//Set site variable equal to the current URL in the chrome URL field:
chrome.tabs.query({ 'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT },
    function(tabs) {
        site = tabs[0].url;
    }
)

//Add a listener to the filter button
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("go").addEventListener("click", clicked);
});

//function that gets called when the button gets clicked
function clicked() {
    var words = document.getElementById("filter_words").value;
    var swearwords = document.getElementById("swear_words").checked;
    document.write(swearwords);
}
