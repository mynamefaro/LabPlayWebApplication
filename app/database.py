import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from django.shortcuts import render,redirect 
# Use a service account
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "lab-play-a66af",
    "private_key_id": "e6e09f245b85a1f152db813a98bc0df5a29ec973",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDQUczalucCohAY\nWzomj0dllrKsB8KRWD/tJ8UNcsdqrnz7iP1APJTBiuOgS18C9VRczgF7xWC8SYKs\nEjI3pyBXVcMqpbO/k9DFQk6IEWBGfLRInjA6pD355CHGUuBzpSiKPe0iEe7rjqNB\nVHc4f5Qw66adoAw9uko9H4PfOxXqmJuBxUgHbOnbyA5TUtkDCiZcf6WwMA2Bqcjq\ncKNsDKIgwyhpoYfaaR/4sNZRtQw1lR32X6SNpGowSda5JnVa8SvH4FgG3wwpCrJt\nK8Yo8NXQu7W8EJzZa1RKJFoxLAhk4f8kNb8oZYrlV0MImya1cRiov3kmNXdJ7r2y\ntDjwh7aBAgMBAAECggEAAiS6qTZ2SAung2ik5N1X4blhkJg/2JkCMgwqYI9hcpKQ\nYfzbMOcEAih4sR81ahALfyz2IkePTZYADInfZGfe0vyPQTK/8mUF9+b3weSpNfB1\n4RgSQk2K/wrpjLiGQLUJVsAjtCm1E01owUpU3mBJrmXZAAmJNrViVYCr2FyA8Y9S\n/S+HiQh6LoXCy8jVcV6wZCsxcqwrBUm+/Tt2VrMsLOwXxzjcavtvsRhR0tfCD94j\n250BM9zZa6f+6GNa5Q+ItYMMlwGs7kMNVrNtVpU2cEWFGU42e8WnLV9uYPphW3BA\nolgmDPKLDT449ZqsL4xYwMF0+g1gF6HH4KW1eUx7AQKBgQD7r9JvVl2cWZ2ywcd2\nsSazwVDL/wpHpubZrLgburnca6tc17lbDxeCzzduyuPxyzF5iTyf+2ev7ssFkeby\nGOF96O3x/rz59CiZ+24JsQ1O6JOGdM+UjOtBuIevrGkyOr0JIJn8HO5vS+oIjTND\nD0nKtOpkxYpqCdDBv+mkVHPkkQKBgQDT47idghtel5LDQTPa91vh5Jw0OPMEs145\n6STjgKmhGZgZRn8nKMOgwbQGiB1RuyyzEpU7KZClT4Km/qds1A7BFpeANJN6oTZF\n11Gm87GInwemCydMIe3uvzCw8Y3wrme/wL+tXoGcgMXcBNi4ade4VnUiOxPGor5g\nQy1+FPHq8QKBgEsVTaLXUf/VoDz2oCmheZlAf3kL8aYkfVPMufPTxaSjHjEJTguD\nOhFU/gV4U34LjwvhzAsx9eG/TCOyPgJVN9fXCD0cMIYkt4QQROhxQDYdHf2LlW2M\niJZHlXrr5UoNyd0SM73JZ7weGohIj1VfFzV4uUAsyjkOCo/yT6Ita5FxAoGBAIsI\nwqv/omvoM3IRh7AnXVAVTPXrZHLyK2L+e6kYVLYT8DytiGOumOcUE0ex6uMlWYhL\nKka+2F3QlV90e3Gql9/VLiX+2cK+o7kiNz7Aav7FsyQd73RCUzi0lYOVjNif6A3n\nsR5Wg9+ok6vyNi6TrOwVNxj2ANz3DsplaiVwIulRAoGBAIx2x+Ng9IFQ9AIRQF/6\nM5lN59daYkabHK+35BV/ADfSVJXLxMCLaRGwK2DhAJHDVZnUPqKlnKROpAVdQXOd\nvig1Q6QaH0vHX/DCtPe5O2SpLHUe/bmN8r77gVXCWj3ewWTRDU31IOwCFfaaLXUA\nIwbhprmT5TRL9hCqBHgbcXa5\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-w2wc0@lab-play-a66af.iam.gserviceaccount.com",
    "client_id": "104502003729239009191",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-w2wc0%40lab-play-a66af.iam.gserviceaccount.com"
})
firebase_admin.initialize_app(cred)
db = firestore.client()


def add(doc,name,data) :
    doc_ref = db.collection(doc).document(name)
    doc_ref.set(data)

def get(doc) :
    try:
        doc_ref = db.collection(doc).order_by(u'like', direction=firestore.Query.DESCENDING)
        writes = doc_ref.stream()
        data = []
        for write in writes :
            data.append(write.to_dict())
        return data
    except:
        return "error"

def get_doc(doc,name) :
    doc_ref = db.collection(doc).document(name)
    try:
        writes = doc_ref.get()
        if(writes.to_dict()==None) :
            return "error"
        else:
            return writes.to_dict()
    except:
        return "error"

def update(doc,name,data) :
    doc_ref = db.collection(doc).document(name)
    try:
        print(data)
        doc_ref.update(data)
    except:
        return "error"
    return 0

#GET IF IT HAVE (==)
def search(doc,search,value) :
    try :
        doc_ref = db.collection(doc).where(search, u'==', value)
        writes = doc_ref.stream()
        data = []
        for write in writes :
            data.append(write.to_dict())
        return data
    except:
        return "error"

def delete(doc,name) :
    db.collection(doc).document(name).delete()
    return 0

def search_delete(doc,search,value) :
    doc_ref = db.collection(doc).where(search, u'==', value).stream()
    for ref in doc_ref :
        ref.reference.delete()
    return 0
 
def add_arr(doc,name,arr,val) :
    city_ref = db.collection(doc).document(name)
    city_ref.update({arr: firestore.ArrayUnion([val])})
    return 0

def remove_arr(doc,name,arr,val) :
    city_ref = db.collection(doc).document(name)
    city_ref.update({arr: firestore.ArrayRemove([val])})
    return 0