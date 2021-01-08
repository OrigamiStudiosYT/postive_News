/* ******************************************************************************
    *
    *   Program: Java.js
    *
    *   Description: Handles the Javascript for the page
    *
    *   Author:  Andrew Lortie
    *
    *   Date: 1/8/2021
    *
    *   History: 1/8/2021 Creation
    *
    ****************************************************************************** */
   /* ******************************************************************************
    *
    *   Module: Mobile switching 
    *
    *   Description: When the user is on mobile this switches them to the mobile version
    *
    *   Author:  Andrew Lortie
    *
    *   Date: 1/8/2021
    *
    *   History: 1/8/2021 Creation
    *
    ****************************************************************************** */
function screenwidth()
{
    if (screen.width <= 699) 
    {
        var url= window.location.pathname;
        if (typeof url !== 'undefined' && url)
        {
            document.location = "m_index.html";
        }
        else
        {
            document.location = "m_"+url.substring(url.lastIndexOf("/")+1);
        }
        
    }
}
function screenwidthdt()
{
    if (screen.width >= 699) 
    {
    var url= window.location.pathname;
    document.location = url.substring(url.lastIndexOf("/m_")+3);
    }
}