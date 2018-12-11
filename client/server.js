const express = require('express')
const fs = require('fs')
const app = express()

const PORT = 5001

app.get('/', (req, res) => res.send("Must construct additional routes"));
app.use('/static', express.static('dist'))

app.listen(PORT, () => console.log(`Listening on port ${PORT}`));
