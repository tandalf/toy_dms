Installing the app
==================
Make sure you have at least python 2.7 installed on your system. Also you 
should have [pip](https://packaging.python.org/installing/) installed on your system. Optionally, you can install 
[virtualenv](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) 
to ensure you dont polute your global environment by mistake.

Manual Installation
-------------------
You can clone, or download this project to install it. To clone, enter this 
command at your terminal.

    git clone https://github.com/tandalf/toy_dms.git


To proceed with installing the app, at your terminal, enter the 
following commands.
    
    cd toy_dms
    pip install -r requirements.txt
    django-admin migrate --settings=toy_dms.settings
    
Note that you do not need to setup any database. This project uses sqlite3
by default but nothing stops you from setting up other database systems
and configuring the project as needed.

Running the App
----------------
Still at the terminal, enter

    python manage.py runserver 8000 --settings=toy_dms.settings

This will make the project run at [http://localhost:8000/documents].





CRUD User
=========

Registration Endpoint (Create)
------------------------------
`http://localhost:8000/auth/registration/   (POST)`

Content Type: `application/json` 

Sample

    {
        "username": "ttt",
        "password1": "12345678_",
        "password2": "12345678_",
        "email": "ttt@live.com"
    }

Sample Response

    {
      "key": "7a4f51c9ae3173c0c38de9b6a379b83afc7c8048"
    }

The provided key is a token which can be used to authenticate each request
to the app by setting it in the header. 

E.g, `Authorization: Token 7a4f51c9ae3173c0c38de9b6a379b83afc7c8048`
The header key `Authorization` has a value of `Token 7a4f51c9ae3173c0c38de9b6a379b83afc7c8048`
Use this key on evey request that requires authentication.

Read Update Delete User
-----------------------
`http://localhost:8000/auth/user/` (GET, PUT, PATCH)

Content Type: `application/json` 

Sample

    {
      "pk": 1
      "username": "ony",
      "email": "ony@live.com",
      "first_name": "",
      "last_name": ""
    }

If the Auth header has been set correctly, this endpoint gives access to
the authenticated user.

Note
----
To create a user you have to use the `registration` endpoint




User Login
==========
`http://localhost:8000/auth/login/`  (POST)

Content Type: `application/json` 

Sample

    {
        "username": "ony",
        "password": "12345678_",
        "email": "ony@live.com"
    }

Sample output

    {
      "key": "7a4f51c9ae3173c0c38de9b6a379b83afc7c8048"
    }

The provided key should be used as the auth key in the header for protected 
resources.

User Logout
==========
`http://localhost:8000/auth/logout/`  (POST)

Content Type: `application/json` 







Document upload, status, and assignment
=======================================
Note
----
You should provide authentication details in the header to hit this endpoint.

`http://localhost:8000/documents/`    (GET, POST)

Content Type: `multipart/form-data` 

Sample

    assignee:       1
    status:         NEW
    description:    This is a sample description of the project.
    document:       "file/on/local/system"

This endpoint DOES NOT use the json format.

The `assignee` is the `pk` field of the user the document is being assigned to.

The `status` is the current document status which is set by either the
assignee or the assigner. The status must take on either one of the following 
values. `NEW, ASSIGNED, INPROG, DONE`.

The `description` field is a meta data field holding the description of the document.

The `document` field is the file on your file system which is the current 
document to be worked on.

Sample Response:
    
    {
      "url": "http://localhost:8000/documents/2/",
      "assigner": 2,
      "assignee": 1,
      "status": "ASSIGNED",
      "description": "this is a test document",
      "document": "http://localhost:8000/documents/docs/01bkb03p_88tAbCd.ppt"
    }

The `url` field of the response is a restful resource endpoint which points
to the document just created. While the `document` field it the url to the
downloadable file.

Update, Delete
--------------
`http://localhost:8000/documents/:id/`    (GET, PUT, DELETE)

Content Type: `multipart/form-data`

Where :id is the id of the document resource. An example url is 
`http://localhost:8000/documents/2/`.

The sample is the same as the POST version above.