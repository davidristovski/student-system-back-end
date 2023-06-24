##  Getting Started

### 1. Setup

```shell script
git clone https://github.com/davidristovski/student-system-back-end.git
```

#### The .env configuration file

This app needs some environment variables in order to work properly.
You can copy the `.env.template` file and fill in the missing `JWT_SECRET_KEY`
and `JWT_REFRESH_SECRET_KEY` with your own set of keys:

```commandline
cd student-system-back-end
cp .env.template .env
cat .env

API_V1_STR=/api/v1
JWT_SECRET_KEY=your_secret_key
JWT_REFRESH_SECRET_KEY=your_refresh_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=60
REFRESH_TOKEN_EXPIRE_MINUTES=10080
DATABASE_URI=sqlite:///database.db
TEST_DATABASE_URI=sqlite:///./test.db
```

You can generate these keys in Python like so:

```python
import secrets
secret_key = secrets.token_urlsafe(32)
refresh_secret_key = secrets.token_urlsafe(32)
print("JWT Secret Key:", secret_key)
print("JWT Refresh Secret Key:", refresh_secret_key)
```
Replace `your_secret_key` and `your_refresh_secret_key` in the `.env` file above
with the values printed from `secret_key` and `refresh_secret_key` respectively.

You can modify the rest of the environment variables if you wish.

Save the `.env` file with your new set of keys.

### 2. Running the `uvicorn` server directly.

Once the `.env` file has been configured, you can run the server directly in
your environment. Open up a new terminal window and do:
```bash
cd student-system-back-end

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

alembic upgrade head # this will run the migration(s)

uvicorn main:app --reload
```

### 3. Running via docker-compose

To run the app in a container, just do:
```commandline
docker-compose up --build
```

Once the server loads, the app will be live at [http://localhost:8000](http://localhost:8000).

## Documentation

FastAPI automatically generates documentation based on the specification of the endpoints you have written. You can find the docs at [http://localhost:8000/docs](http://localhost:8000/docs).

There's also the alternative version that can be found here: [http://localhost:8000/redoc](http://localhost:8000/redoc).

## Authentication

This app is using the "Password Grant Type" from Oauth2. Check the API docs above
on which of the endpoints are protected.

To create you user, use the `/api/v1/users` endpoint.
