// NODE.JS CONNECT TO MSSQL

const sql = require("mssql");

const config = {
  server: "",
  database: "",
  user: "",
  password: "",
  options: {
    enableArithAbort: true,
  },
};

function connect() {
  const conn = new sql.ConnectionPool(config);
  const req = new sql.Request(conn);

  const query = `
  select * from dbo.Autorzy
  `;

  conn.connect((err) => {
    if (err) throw err;
    req.query(query, (err, res) => {
      if (err) throw err;
      else console.log(res);
      conn.close();
    });
  });
}

connect();
