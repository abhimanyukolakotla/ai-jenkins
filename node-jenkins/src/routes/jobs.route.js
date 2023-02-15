const express = require('express');
const router = express.Router();
const jobsController = require('../controller/jobsController');

/* GET programming languages. */
router.get('/all', jobsController.allJobs);

module.exports = router;
