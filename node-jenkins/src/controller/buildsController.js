const jenkins = require('../services/jenkins-service');

const allBuilds = (req, res) => {
    const reqJob = req.params.job;

    jenkins.all_builds(reqJob, function (err, data) {
        if (err) {
            return res.json(err);
        }
        return res.json(data);
    });
};

module.exports = {
    allBuilds,
};
