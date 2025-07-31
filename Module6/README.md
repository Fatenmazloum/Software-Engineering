

🧪 Unit Test = Test one small part
Tests one function only

No database, no API

Example:
“Does this add() function give the right answer?”

🔗 Integration Test = Test how parts work together
Tests many things together

Includes API, database, or services

Example:
“When I call the API, does it talk to the database and give the right result?”


200	OK	Request was successful
400	Bad Request	You gave bad input (missing or wrong format)
500	Internal Error	Something broke inside the server

To push :
git init
git add .gitignore
git add. 
git status
git commit -m "add all folders"
git branch -M main
git remote add origin ........
git push -u origin main


✅ Supabase is a cloud platform that provides a hosted PostgreSQL database along with many extra features.

In other words, Supabase runs PostgreSQL for you in the cloud, so you don’t have to install or manage PostgreSQL yourself.

✅  If you deploy your app connected to Supabase’s managed database, then:

You don’t need a local database named myappdb.

You don’t need the course_role user you created locally.

You don’t need the local password (mypassword) you used for your local setup.

Because:
Your app uses the Supabase database — which has its own database name (usually postgres), user (postgres), and password (the one you set when creating your Supabase project).

Your connection string (DATABASE_URL) points directly to that remote Supabase database and credentials.
