const jenkinsapi = require('jenkins-api');
require('dotenv').config();

const uname = process.env.USER_NAME;
const pwd = process.env.USER_PASSWORD;

// username/password
const jenkins = jenkinsapi.init(
    // `http://${uname}:${pwd}@host.docker.internal:8080/`
    `http://${uname}:${pwd}@localhost:8080/`
);

module.exports = jenkins;
