var site;
chrome.tabs.query({ 'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT },
    function(tabs) {
        site = tabs[0].url;
    }
)
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("go").addEventListener("click", clicked);
});
function clicked() {
    document.write(site);
}
