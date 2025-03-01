*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Keywords ***


*** Test Cases ***
Log in wikipedia
    Open Browser   https://pl.wikipedia.org    chrome
    Click Element    id:pt-login-2
    Input Text   wpName1   Kamil
    Input text    wpPassword1    aaa
    Select Checkbox  wpRemember
    click element    wpLoginAttempt
    sleep   3
    Close Browser
