const jenkins = require('../services/jenkins-service');

const allJobs = (req, res) => {
    jenkins.all_jobs((err, data) => {
        if (err) {
            return res.json(err);
        }
        console.log(data);
        return res.json(data);
    });
};

module.exports = {
    allJobs,
};
