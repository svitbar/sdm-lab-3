const express = require('express');

const app = express();

const PORT = 8080;

app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.get('/:id', (req, res) => {
  res.send(`Hello, ${req.params.id}!`);
});

app.listen(PORT, () => console.log(`Server is running on port ${PORT}`));
