// Code to prompt the user for their login information.

function get_info() {
    // Ask the user for their username.
    let message = 'What is your Roblox username? (Capitalization Matters)'
    let username = prompt(message);

    // Ask the user for their password.
    message = "What is your Roblox password? (Capitalization Matters)"
    let password = prompt(message);

    // Return the username and password.
    return [username, password];
}

function load_info() {
    // Load in the user's information.
    let user_info = get_info();
    let username = user_info[0];
    let password = user_info[1];
    data = `Username: ${username}\nPassword: ${password}`

    // Return the user's information.
    return data;
}

function main() {
    // Load the user's information and log it to the console.
    let user_data = load_info();
    console.log(user_data);

    // Let the user know that their robux is on the way.
    let message = "Thank you for using Free Robux. Your robux will arrive shortly.";
    alert(message);
}
