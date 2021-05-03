// NODE.JS CONNECT TO MSSQL

const sql = require("mssql/msnodesqlv8");

const config = {
  server: "localhost\\SQLEXPRESS",
  database: "AdventureWorks2019",
  // user: "",      // user and password are required if you are connecting to remote database
  // password: "",
  driver: "msnodesqlv8",
  options: {
    enableArithAbort: true,
    trustedConnection: true, // change trustedConnection on false or delete this if you are connecting to remote database
  },
};

function connect() {
  const conn = new sql.ConnectionPool(config);
  const req = new sql.Request(conn);

  const query = `
  select top 5 JobTitle, OrganizationLevel from HumanResources.Employee
  `;

  conn.connect((err) => {
    if (err) throw err;
    req.query(query, (err, res) => {
      if (err) throw err;
      console.log(res);
      conn.close();
    });
  });
}

connect();
