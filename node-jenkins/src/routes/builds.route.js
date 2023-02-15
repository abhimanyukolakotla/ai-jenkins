const express = require('express');
const router = express.Router();
const buildsController = require('../controller/buildsController');

/* GET programming languages. */
router.get('/:job', buildsController.allBuilds);

module.exports = router;
