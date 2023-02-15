const express = require('express');
const bodyParser = require('body-parser');
const router = require('./src/routes');

const app = express();

app.use(bodyParser.urlencoded({ extended: false }));

app.get('/', async (req, res) => {
    res.json({ message: 'ok' });
});

app.use('/v1', router);

/* Error handler middleware */
app.use((err, req, res, next) => {
    const statusCode = err.statusCode || 500;
    console.error(err.message, err.stack);
    res.status(statusCode).json({ message: err.message });

    return;
});

app.listen(3000, function () {
    console.log('Example app listening on port 3000!');
});
