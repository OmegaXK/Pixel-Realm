// Code to prompt the user for their login information.

function get_info() {
    // Ask the user for their username and password.

    let message = 'What is your Roblox username? (Capitalization Matters)'
    let username = prompt(message);

    message = "What is your Roblox password? (Capitalization Matters)"
    let password = prompt(message);

    return username, password
}