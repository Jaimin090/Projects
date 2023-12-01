// Gets hostname, path and URL to webpage
let hostname = location.hostname;
let path = location.pathname;
let href = location.href;

console.log("Hostname is ", hostname);
console.log("Path is ", path);
console.log("URL is ", href);

// Navigates to another page
location.href = 'https://www.sait.ca';
