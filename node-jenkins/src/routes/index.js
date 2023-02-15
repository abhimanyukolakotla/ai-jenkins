const express = require('express');
const jobRoute = require('./jobs.route');
const buildRoute = require('./builds.route');
const router = express.Router();

/* JOBS */
router.use('/job', jobRoute);

/* BUILDS */
router.use('/build', buildRoute);

module.exports = router;
