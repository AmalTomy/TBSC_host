import dlib
import numpy as np
from PIL import Image
import os
from django.conf import settings
import face_recognition

def get_face_encodings(image_path):
    """
    Get face encodings from an image file
    """
    try:
        # Load the image using face_recognition (which uses dlib internally)
        image = face_recognition.load_image_file(image_path)
        
        # Get face encodings
        face_encodings = face_recognition.face_encodings(image)
        
        if not face_encodings:
            return None
        
        # Return the first face encoding found
        return face_encodings[0]
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return None

def compare_faces(known_encoding, unknown_encoding, tolerance=0.6):
   
    if known_encoding is None or unknown_encoding is None:
        return False
    
    face_distance = face_recognition.face_distance([known_encoding], unknown_encoding)
    
    return face_distance[0] <= tolerance

def detect_faces_in_image(image_path):
    try:
        image = face_recognition.load_image_file(image_path)
        
        face_locations = face_recognition.face_locations(image)
        
        return face_locations
    except Exception as e:
        print(f"Error detecting faces: {str(e)}")
        return []

def find_matching_persons(detected_image_path, tolerance=0.6):
    from .models import MissingPerson  
    
    detected_encoding = get_face_encodings(detected_image_path)
    
    if detected_encoding is None:
        return []
    
    matches = []
    
    missing_persons = MissingPerson.objects.filter(is_finished=False)
    
    for person in missing_persons:
        missing_person_encoding = get_face_encodings(person.image.path)
        
        if missing_person_encoding is not None:
            if compare_faces(missing_person_encoding, detected_encoding, tolerance):
                matches.append(person)
    
    return matches
